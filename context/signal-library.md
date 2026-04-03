# Signal Library

*Signals are observable events that predict pipeline conversion 30–90 days in advance. This library is the source of truth for all signal-based outreach. Every campaign in this repo traces back to at least one signal here.*

Last updated: [YYYY-MM-DD]

---

## Signal Scoring Model

Accounts accumulate points as signals fire. Thresholds determine outreach intensity.

| Score | Tier | Action |
|-------|------|--------|
| 80–100 | Hot | Immediate outreach, Tier 1 sequence |
| 60–79 | Warm | Tier 2 sequence within 48 hours |
| 40–59 | Cool | Add to Tier 3 nurture |
| 0–39 | Cold | Monitor only |

---

## Tier 1 Signals — Act Immediately

*High predictive power. When a Tier 1 signal fires, outreach goes out within 24 hours.*

### Signal: [Signal Name]
**Category:** [Firmographic / Technographic / Behavioral / Organizational / Intent]
**Points:** [30–40]
**Source:** [Clay / LinkedIn / Crunchbase / Custom / etc.]
**Refresh cadence:** [Real-time / Daily / Weekly]

**Definition:** [Exactly what event or attribute constitutes this signal]

**Why it predicts fit:** [The causal logic — why does this event correlate with buying intent?]

**Detection method:**
```
[How to detect it — Clay formula, API, manual check, etc.]
```

**Message hook:** [The one-liner that references this signal in outreach, e.g., "Saw you raised your Series B last week — congrats."]

---

### Signal: [Signal Name]
**Category:** [Category]
**Points:** [30–40]
**Source:** [Source]
**Refresh cadence:** [Cadence]

**Definition:** [Definition]

**Why it predicts fit:** [Logic]

**Detection method:**
```
[Method]
```

**Message hook:** [Hook]

---

## Tier 2 Signals — Add to Active Sequences

*Moderate predictive power. Use to prioritize within existing sequences or trigger lighter outreach.*

### Signal: [Signal Name]
**Category:** [Category]
**Points:** [15–25]
**Source:** [Source]

**Definition:** [Definition]

**Why it predicts fit:** [Logic]

---

### Signal: [Signal Name]
**Category:** [Category]
**Points:** [15–25]
**Source:** [Source]

**Definition:** [Definition]

**Why it predicts fit:** [Logic]

---

## Tier 3 Signals — Monitor

*Weak signals on their own. Valuable in combination with Tier 1 or 2 signals.*

- [Signal name] (+5 pts) — [One-line description]
- [Signal name] (+5 pts) — [One-line description]
- [Signal name] (+5 pts) — [One-line description]

---

## Signal Combinations

*Certain combinations of signals are stronger predictors than any single signal.*

| Combination | Combined Score | What it means | Action |
|-------------|----------------|---------------|--------|
| [Signal A] + [Signal B] | +[X] bonus | [Interpretation] | [What to do] |
| [Signal A] + [Signal C] | +[X] bonus | [Interpretation] | [What to do] |

---

## Suppression Rules

*Signals that should pause or cancel outreach regardless of score.*

- Account is an existing customer → suppress all outreach
- Contact has unsubscribed in last 90 days → suppress email
- Active opportunity in CRM → suppress automated sequences
- [Custom rule] → [Action]

---

## Signal Performance Log

*Track which signals are actually generating pipeline. Update quarterly.*

| Signal | Outreach sent | Replies | Meetings | Pipeline | Notes |
|--------|--------------|---------|----------|----------|-------|
| [Signal A] | | | | | |
| [Signal B] | | | | | |
