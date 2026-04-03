# Signal Library

*Signals are observable events that predict pipeline conversion 30–90 days in advance. This library is the source of truth for all signal-based outreach. Every campaign in this repo traces back to at least one signal here.*

Last updated: [YYYY-MM-DD]

*See example: `examples/sample-company/context/signal-library.md`*

---

## Signal Scoring Model

Accounts accumulate points as signals fire. Thresholds determine outreach intensity.

| Score | Tier | Action |
|-------|------|--------|
| 80–100 | Hot | AE alert within 2 hours. Research brief within 24 hours. Outreach within 48 hours. |
| 60–79 | Warm | SDR triggers Tier 2 sequence within 48 hours. |
| 40–59 | Cool | Add to Tier 3 automated sequence. |
| 0–39 | Cold | Log and monitor. No outreach. |

---

## Tier 1 Signals — Act Immediately

*High predictive power. When a Tier 1 signal fires: alert within 2 hours, research within 24 hours, outreach within 48 hours.*

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

## Signal Decay

Signal scores reduce over time. A signal from 150 days ago is not the same as one from 10 days ago — score them differently.

| Signal age | Score multiplier |
|------------|-----------------|
| 0–30 days | 100% |
| 31–60 days | 75% |
| 61–90 days | 50% |
| 91–180 days | 25% |
| 180+ days | 0% (signal expires) |

Run a weekly batch to recalculate scores with decay applied. Accounts that drop below tier thresholds are downgraded automatically. Without decay, your active list quietly fills with accounts that were relevant six months ago and aren't anymore.

---

## Signal Performance Log

*Track which signals are actually generating pipeline. Update after every campaign.*

| Signal | Outreach sent | Replies | Meetings | Pipeline | Notes |
|--------|--------------|---------|----------|----------|-------|
| [Signal A] | | | | | |
| [Signal B] | | | | | |
