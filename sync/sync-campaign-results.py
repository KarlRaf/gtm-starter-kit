"""
sync-campaign-results.py

Pulls campaign metrics from your outbound tool API and writes them to
outputs/campaigns/[campaign]/results-sync.json for the weekly-update skill to read.

Supported tools: Apollo.io, Instantly, Outreach (configure via .env)

Usage:
    python3 sync/sync-campaign-results.py
    python3 sync/sync-campaign-results.py --campaign "series-b-revops-tier2"

Requirements:
    pip install requests python-dotenv
"""

import os
import json
import argparse
from datetime import datetime, timedelta
from pathlib import Path

# Load environment variables from .env
try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    print("python-dotenv not installed. Run: pip install python-dotenv")

# --- Configuration -----------------------------------------------------------
# Set these in your .env file, never hardcode here.

OUTBOUND_TOOL = os.getenv("OUTBOUND_TOOL", "apollo")  # apollo | instantly | outreach
APOLLO_API_KEY = os.getenv("APOLLO_API_KEY")
INSTANTLY_API_KEY = os.getenv("INSTANTLY_API_KEY")
OUTREACH_API_KEY = os.getenv("OUTREACH_API_KEY")

CAMPAIGNS_DIR = Path("outputs/campaigns")
LOOKBACK_DAYS = int(os.getenv("SYNC_LOOKBACK_DAYS", "7"))

# -----------------------------------------------------------------------------


def fetch_apollo_campaign_metrics(campaign_name: str) -> dict:
    """
    Fetch sequence metrics from Apollo.io.
    Docs: https://apolloio.github.io/apollo-api-docs/
    """
    import requests

    if not APOLLO_API_KEY:
        raise ValueError("APOLLO_API_KEY not set in .env")

    headers = {"X-Api-Key": APOLLO_API_KEY, "Content-Type": "application/json"}

    # Apollo: list sequences and find matching one
    resp = requests.get(
        "https://api.apollo.io/v1/emailer_campaigns",
        headers=headers,
        params={"q_name": campaign_name, "per_page": 10},
    )
    resp.raise_for_status()
    sequences = resp.json().get("emailer_campaigns", [])

    if not sequences:
        print(f"  No Apollo sequence found matching: {campaign_name}")
        return {}

    seq = sequences[0]
    seq_id = seq["id"]

    # Fetch stats for this sequence
    stats_resp = requests.get(
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
    import requests

    if not INSTANTLY_API_KEY:
        raise ValueError("INSTANTLY_API_KEY not set in .env")

    headers = {"Authorization": f"Bearer {INSTANTLY_API_KEY}"}

    resp = requests.get(
        "https://api.instantly.ai/api/v1/campaign/list",
        headers=headers,
        params={"limit": 100},
    )
    resp.raise_for_status()
    campaigns = resp.json().get("data", [])

    match = next((c for c in campaigns if campaign_name.lower() in c["name"].lower()), None)
    if not match:
        print(f"  No Instantly campaign found matching: {campaign_name}")
        return {}

    campaign_id = match["id"]
    analytics_resp = requests.get(
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
        "meetings_booked": None,  # Instantly doesn't track meetings natively
        "reply_rate": round(replies / sent, 4) if sent > 0 else 0,
        "meeting_rate": None,
    }


def sync_all_campaigns():
    """Sync metrics for all campaign folders found in outputs/campaigns/."""
    if not CAMPAIGNS_DIR.exists():
        print(f"No campaigns directory found at {CAMPAIGNS_DIR}")
        return

    campaign_dirs = [d for d in CAMPAIGNS_DIR.iterdir() if d.is_dir()]
    if not campaign_dirs:
        print("No campaign folders found in outputs/campaigns/")
        return

    print(f"Found {len(campaign_dirs)} campaign(s). Syncing from {OUTBOUND_TOOL}...\n")

    for campaign_dir in campaign_dirs:
        campaign_name = campaign_dir.name
        print(f"  Syncing: {campaign_name}")

        try:
            if OUTBOUND_TOOL == "apollo":
                metrics = fetch_apollo_campaign_metrics(campaign_name)
            elif OUTBOUND_TOOL == "instantly":
                metrics = fetch_instantly_campaign_metrics(campaign_name)
            else:
                print(f"  Unsupported tool: {OUTBOUND_TOOL}. Add your integration above.")
                continue

            if not metrics:
                continue

            output_path = campaign_dir / "results-sync.json"
            with open(output_path, "w") as f:
                json.dump(metrics, f, indent=2)

            print(f"  Wrote {output_path}")
            print(f"    Sends: {metrics.get('sends')} | Replies: {metrics.get('replies')} | "
                  f"Reply rate: {metrics.get('reply_rate', 0):.1%} | "
                  f"Meetings: {metrics.get('meetings_booked', 'n/a')}")

        except Exception as e:
            print(f"  Error syncing {campaign_name}: {e}")

    print("\nSync complete. Run the weekly-update skill to incorporate these numbers.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Sync campaign results from outbound tool")
    parser.add_argument("--campaign", help="Sync a specific campaign folder name only")
    args = parser.parse_args()

    if args.campaign:
        campaign_dir = CAMPAIGNS_DIR / args.campaign
        if not campaign_dir.exists():
            print(f"Campaign folder not found: {campaign_dir}")
        else:
            print(f"Syncing single campaign: {args.campaign}")
            if OUTBOUND_TOOL == "apollo":
                metrics = fetch_apollo_campaign_metrics(args.campaign)
            elif OUTBOUND_TOOL == "instantly":
                metrics = fetch_instantly_campaign_metrics(args.campaign)
            if metrics:
                output_path = campaign_dir / "results-sync.json"
                with open(output_path, "w") as f:
                    json.dump(metrics, f, indent=2)
                print(f"Wrote {output_path}")
    else:
        sync_all_campaigns()
