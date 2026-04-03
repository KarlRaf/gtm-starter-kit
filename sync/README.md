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
