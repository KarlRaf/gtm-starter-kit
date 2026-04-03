# CLAUDE.md — Relay

Relay is a workflow automation platform built for RevOps and GTM teams at growth-stage B2B SaaS companies. We replace the patchwork of Zaps and manual processes that break as teams scale from 50 to 500 people.

---

## Company Overview

**Company:** Relay
**Website:** relay.io
**What we do:** Relay automates the ops work that falls between your CRM, billing, and product — the handoffs, alerts, syncs, and routing logic that every RevOps team builds manually and rebuilds every time something changes.
**Stage:** Series B ($28M raised, 2023)
**Team size:** 85 people, 22 in GTM
**HQ:** San Francisco, CA

---

## GTM Motion

**Primary motion:** Sales-led with a product-qualified lead layer (free tier drives discovery)
**ACV range:** $24,000 – $180,000
**Sales cycle:** 32 days median (enterprise: 60–90 days)
**Primary channels:** Outbound (40%), inbound/PQL (35%), events (15%), partner (10%)
**Deal type:** AE-led evaluation with RevOps technical champion

---

## ICP Summary

Full definition: `context/icp-definition.md`

**Ideal customer in one sentence:** Series B–D B2B SaaS companies with a dedicated RevOps or Sales Ops function, 100–500 employees, running HubSpot or Salesforce, where the RevOps team spends more than 20% of their time on manual process work.

**Top 3 firmographic filters:**
1. Employee count: 100–500
2. Industry: B2B SaaS, FinTech, HR Tech
3. Funding: Series A–C, raised in last 24 months

**Anti-ICP:**
- SMBs under 50 employees — no dedicated ops function, no budget
- Enterprise (2,000+ employees) — buying process too complex for our current sales motion
- Companies using Workato as core infrastructure — migration cost too high
- Services/agencies — wrong business model

---

## Personas

Full profiles: `context/personas/`

| Persona | Title | What they care about | How to reach them |
|---------|-------|---------------------|-------------------|
| Champion | Head of RevOps / Sr. RevOps Manager | Reducing manual work, proving ops impact to leadership | Email + LinkedIn |
| Economic buyer | CRO / VP Sales | Pipeline velocity, rep efficiency, forecast accuracy | Events + email |
| Technical evaluator | Sales Ops Analyst / GTM Engineer | Integration reliability, API quality, migration effort | Email + Slack communities |

---

## Positioning

Full document: `context/positioning.md`

**Core value prop:** Relay reduces time-to-workflow from weeks to hours — RevOps teams build, test, and deploy process automations without waiting for engineering.

**Against each competitor:**
- vs. Workato: We win on speed-to-value and RevOps-specific UX. Workato requires IT involvement. We don't.
- vs. Zapier (Teams): We win on reliability at scale and native CRM depth. Zapier breaks above 10k records/day.
- vs. custom engineering: We win on iteration speed. Engineering changes take sprints. Relay changes take minutes.

**Tone and voice:** Practical, direct, zero fluff. We respect that our buyers are technical. We don't over-explain.

---

## Signal Library

Full library: `context/signal-library.md`

**Tier 1 signals (act immediately):**
1. "RevOps Manager" or "GTM Engineer" hired in last 30 days — new hire inheriting broken processes, high change appetite
2. Series B announced in last 60 days — team scaling fast, ops layer about to break
3. Job posting for 2+ RevOps/Sales Ops roles simultaneously — ops team overwhelmed, about to invest in tooling

**Tier 2 signals (add to sequence):**
1. Using HubSpot + Salesforce simultaneously — integration complexity = our core use case
2. LinkedIn post from RevOps leader about manual processes or CRM data quality
3. G2 review of Zapier Teams mentioning scaling issues

---

## Tech Stack

**CRM:** Salesforce (primary) + HubSpot (marketing)
**Enrichment:** Clay (primary), Clearbit (backup)
**Signal intelligence:** Trigify (job change alerts), Common Room (community signals)
**Outbound:** Outreach (enterprise), Smartlead (mid-market)
**Call intelligence:** Gong
**Intent data:** G2 Buyer Intent
**Data warehouse:** None currently

---

## Workflows

- `workflows/enrichment.md` — Clay waterfall for account + contact enrichment
- `workflows/signal-routing.md` — How signals route to Outreach or SDR queue
- `workflows/campaign-build.md` — Campaign launch process

---

## Team

| Name | Role | Owns |
|------|------|------|
| Sarah Chen | Head of GTM Engineering | Signal system, Clay, CRM architecture |
| Marcus Webb | SDR Lead | Outbound sequences, Outreach admin |
| Priya Nair | AE (Enterprise) | Tier 1 accounts, $60k+ ACV |
| David Kim | AE (Mid-Market) | Tier 2 accounts, $24k–$60k ACV |

---

## Current Priorities

- [ ] Build Series B signal campaign for Q2 (400 accounts identified, enrichment 60% complete)
- [ ] Rebuild Zapier competitive campaign — current reply rate is 1.2%, target is 4%
- [ ] Implement signal decay scoring — accounts from 2023 are inflating our active list

---

## How to Use This Repo

**Research an account:**
```
Read skills/account-research/SKILL.md and research [company.com]
```

**Score a list:**
```
Read skills/icp-scoring/SKILL.md and score the companies in [paste list].
Output a table sorted by score. Flag anything ≥ 60.
```

**Build a campaign:**
```
Read skills/signal-to-sequence/SKILL.md. Build a campaign for accounts
that triggered the "Series B in last 60 days" signal. Target the Head of RevOps
persona. Tier 2 intensity.
```
