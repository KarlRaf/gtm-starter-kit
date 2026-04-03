# Skill: ICP Scoring

**Duration:** 15–30 minutes per account (or run in batch)
**Output:** ICP score + tier assignment saved to CRM or `outputs/scoring/`

---

## Quick Start

Single account:
```
Read skills/icp-scoring/SKILL.md and score [company.com] against our ICP
```

Batch:
```
Read skills/icp-scoring/SKILL.md and context/icp-definition.md.
Score these companies and output a table sorted by score, Tier 1 flagged:
[paste list of company names or domains]
```

---

## Purpose

Score any account against your ICP and assign it to the right tier. Replaces gut feel with a repeatable model. When run at scale, it tells you which accounts to prioritize this week, which to monitor, and which to skip entirely.

---

## When to Run This Skill

- New accounts entering the pipeline — score before assigning to a rep
- Enrichment run complete — re-score the full account list
- ICP definition updated — re-score to find newly qualified accounts
- Preparing a campaign list — score to determine sequence tier
- Quarterly pipeline review — re-score all open opportunities

## Re-scoring Cadence

Scores go stale. Set a recurring schedule:

| Segment | Frequency | Why |
|---------|-----------|-----|
| Full account list | Quarterly | ICP drift, new signal data |
| Tier 1 accounts | Monthly | High-value; worth tracking closely |
| Active pipeline | After each campaign | Campaign results reveal scoring gaps |
| After ICP change | Immediately | Find newly qualified or disqualified accounts |

After a quarterly re-score, pull the delta: which accounts moved tiers? Accounts that dropped from Tier 1 to Tier 2 need to be removed from AE pipelines. Accounts that moved up need to be activated.

---

## Inputs

- Account name, domain, and available firmographic/technographic data
- `context/icp-definition.md` — scoring criteria and tier definitions
- `context/signal-library.md` — signal scores to add on top of ICP fit

---

## Scoring Model

### Part 1: ICP Fit Score (0–70 points)

Measure how well the account matches your ideal customer profile.

#### Firmographic Fit (0–30 points)

| Criterion | Points | How to assess |
|-----------|--------|---------------|
| Employee count in range | 0–10 | [Your range from ICP definition] |
| Industry match | 0–10 | Primary = 10, Secondary = 5, Other = 0 |
| Funding stage match | 0–10 | Ideal stage = 10, Adjacent = 5, Outside = 0 |

#### Technographic Fit (0–20 points)

| Criterion | Points | How to assess |
|-----------|--------|---------------|
| Uses [key integration tool] | 0–10 | Confirms workflow match |
| Uses [secondary tool] | 0–5 | Confirms sophistication level |
| No [disqualifying tool] | 0–5 | Absence of competitive blocker |

#### Organizational Fit (0–20 points)

| Criterion | Points | How to assess |
|-----------|--------|---------------|
| Has [key role/function] | 0–10 | Confirms decision-maker exists |
| [Role] hired in last 12 months | 0–5 | New leader = change appetite |
| Hiring for [relevant role] | 0–5 | Active investment in function |

---

### Part 2: Signal Score (0–30 points)

Add points for active signals from `context/signal-library.md`. Reference the point values defined there.

**Note:** Signal scores decay over time. Apply the decay multipliers from `context/signal-library.md` — a signal at 91–180 days is worth 25% of its original value; at 180+ days it expires entirely.

---

### Total Score Interpretation

| Total | Tier | Action |
|-------|------|--------|
| 80–100 | Tier 1 | Immediate outreach, full research (run Account Research skill), assign to AE |
| 60–79 | Tier 2 | Signal-triggered sequence within 48 hours |
| 40–59 | Tier 3 | Add to automated sequence |
| 20–39 | Tier 4 | Monitor, re-score in 90 days |
| 0–19 | Exclude | Remove from active list |

---

## Running at Scale (Batch Scoring)

When scoring a large list (50+ accounts), structure the output as a table:

```
| Account | Domain | Firmographic | Technographic | Org | Signal | Total | Tier | Action |
```

Instruct Claude:
```
Read skills/icp-scoring/SKILL.md and context/icp-definition.md.
Score the accounts in [file or pasted list].
Output a scored table sorted by total score descending.
Flag any accounts scoring 80+ for immediate follow-up.
```

---

## Scoring Output Format

```markdown
# ICP Score: [Company Name]
Date scored: [YYYY-MM-DD]
Scored by: [Claude / Name]

## Score Breakdown

| Category | Score | Max | Notes |
|----------|-------|-----|-------|
| Firmographic fit | X | 30 | [Key observations] |
| Technographic fit | X | 20 | [Key observations] |
| Organizational fit | X | 20 | [Key observations] |
| Active signals | X | 30 | [Signals present] |
| **Total** | **X** | **100** | |

## Tier Assignment: [Tier 1 / 2 / 3 / 4 / Exclude]

## What Qualifies Them
- [Specific reason 1]
- [Specific reason 2]

## What Disqualifies or Reduces Score
- [Gap 1 — what would need to change for this to be a higher tier]

## Recommended Next Action
[Specific: which skill to run next, which sequence to assign, or what to monitor]

## Re-score Trigger
[Condition that should trigger re-scoring — e.g., "If they raise a new round" or "If they hire a VP of Ops"]
```

---

## Calibration Notes

*Update this section when you find scoring gaps — accounts that scored high but churned, or accounts that scored low but converted.*

| Date | Account | Scored | Actual outcome | What the model missed |
|------|---------|--------|---------------|----------------------|
| | | | | |

Run a calibration review quarterly: pull the last 90 days of scored accounts and compare predicted tier to actual outcome. Adjust point values where the model is consistently wrong.
