"""
sync-signal-performance.py

Aggregates performance metrics across all campaign results-sync.json files
and writes a summary to context/signal-performance-sync.json.

The weekly-update skill reads this file to draft updated signal performance
log entries without requiring manual metric transcription.

Usage:
    python3 sync/sync-signal-performance.py

Requirements:
    pip install python-dotenv
"""

import json
import os
from datetime import datetime
from pathlib import Path
from collections import defaultdict

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
        print(f"No campaigns directory at {CAMPAIGNS_DIR}")
        return

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

        except Exception as e:
            print(f"  Error reading {sync_file}: {e}")

    if synced_count == 0:
        print("No results-sync.json files found. Run sync-campaign-results.py first.")
        return

    # Build output
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

    print(f"Signal performance summary written to {OUTPUT_PATH}")
    print(f"\nSummary ({synced_count} campaign(s) aggregated):\n")

    for signal, stats in output["signals"].items():
        print(f"  {signal}")
        print(f"    Sends: {stats['sends_90d']} | Reply rate: {stats['reply_rate']:.1%} | "
              f"Meeting rate: {stats['meeting_rate']:.1%}")

    print("\nRun the weekly-update skill to incorporate these into the signal performance log.")


if __name__ == "__main__":
    aggregate()
