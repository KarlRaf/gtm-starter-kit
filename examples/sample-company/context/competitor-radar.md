# Competitor Radar — Relay

Last updated: 2024-03-01

---

## Competitive Landscape Summary

| Competitor | Market position | Our win rate | Best angle against them |
|------------|----------------|-------------|------------------------|
| Zapier Teams | Default choice, brand recognition | 68% when we get to eval | Scale and reliability |
| Workato | Enterprise standard, IT-led | 22% — we usually don't compete here | Avoid unless they're re-evaluating |
| Tray.io | Mid-market, technical buyers | 55% | RevOps-specific UX |
| Custom engineering | Default at Series C+ | 41% | Speed of iteration |

---

## Zapier Teams

**One-line summary:** The default first choice for any team starting to automate. Strong brand, huge template library, low friction to start.

**Market position:** Dominant at SMB, losing ground at growth-stage as teams hit scale limits.

**Their strengths:**
- Brand recognition — every RevOps person has used it
- Template library (5,000+ pre-built Zaps)
- Low barrier to start: first workflow in 10 minutes

**Their weaknesses:**
- Reliability at scale: fails silently above ~10k records/day
- No native CRM depth — Salesforce/HubSpot connectors are surface-level
- No human-in-the-loop steps — automation is binary
- Error visibility is poor: teams often don't know a Zap broke until a deal is already wrong

**Why customers switch to us:**
- "We kept finding broken Zaps days later" (reliability)
- "We needed a sales ops person to review before it updated the CRM" (human-in-the-loop)
- "Our Clay and Salesforce tables got out of sync and nobody knew why" (CRM depth)

**How to handle the "we already use Zapier" objection:**
> "Most of our customers started on Zapier — it's the right tool when you're getting started. The pattern we see is that around 100–150 employees, teams have 30–50 Zaps running, no one knows which ones are still active, and they've had at least one data incident they had to clean up manually. That's usually when they call us."

**Signal that an account uses Zapier:**
- BuiltWith tech stack: Zapier detected
- G2 review of Zapier Teams mentioning scale, reliability, or CRM sync issues

**Competitive message for first touch (don't name Zapier directly):**
> "Most RevOps teams at your stage are running 30–50 automation workflows that no one fully trusts anymore. The issue isn't the workflows — it's that the tooling wasn't built for the volume or the CRM depth you need now."

---

## Workato

**One-line summary:** Enterprise-grade integration platform. IT-owned, engineering-deployed, not a RevOps tool.

**Market position:** The CIO's choice at 1,000+ employee companies. Serious overkill for our ICP.

**Their strengths:**
- Depth and reliability at enterprise scale
- IT and security compliance
- Pre-built connectors for everything

**Their weaknesses:**
- Requires IT involvement to deploy and maintain
- 3–6 month implementation timeline
- Priced for enterprise ($50k+ per year)
- Not built for RevOps self-service

**When to compete:**
Only compete when a growth-stage company is being pushed toward Workato by an IT stakeholder. The conversation is: "Workato is the right tool when IT owns the process. If RevOps owns it, Relay deploys 10x faster and your team can maintain it without filing a ticket."

**When not to compete:**
If they already have Workato deployed with IT ownership, do not pursue. Migration cost and internal politics make this a 12-month sales cycle at best.

**Win rate:** 22% overall — avoid unless they're actively re-evaluating.

---

## Tray.io

**One-line summary:** Mid-market automation platform, technically sophisticated, weaker RevOps-specific UX.

**Their strengths:**
- Reliable at scale
- Flexible data transformation
- Reasonable pricing for mid-market

**Their weaknesses:**
- UX is built for technical users — a RevOps analyst can't self-serve
- Less CRM-specific than Relay
- Smaller customer community and template library

**Why customers switch to us:**
- RevOps teams who bought Tray for flexibility and then discovered their team couldn't maintain it without their one technical ops person.

**Win rate:** 55% when it's a true head-to-head evaluation.

---

## Custom Engineering

**This isn't a vendor — it's the default alternative at Series C+ when engineering bandwidth exists.**

**The pattern:** Growth-stage company raises Series C, adds engineering headcount, someone says "let's just build this ourselves."

**Why they eventually come back:**
- Custom-built automation requires ongoing maintenance that engineering deprioritizes
- Engineers leave and no one knows how it works
- Time to new workflow is weeks, not hours
- RevOps can't modify workflows without engineering tickets

**The angle:**
> "Engineering can build this — the question is whether you want one of your engineers spending a sprint on a routing workflow every time your sales process changes, or whether RevOps can own it and iterate in minutes."

**Win condition:** When the CRO or VP Sales has been waiting 3+ weeks for an engineering change to a workflow they could build in Relay in an afternoon.

---

## Win/Loss Patterns

**Why we win:**
1. RevOps champion has been burned by Zapier reliability at least once
2. Human-in-the-loop requirement (legal, finance, exec approvals in deal flow)
3. The technical evaluator has seen the API and Salesforce connector depth in a POC

**Why we lose:**
1. Price is the primary criterion and they're comparing to Zapier Teams pricing
2. IT owns the evaluation and Workato is the IT default
3. We're evaluated against a custom solution that an engineer is actively building
4. Champion leaves the company mid-deal
