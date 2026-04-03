# sync/

Scripts that pull live data from your outbound tool and CRM into the repo. Run these before the weekly-update skill to give Claude fresh numbers without manual data entry.

---

## Scripts

| Script | What it pulls | Configure |
|--------|--------------|-----------|
| `sync-campaign-results.py` | Reply rates, meeting rates, pipeline by campaign | Apollo / Outreach / Instantly API |
| `sync-signal-performance.py` | Signal performance by send volume | Outbound tool + CRM |

---

## Setup

```bash
cp .env.example .env
# Fill in your API keys — never commit .env to git
pip install -r sync/requirements.txt
```

Run manually:
```bash
python3 sync/sync-campaign-results.py
python3 sync/sync-signal-performance.py
```

Then run the weekly-update skill. Claude will read the freshly synced data automatically.

---

## Automating with OpenClaw

[OpenClaw](https://openclaw.ai) can trigger these scripts on a schedule, update the repo files, and message you on Slack when the update is ready for review. See the OpenClaw skill registry for a pre-built GTM repo skill.

---

## Output Format

Each script writes to a structured file that the weekly-update skill reads:

- `sync-campaign-results.py` → `outputs/campaigns/[campaign-name]/results-sync.json`
- `sync-signal-performance.py` → `context/signal-performance-sync.json`

These JSON files are gitignored by default (they contain live data). The weekly-update skill reads them and incorporates the numbers into its drafted updates.

### results-sync.json schema

```json
{
  "tool": "apollo | instantly | outreach",
  "campaign_id": "string",
  "campaign_name": "string",
  "synced_at": "ISO 8601 datetime",
  "sends": 0,
  "replies": 0,
  "meetings_booked": 0,
  "reply_rate": 0.0,
  "meeting_rate": 0.0
}
```

Note: `meetings_booked` and `meeting_rate` may be `null` for tools that don't track meetings natively (e.g., Instantly). The weekly-update skill handles nulls gracefully.

### signal-performance-sync.json schema

```json
{
  "synced_at": "ISO 8601 datetime",
  "signals": {
    "Signal Name": {
      "sends_90d": 0,
      "replies": 0,
      "meetings_booked": 0,
      "reply_rate": 0.0,
      "meeting_rate": 0.0,
      "source_campaigns": ["campaign-folder-name"]
    }
  }
}
```

### If a script fails

Common failure modes and fixes:

| Error | Likely cause | Fix |
|-------|-------------|-----|
| `API key not set` | Missing `.env` entry | Copy `.env.example` to `.env` and fill in keys |
| `No campaign found matching...` | Campaign name mismatch | Update `CAMPAIGN_TO_SIGNAL_MAP` in `sync-signal-performance.py` |
| `No results-sync.json files found` | `sync-campaign-results.py` hasn't run | Run campaign sync first, then signal sync |
| `HTTP 401 / 403` | API key invalid or expired | Regenerate key in your outbound tool |

If the weekly-update skill runs without fresh sync data, it will note which numbers are stale rather than use incorrect data.
