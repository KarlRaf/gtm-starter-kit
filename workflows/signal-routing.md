# Workflow: Signal Routing

*How signals get detected, scored, and routed to the right action. The connective tissue between your data layer and your outreach.*

---

## Purpose

Signals mean nothing without routing. This workflow defines what happens when a signal fires — which account gets enriched, which rep gets notified, which sequence gets triggered, and which signals cancel or delay outreach.

---

## Signal Detection Methods

### Real-time (fire within hours)

Requires an integration or webhook. Set these up once.

| Signal | Detection method | Tool |
|--------|-----------------|------|
| New funding round | Crunchbase / PitchBook webhook | Clay / Zapier |
| Job posting published | Otta / LinkedIn / Ashby | Clay Claygent / Trigify |
| LinkedIn engagement | Comment or like on company content | Common Room / Trigify |
| Intent spike | Category surge | 6sense / G2 / Bombora |

### Daily (batch, runs overnight)

| Signal | Detection method | Tool |
|--------|-----------------|------|
| New hire in target role | LinkedIn Sales Nav + Clay | Clay |
| Tech stack change | BuiltWith delta | Clay |
| Social post mentioning [keyword] | LinkedIn / Twitter monitoring | Common Room |
| Website traffic spike | Clearbit Reveal | Clearbit |

### Weekly (manual or scheduled batch)

| Signal | Detection method | Tool |
|--------|-----------------|------|
| [Proprietary source] update | [Your method] | [Your tool] |
| CRM inactivity review | Accounts with no activity in 30+ days | CRM report |
| Signal score decay | Points reduced for aging signals | Scoring model run |

---

## Routing Logic

When a signal fires, this decision tree determines the action.

```
Signal fires on account X
│
├── Is X an existing customer?
│   └── Yes → Route to CSM for expansion signal. Stop.
│
├── Is X in active pipeline?
│   └── Yes → Add signal note to opportunity. Alert AE. Stop.
│
├── Is X suppressed (unsubscribed, DNC, recent contact)?
│   └── Yes → Log signal, do not trigger outreach. Stop.
│
├── Calculate signal score
│   │
│   ├── Score ≥ 80 (Tier 1)
│   │   └── Alert assigned AE immediately
│   │       Run Account Research skill within 24 hours
│   │       AE reviews and approves outreach within 48 hours
│   │
│   ├── Score 60–79 (Tier 2)
│   │   └── Trigger automated Tier 2 sequence
│   │       Alert SDR for manual review of touch 1
│   │
│   ├── Score 40–59 (Tier 3)
│   │   └── Add to Tier 3 automated sequence
│   │       No manual review required
│   │
│   └── Score < 40
│       └── Log signal, update score, no outreach
```

---

## Alert Templates

### Tier 1 Signal Alert (to AE)

```
Subject: Tier 1 signal — [Company] — [Signal name]

[Company] just hit Tier 1 threshold.

Signal: [Signal name]
Fired: [Date]
Account score: [X]/100

ICP fit: [Key fit indicators]
Recommended contact: [Name, Title]

Action needed: Review research brief and approve outreach by [Date + 48h].
Research: [Link to account research output]
```

---

### SDR Notification (Tier 2)

```
[Company] entered Tier 2 — [Signal name] fired [X] days ago.
Score: [X]/100
Sequence: [Sequence name] queued, touch 1 scheduled for [Date].
Review touch 1 before send: [Link]
```

---

## Suppression Rules

An account in any of the following states should NOT receive triggered outreach, regardless of signal score:

- Active customer (any plan)
- Active opportunity (any stage)
- Contact unsubscribed in last 90 days
- Account marked "do not contact" in CRM
- Contact on legal/compliance hold
- Outreach sent in last [X] days (set cooldown per tier)

**Cooldown periods by tier:**
- Tier 1: 45 days after last sequence completion
- Tier 2: 60 days
- Tier 3: 90 days

---

## Signal Decay

Signal scores reduce over time. Older signals are weaker signals.

| Signal age | Score multiplier |
|------------|-----------------|
| 0–30 days | 100% |
| 31–60 days | 75% |
| 61–90 days | 50% |
| 91–180 days | 25% |
| 180+ days | 0% (signal expires) |

Run a weekly batch to recalculate scores with decay applied. Accounts that drop below tier thresholds are downgraded automatically.
