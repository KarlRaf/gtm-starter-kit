# Workflow: Account Enrichment

*How we enrich accounts and contacts. Run this before any scoring or outreach to ensure data quality.*

---

## Purpose

Populate accounts and contacts with the firmographic, technographic, and organizational data needed to score ICP fit and personalize outreach. The goal is not complete data — it is the right data for our specific signals and scoring model.

---

## Enrichment Waterfall

Run enrichment sources in this order. Stop when you have sufficient coverage for a field. Don't pay for data you can get free.

### Tier 1: Free / Included Sources

1. **Company website + LinkedIn** — headcount, product, recent hires, tech stack (job postings)
2. **Crunchbase / PitchBook (free tier)** — funding history, investors
3. **BuiltWith / Wappalyzer** — tech stack fingerprint
4. **GitHub** — for developer-focused companies: activity, open source presence, team size

Use for: company snapshot, initial ICP screening, tech stack signals

---

### Tier 2: Clay Waterfall

For accounts that pass Tier 1 screening (ICP score ≥ 40), run through Clay in this order:

```
1. Clearbit Enrichment         → firmographics, estimated revenue, seniority data
2. People Data Labs (PDL)      → contact data, LinkedIn profiles, email
3. Apollo.io                   → email validation, additional contacts
4. Hunter.io                   → email verification fallback
5. LinkedIn (manual or Sales Nav) → contact verification, recent activity
```

**Clay table setup:**
- Input: domain
- Required output fields: company size, industry, funding stage, last funding date, tech stack, key contacts (name, title, email, LinkedIn URL)
- Quality gate: flag accounts where email confidence < 80%

---

### Tier 3: Custom / Proprietary Sources

*These are the signals that competitors don't have. Build these for your specific industry.*

Examples:
- Industry-specific regulatory databases (building permits, compliance filings)
- Job posting aggregators (track hiring patterns over time)
- App marketplaces (reviews, ratings, recent listings)
- Government datasets relevant to your ICP

Document your proprietary sources here:

| Source | What it provides | How to access | Refresh cadence |
|--------|-----------------|---------------|-----------------|
| [Source name] | [Signal type] | [API / Manual / CSV] | [Frequency] |

---

## Contact Enrichment

For each qualified account, identify and enrich 2–3 contacts matching your target personas.

**Contact priority order:**
1. [Primary persona title — e.g., VP of Sales Ops]
2. [Secondary persona title — e.g., Director of RevOps]
3. [Economic buyer title — e.g., CRO]

**For each contact, collect:**
- Full name
- Current title and company
- Work email (verified)
- LinkedIn URL
- Time in current role
- Recent LinkedIn activity (last post topic and date)

---

## Data Quality Standards

An account is "enrichment complete" when:

- [ ] Employee count: populated and accurate
- [ ] Funding stage: confirmed with last funding date
- [ ] Tech stack: at least 3 tools identified
- [ ] ICP score: calculated and recorded
- [ ] Primary contact: name, title, verified email, LinkedIn URL
- [ ] Secondary contact: at least one additional stakeholder identified

Accounts below this threshold stay in the enrichment queue — they don't move to active sequences.

---

## Enrichment Cadence

| Account tier | Re-enrich every |
|-------------|----------------|
| Tier 1 | 30 days |
| Tier 2 | 60 days |
| Tier 3 | 90 days |
| Tier 4 | On re-qualification event |

---

## Email Deliverability Infrastructure

Enrichment is only useful if your outbound emails land in the inbox. This is infrastructure, not a nice-to-have — handle it before you launch any sequence.

**Domain setup:**
- Send from a subdomain (e.g., `outbound.yourdomain.com` or a dedicated sending domain), never your primary domain
- SPF, DKIM, and DMARC must be configured on every sending domain — verify with [MXToolbox](https://mxtoolbox.com/) before sending
- Warm new domains for 4–6 weeks before sending at volume: start at 10–20 emails/day, increase 20–30% per week

**Sending limits (per mailbox):**
- Warmed mailbox: 40–50 emails/day max
- Multiple signals or tiers = multiple mailboxes — rotate across them
- Daily cap per sequence: enforce in your outbound tool, not manually

**Mailbox rotation:**
- Tier 1 outreach: dedicated mailboxes, manually monitored for replies
- Tier 2/3 sequences: shared mailbox pool, rotate sends evenly
- Immediately pull any mailbox with reply rate < 1% or bounce rate > 3%

**Bounce rate management:**
- Verify emails before enrolling contacts (Apollo, Hunter, or NeverBounce)
- Target: < 2% hard bounce rate per campaign
- Bounce rate > 5% = immediate pause and domain review

---

## CRM Sync

After enrichment, update the following CRM fields:

| CRM Field | Source | Notes |
|-----------|--------|-------|
| [Field name] | [Clay / Manual] | |
| [Field name] | [Clay / Manual] | |
| ICP Score | ICP Scoring skill | Calculated score, not vendor score |
| Account Tier | ICP Scoring skill | 1–4 based on score |
| Last Enriched | System | Auto-timestamp |
