"""
sync-signal-performance.py

Aggregates performance metrics across all campaign results-sync.json files
and writes a summary to context/signal-performance-sync.json.

The weekly-update skill reads this file to draft updated signal performance
log entries without requiring manual metric transcription.

Usage:
    python3 sync/sync-signal-performance.py

Requirements:
    pip install -r sync/requirements.txt
"""

import json
import os
import sys
import logging
from datetime import datetime
from pathlib import Path
from collections import defaultdict

# --- Logging ------------------------------------------------------------------

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
)
log = logging.getLogger("sync-signal-performance")

LOG_FILE = os.getenv("SYNC_LOG_FILE")
if LOG_FILE:
    fh = logging.FileHandler(LOG_FILE)
    fh.setFormatter(logging.Formatter("%(asctime)s [%(levelname)s] %(message)s"))
    log.addHandler(fh)

# --- Configuration -----------------------------------------------------------

CAMPAIGNS_DIR = Path("outputs/campaigns")
OUTPUT_PATH = Path("context/signal-performance-sync.json")

# Map campaign name patterns to signal names.
# Edit this to match your actual campaign folder names and signal library.
CAMPAIGN_TO_SIGNAL_MAP = {
    "series-b": "Series B Announced (last 60 days)",
    "revops-hire": "New RevOps Hire (last 30 days)",
    "job-posting": "2+ RevOps Job Postings Active",
    "dual-stack": "HubSpot + Salesforce Dual Stack",
    "linkedin-intent": "LinkedIn Post About Manual Processes",
    "g2-intent": "G2 Review of Zapier Teams",
}


def infer_signal(campaign_name: str) -> str:
    """Map a campaign folder name to a signal name using the map above."""
    campaign_lower = campaign_name.lower()
    for key, signal in CAMPAIGN_TO_SIGNAL_MAP.items():
        if key in campaign_lower:
            return signal
    return "Unknown Signal"


def aggregate():
    signal_data = defaultdict(lambda: {"sends": 0, "replies": 0, "meetings": 0, "campaigns": []})

    if not CAMPAIGNS_DIR.exists():
        log.error(f"No campaigns directory at {CAMPAIGNS_DIR}")
        sys.exit(1)

    errors = 0
    synced_count = 0
    for campaign_dir in CAMPAIGNS_DIR.iterdir():
        if not campaign_dir.is_dir():
            continue

        sync_file = campaign_dir / "results-sync.json"
        if not sync_file.exists():
            continue

        try:
            with open(sync_file) as f:
                data = json.load(f)

            signal = infer_signal(campaign_dir.name)
            signal_data[signal]["sends"] += data.get("sends", 0)
            signal_data[signal]["replies"] += data.get("replies", 0)
            signal_data[signal]["meetings"] += data.get("meetings_booked") or 0
            signal_data[signal]["campaigns"].append(campaign_dir.name)
            synced_count += 1

        except json.JSONDecodeError as e:
            log.error(f"  Invalid JSON in {sync_file}: {e}")
            log.error(f"  Fix: delete {sync_file} and re-run sync-campaign-results.py")
            errors += 1
        except Exception as e:
            log.error(f"  Error reading {sync_file}: {e}")
            errors += 1

    if synced_count == 0:
        log.error("No results-sync.json files found. Run sync-campaign-results.py first.")
        sys.exit(1)

    output = {
        "synced_at": datetime.utcnow().isoformat(),
        "signals": {}
    }

    for signal, data in signal_data.items():
        sends = data["sends"]
        replies = data["replies"]
        meetings = data["meetings"]
        output["signals"][signal] = {
            "sends_90d": sends,
            "replies": replies,
            "meetings_booked": meetings,
            "reply_rate": round(replies / sends, 4) if sends > 0 else 0,
            "meeting_rate": round(meetings / sends, 4) if sends > 0 else 0,
            "source_campaigns": data["campaigns"],
        }

    with open(OUTPUT_PATH, "w") as f:
        json.dump(output, f, indent=2)

    log.info(f"Signal performance summary written to {OUTPUT_PATH}")
    log.info(f"\nSummary ({synced_count} campaign(s) aggregated):\n")

    for signal, stats in output["signals"].items():
        log.info(f"  {signal}")
        log.info(f"    Sends: {stats['sends_90d']} | Reply rate: {stats['reply_rate']:.1%} | "
                  f"Meeting rate: {stats['meeting_rate']:.1%}")

    if errors > 0:
        log.error(f"\n{errors} file(s) had errors. See above.")
        sys.exit(1)
    else:
        log.info("\nRun the weekly-update skill to incorporate these into the signal performance log.")


if __name__ == "__main__":
    aggregate()
