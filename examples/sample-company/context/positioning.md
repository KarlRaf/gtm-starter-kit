# Positioning — Relay

*Source of truth for how we talk about what we do, who we beat, and who we lose to. Reference before writing any outbound copy, building a battlecard, or preparing for a competitive evaluation.*

Last updated: 2024-03-01

---

## Core Positioning Statement

Relay is the workflow automation platform for RevOps teams at growth-stage B2B SaaS companies. We replace the patchwork of Zaps and manual handoffs that break as teams scale from 50 to 500 people.

**The mechanism:** Relay is built for the specific workflows that live between CRM, billing, and product — deal desk approvals, lead routing, HubSpot-to-Salesforce sync, renewal alerts. Not generic automation. RevOps automation. Every template, every integration, every error alert is designed for the ops team managing a revenue stack, not a developer building general-purpose workflows.

---

## Value Pillars

### Pillar 1: Speed to Workflow

**Leads for:** Head of RevOps / Sr. RevOps Manager (champion)

RevOps teams at growth-stage companies don't have weeks to wait for engineering. Relay workflows are built, tested, and deployed by the ops team directly — no code, no Jira ticket, no sprint cycle. Teams at our ACV range typically go from identified problem to live workflow in under a week.

**Proof points:**
- Watershed's deal desk approval workflow: from a 4-day average to same-day, built and deployed by their RevOps team in 3 days
- Ashby reduced ops-to-engineering handoff tickets by 70% in 60 days

---

### Pillar 2: Reliability at Scale

**Leads for:** Head of RevOps (champion), CRO / VP Sales (economic buyer)

Zapier breaks above ~10,000 tasks/day. Multi-step workflows start failing silently. Relay has full audit logging and error alerting built into every workflow — when something breaks, you know immediately, you see the full trace, and you can replay failed runs. No silent failures. No "the sync was off for three days and nobody noticed."

**Proof points:**
- 99.7% workflow execution reliability across all customers in 2023
- Drata team estimated 6 hours/week saved on manual data reconciliation after migration

---

### Pillar 3: RevOps-Native Integrations

**Leads for:** Sales Ops Analyst / GTM Engineer (technical evaluator)

Relay connects HubSpot, Salesforce, Stripe, and the common RevOps stack with native two-way sync — not a web hook and a prayer. Integration depth means ops teams can build the workflows they actually need: conditional routing based on deal value, multi-approver sequences for enterprise contracts, product-qualified lead scoring that writes back to CRM.

**Proof points:**
- Native HubSpot ↔ Salesforce two-way sync with field-level conflict resolution
- Stripe integration for usage-based billing alert workflows (triggers at >80% of plan limit)

---

## Messaging Matrix

| Persona | Lead with | Avoid |
|---------|-----------|-------|
| Head of RevOps | Speed to workflow, no engineering dependency, audit logging | Feature comparisons, generic "automation" language |
| CRO / VP Sales | Pipeline velocity, forecast accuracy, rep efficiency | Technical details, integration specifics |
| Sales Ops Analyst / GTM Engineer | Integration reliability, API quality, HubSpot/Salesforce native depth | Oversimplified "no-code" language — they know the tools |

---

## Competitive Positioning

Full battlecards: `context/competitor-radar.md`

| Competitor | We win when | We lose when |
|------------|-------------|-------------|
| Zapier Teams | Account is scaling past 10k tasks/day or needs audit logging | They only need simple 2-step automation and nothing else |
| Workato | RevOps team wants to own workflows without IT involvement | IT owns the integration stack and Workato is already entrenched |
| Tray.io | They want RevOps-specific templates and faster time to value | They need developer-first flexibility for complex custom logic |
| Custom engineering | They need iteration speed and ops team ownership | Eng team already built something working and migration cost is high |

---

## What Not to Say

**Don't position as "the Zapier for enterprise."** Zapier is a reference point but not our identity. This frame makes us sound like a feature upgrade, not a category. Say: "built specifically for RevOps workflows" — it's a different use case, not a bigger version.

**Don't lead outbound with "workflow automation."** Too generic. Every vendor says this. Lead with the specific problem: "HubSpot-to-Salesforce sync," "deal desk approval," "lead routing logic." The specific pain is what gets responses.

**Don't promise unlimited scalability.** Our sweet spot is 100–500 employee B2B SaaS. Don't overpromise on the enterprise use cases we haven't fully solved — migration complexity and IT procurement at 2,000+ employees is a different motion.

---

## Reference Customers by Use Case

| Customer | Use case | Can reference? |
|----------|----------|---------------|
| Watershed | Deal desk approval + HubSpot/Salesforce sync | Yes — public case study |
| Ashby | Lead routing + ops-to-eng ticket reduction | Yes — can reference in outbound |
| Drata | Manual reconciliation reduction | Anonymize as "a compliance automation company" |
