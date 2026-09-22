"""
sync-campaign-results.py

Pulls campaign metrics from your outbound tool API and writes them to
outputs/campaigns/[campaign]/results-sync.json for the weekly-update skill to read.

Supported tools: Apollo.io, Instantly, Outreach (configure via .env)

Usage:
    python3 sync/sync-campaign-results.py
    python3 sync/sync-campaign-results.py --campaign "series-b-revops-tier2"

Requirements:
    pip install -r sync/requirements.txt
"""

import os
import sys
import json
import time
import logging
import argparse
from datetime import datetime, timedelta
from pathlib import Path

try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    print("python-dotenv not installed. Run: pip install -r sync/requirements.txt")

try:
    import requests
except ImportError:
    print("requests not installed. Run: pip install -r sync/requirements.txt")
    sys.exit(1)

# --- Logging ------------------------------------------------------------------

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
)
log = logging.getLogger("sync-campaign-results")

LOG_FILE = os.getenv("SYNC_LOG_FILE")
if LOG_FILE:
    fh = logging.FileHandler(LOG_FILE)
    fh.setFormatter(logging.Formatter("%(asctime)s [%(levelname)s] %(message)s"))
    log.addHandler(fh)

# --- Configuration -----------------------------------------------------------

OUTBOUND_TOOL = os.getenv("OUTBOUND_TOOL", "apollo")  # apollo | instantly | outreach
APOLLO_API_KEY = os.getenv("APOLLO_API_KEY")
INSTANTLY_API_KEY = os.getenv("INSTANTLY_API_KEY")
OUTREACH_API_KEY = os.getenv("OUTREACH_API_KEY")

CAMPAIGNS_DIR = Path("outputs/campaigns")
LOOKBACK_DAYS = int(os.getenv("SYNC_LOOKBACK_DAYS", "7"))

MAX_RETRIES = 3
RETRY_BACKOFF = [2, 5, 15]

# -----------------------------------------------------------------------------


def retry_request(method, url, **kwargs):
    """Retry HTTP requests on transient failures (429, 503)."""
    for attempt in range(MAX_RETRIES):
        resp = method(url, **kwargs)
        if resp.status_code == 429:
            retry_after = int(resp.headers.get("Retry-After", RETRY_BACKOFF[attempt]))
            log.warning(f"Rate limited (429). Retrying in {retry_after}s (attempt {attempt + 1}/{MAX_RETRIES})")
            time.sleep(retry_after)
            continue
        if resp.status_code == 503:
            log.warning(f"Service unavailable (503). Retrying in {RETRY_BACKOFF[attempt]}s (attempt {attempt + 1}/{MAX_RETRIES})")
            time.sleep(RETRY_BACKOFF[attempt])
            continue
        return resp
    return resp


def fetch_apollo_campaign_metrics(campaign_name: str) -> dict:
    """
    Fetch sequence metrics from Apollo.io.
    Docs: https://apolloio.github.io/apollo-api-docs/
    """
    if not APOLLO_API_KEY:
        raise ValueError("APOLLO_API_KEY not set in .env")

    headers = {"X-Api-Key": APOLLO_API_KEY, "Content-Type": "application/json"}

    resp = retry_request(
        requests.get,
        "https://api.apollo.io/v1/emailer_campaigns",
        headers=headers,
        params={"q_name": campaign_name, "per_page": 10},
    )
    resp.raise_for_status()
    sequences = resp.json().get("emailer_campaigns", [])

    if not sequences:
        log.info(f"  No Apollo sequence found matching: {campaign_name}")
        return {}

    seq = sequences[0]
    seq_id = seq["id"]

    stats_resp = retry_request(
        requests.get,
        f"https://api.apollo.io/v1/emailer_campaigns/{seq_id}/emailer_campaign_analytics",
        headers=headers,
    )
    stats_resp.raise_for_status()
    stats = stats_resp.json().get("emailer_campaign_analytics", {})

    sent = stats.get("num_sent_emails", 0)
    replies = stats.get("num_replied_emails", 0)
    meetings = stats.get("num_meetings_booked", 0)

    return {
        "tool": "apollo",
        "campaign_id": seq_id,
        "campaign_name": seq.get("name"),
        "synced_at": datetime.utcnow().isoformat(),
        "sends": sent,
        "replies": replies,
        "meetings_booked": meetings,
        "reply_rate": round(replies / sent, 4) if sent > 0 else 0,
        "meeting_rate": round(meetings / sent, 4) if sent > 0 else 0,
    }


def fetch_instantly_campaign_metrics(campaign_name: str) -> dict:
    """
    Fetch campaign analytics from Instantly.ai.
    Docs: https://developer.instantly.ai/
    """
    if not INSTANTLY_API_KEY:
        raise ValueError("INSTANTLY_API_KEY not set in .env")

    headers = {"Authorization": f"Bearer {INSTANTLY_API_KEY}"}

    resp = retry_request(
        requests.get,
        "https://api.instantly.ai/api/v1/campaign/list",
        headers=headers,
        params={"limit": 100},
    )
    resp.raise_for_status()
    campaigns = resp.json().get("data", [])

    match = next((c for c in campaigns if campaign_name.lower() in c["name"].lower()), None)
    if not match:
        log.info(f"  No Instantly campaign found matching: {campaign_name}")
        return {}

    campaign_id = match["id"]
    analytics_resp = retry_request(
        requests.get,
        f"https://api.instantly.ai/api/v1/analytics/campaign/summary",
        headers=headers,
        params={"campaign_id": campaign_id},
    )
    analytics_resp.raise_for_status()
    data = analytics_resp.json()

    sent = data.get("total_sent", 0)
    replies = data.get("total_replied", 0)

    return {
        "tool": "instantly",
        "campaign_id": campaign_id,
        "campaign_name": match["name"],
        "synced_at": datetime.utcnow().isoformat(),
        "sends": sent,
        "replies": replies,
        "meetings_booked": None,
        "reply_rate": round(replies / sent, 4) if sent > 0 else 0,
        "meeting_rate": None,
    }


def sync_campaign(campaign_name: str) -> dict:
    """Sync a single campaign by name. Returns metrics dict or empty dict."""
    if OUTBOUND_TOOL == "apollo":
        return fetch_apollo_campaign_metrics(campaign_name)
    elif OUTBOUND_TOOL == "instantly":
        return fetch_instantly_campaign_metrics(campaign_name)
    else:
        log.error(f"  Unsupported tool: {OUTBOUND_TOOL}. Supported: apollo, instantly")
        return {}


def sync_all_campaigns():
    """Sync metrics for all campaign folders found in outputs/campaigns/."""
    if not CAMPAIGNS_DIR.exists():
        log.error(f"No campaigns directory found at {CAMPAIGNS_DIR}")
        sys.exit(1)

    campaign_dirs = [d for d in CAMPAIGNS_DIR.iterdir() if d.is_dir()]
    if not campaign_dirs:
        log.info("No campaign folders found in outputs/campaigns/")
        return

    log.info(f"Found {len(campaign_dirs)} campaign(s). Syncing from {OUTBOUND_TOOL}...")

    errors = 0
    synced = 0

    for campaign_dir in campaign_dirs:
        campaign_name = campaign_dir.name
        log.info(f"  Syncing: {campaign_name}")

        try:
            metrics = sync_campaign(campaign_name)

            if not metrics:
                continue

            output_path = campaign_dir / "results-sync.json"
            with open(output_path, "w") as f:
                json.dump(metrics, f, indent=2)

            log.info(f"  Wrote {output_path}")
            log.info(f"    Sends: {metrics.get('sends')} | Replies: {metrics.get('replies')} | "
                      f"Reply rate: {metrics.get('reply_rate', 0):.1%} | "
                      f"Meetings: {metrics.get('meetings_booked', 'n/a')}")
            synced += 1

        except ValueError as e:
            log.error(f"  Configuration error for {campaign_name}: {e}")
            log.error("  Fix: check sync/.env.example and ensure all required API keys are set in .env")
            errors += 1
        except requests.exceptions.HTTPError as e:
            status = e.response.status_code if e.response else "unknown"
            log.error(f"  API error for {campaign_name}: HTTP {status}")
            if status == 401:
                log.error(f"  Fix: your {OUTBOUND_TOOL} API key is invalid or expired. Regenerate it in the {OUTBOUND_TOOL} dashboard.")
            elif status == 403:
                log.error(f"  Fix: your {OUTBOUND_TOOL} API key lacks permission for this endpoint. Check API scopes.")
            errors += 1
        except requests.exceptions.ConnectionError:
            log.error(f"  Connection failed for {campaign_name}. Check your internet connection and the {OUTBOUND_TOOL} API status page.")
            errors += 1
        except Exception as e:
            log.error(f"  Unexpected error syncing {campaign_name}: {e}")
            errors += 1

    if errors > 0:
        log.error(f"\n{errors} campaign(s) failed to sync. See errors above.")
        sys.exit(1)
    else:
        log.info(f"\n{synced} campaign(s) synced successfully. Run the weekly-update skill to incorporate these numbers.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Sync campaign results from outbound tool")
    parser.add_argument("--campaign", help="Sync a specific campaign folder name only")
    args = parser.parse_args()

    if args.campaign:
        campaign_dir = CAMPAIGNS_DIR / args.campaign
        if not campaign_dir.exists():
            log.error(f"Campaign folder not found: {campaign_dir}")
            sys.exit(1)

        log.info(f"Syncing single campaign: {args.campaign}")
        try:
            metrics = sync_campaign(args.campaign)
            if metrics:
                output_path = campaign_dir / "results-sync.json"
                with open(output_path, "w") as f:
                    json.dump(metrics, f, indent=2)
                log.info(f"Wrote {output_path}")
            else:
                log.error(f"No metrics returned for {args.campaign}")
                sys.exit(1)
        except ValueError as e:
            log.error(f"Configuration error: {e}")
            log.error("Fix: check sync/.env.example and ensure all required API keys are set in .env")
            sys.exit(1)
        except requests.exceptions.HTTPError as e:
            status = e.response.status_code if e.response else "unknown"
            log.error(f"API error: HTTP {status}")
            sys.exit(1)
        except requests.exceptions.ConnectionError:
            log.error(f"Connection failed. Check your internet connection and the {OUTBOUND_TOOL} API status page.")
            sys.exit(1)
    else:
        sync_all_campaigns()
