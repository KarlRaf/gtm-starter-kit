# Skill: Weekly Context Update

**Duration:** 10–15 minutes
**Cadence:** Weekly (Monday morning recommended)
**Output:** Updated context files + a brief change log entry

---

## Quick Start

```
Read skills/weekly-update/SKILL.md and run the weekly context update.
```

That's it. Claude will read the current state of the repo, identify what's stale, draft every section that needs updating, and ask you to fill in the parts it can't know.

---

## Purpose

Keep the repo accurate without making maintenance feel like a second job. This skill handles the diff — what changed since last week — rather than asking you to rewrite everything from scratch.

The output is a set of proposed edits, not final commits. You review, adjust, approve. Claude drafts; you decide.

---

## What Claude Reads

Before producing any output, Claude reads:

1. `CLAUDE.md` — current priorities, active campaigns, team focus
2. `context/signal-library.md` — signal performance log and last-updated date
3. `context/icp-definition.md` — ICP evolution log and last-updated date
4. `context/competitor-radar.md` — win/loss patterns and last-updated date
5. All files in `outputs/campaigns/` — active campaigns and their results tables
6. Any files in `outputs/` dated in the last 14 days

---

## Step 1: Staleness Check

Claude identifies which sections are out of date based on last-updated dates and campaign activity.

Flag any of the following:

| File / Section | Stale if... |
|---------------|-------------|
| `CLAUDE.md` → Current priorities | Not updated in the last 7 days |
| Signal performance log | A campaign has been live for 14+ days with no results recorded |
| Campaign results table | Campaign is live but results rows are empty or older than 7 days |
| Competitor radar | Last updated more than 60 days ago |
| ICP evolution log | Last updated more than 90 days ago |

Print a summary of what's stale before drafting anything.

---

## Step 2: Draft Updates

For each stale section, draft a proposed update. Use this format:

```
### [File] — [Section]
Last updated: [date]
Status: STALE — [reason]

CURRENT:
[existing content]

PROPOSED:
[drafted update based on what Claude can infer from the repo]

QUESTIONS FOR YOU:
- [anything Claude can't know — requires human input]
```

Work through each stale section in order of impact:

### 2a. CLAUDE.md — Current Priorities

Draft a new "Current priorities" block based on:
- Which campaigns are currently live (from `outputs/campaigns/`)
- What signals are active (from `context/signal-library.md`)
- What was in last week's priorities (carry forward anything still relevant)

Then ask:
- What changed this week that's not reflected in the repo?
- Any new accounts or segments becoming a focus?
- Any campaigns pausing or wrapping up?

### 2b. Signal Performance Log

Pull results from any campaign output files updated in the last 7 days. For each active signal:
- Count sends, replies, and meetings booked from the campaign results table
- Calculate reply rate and meeting rate
- Compare to the existing log entry
- Draft an updated row if the numbers changed

Flag: if a signal has 30+ sends with no meetings booked, note it explicitly. That's a calibration signal.

### 2c. Active Campaign Results

For each campaign in `outputs/campaigns/` with a live results table:
- Identify the most recent row
- Note if it hasn't been updated in 7+ days
- Draft a placeholder row for this week with the date filled in and metrics as `[update]`

Ask: what are the current reply, meeting, and pipeline numbers for each live campaign?

### 2d. Competitor Radar (if stale)

If `context/competitor-radar.md` hasn't been updated in 60+ days:
- Flag it
- Ask: any competitive deals won or lost since the last update? Any new objections you're hearing that aren't in the battlecard?

Do not draft a competitive update without input — competitive intel requires human knowledge. Just surface the flag and ask the question.

### 2e. ICP Evolution Log (if stale)

If the evolution log hasn't been updated in 90+ days:
- Draft a log entry template pre-filled with today's date
- Ask: has anything changed about who you're targeting? A segment that's underperforming? A new company type showing up in pipeline?

---

## Step 3: Confirm and Apply

Present all proposed changes in one response. For each:

- Show CURRENT vs. PROPOSED side by side
- Mark sections that need human input with `[NEEDS YOUR INPUT]`
- After confirmation, apply all approved changes to the relevant files

Do not apply changes until the user confirms. Do not invent performance data — if numbers aren't in the repo, ask for them.

---

## Output

No separate output file. Changes are applied directly to the relevant context files. Add a one-line entry to `outputs/weekly-log.md` (create it if it doesn't exist):

```
YYYY-MM-DD: Updated [list of files changed]. [One sentence on the most significant change.]
```

This log lets you track how the repo has evolved over time without digging through git history.

---

## If You're Using Automated Data Sync

If you have scripts in `sync/` that pull campaign metrics from your outbound tool or CRM, run them before this skill:

```bash
python3 sync/sync-campaign-results.py
python3 sync/sync-signal-performance.py
```

Then run the skill. Claude will read the freshly synced data and incorporate it into the drafted updates automatically — no manual metric entry required.

**Running this automatically with OpenClaw:** [OpenClaw](https://openclaw.ai) is an open-source AI agent that runs locally and can trigger this entire workflow on a schedule — pull metrics via browser automation, update the data files, run this skill, and message you on Slack with the draft for review. See the OpenClaw skill registry for a pre-built GTM repo update skill, or configure your own using the `sync/` scripts as the data layer.
