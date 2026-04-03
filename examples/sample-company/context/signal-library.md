# Signal Library — Relay

Last updated: 2024-03-01

---

## Signal Scoring Model

| Score | Tier | Action |
|-------|------|--------|
| 80–100 | Hot | AE alert within 2 hours. Research brief within 24 hours. Outreach within 48 hours. |
| 60–79 | Warm | SDR triggers Tier 2 sequence within 48 hours. |
| 40–59 | Cool | Add to Tier 3 automated sequence. |
| 0–39 | Cold | Log and monitor. No outreach. |

---

## Tier 1 Signals — Act Immediately

### Signal: New RevOps Hire (last 30 days)
**Category:** Organizational
**Points:** 35
**Source:** LinkedIn (via Trigify or Clay)
**Refresh cadence:** Daily

**Definition:** A company has posted a new "RevOps Manager," "Head of Revenue Operations," "Sales Ops Manager," or "GTM Engineer" who started in the last 30 days, as indicated by LinkedIn profile update or job posting closure.

**Why it predicts fit:** New RevOps hires inherit broken processes. They have mandate and motivation to fix tooling in their first 90 days. Contact within 14 days of the hire date is our highest-conversion window — 3–4x the meeting rate of cold outreach to tenured holders of the same role.

**Detection method:**
```
Clay Claygent prompt:
"Go to LinkedIn and search for people who currently work at [company domain]
with 'RevOps', 'Revenue Operations', 'Sales Ops', or 'GTM Engineer' in their title.
For each person found, return their name, title, LinkedIn URL, and estimated start date.
Flag anyone whose start date appears to be within the last 30 days."

Clay column setup:
- Input: company LinkedIn URL or domain
- Run Claygent on accounts that passed ICP screening
- Output: name, title, start_date, linkedin_url, is_recent_hire (true/false)
- Filter downstream: is_recent_hire = true AND start_date > today - 30 days
- Verify: spot-check LinkedIn manually for top accounts — Claygent can misread tenure
```

**Message hook:** "Congrats on the new RevOps hire — first 90 days in that seat is usually when people decide what to rebuild."

---

### Signal: Series B Announced (last 60 days)
**Category:** Firmographic
**Points:** 30
**Source:** Crunchbase (webhook via Clay)
**Refresh cadence:** Real-time

**Definition:** Company has announced a Series B funding round in the last 60 days, with raise amount between $10M and $150M. (Rounds outside this range — micro-B below $10M or mega-rounds above $150M — are either pre-product-market-fit or too far into scale to be our best entry point.)

**Why it predicts fit:** Series B is the inflection point where GTM teams scale from scrappy to systematic. Headcount grows 50–100% in 12 months. Ops processes that worked at 40 people break at 120. Budget exists and urgency is real.

**Detection method:**
```
Crunchbase webhook → Clay → filter:
  funding_type = "Series B"
  announced_date > today - 60 days
  raised_amount >= 10000000 AND <= 150000000
```

**Message hook:** "Series B is the point where RevOps either scales or becomes the bottleneck — usually within 6 months of the announcement."

---

### Signal: 2+ RevOps Job Postings Active (same time)
**Category:** Organizational
**Points:** 30
**Source:** LinkedIn / Greenhouse / Lever (via Clay)
**Refresh cadence:** Weekly

**Definition:** Company has 2 or more open roles with "RevOps," "Sales Ops," or "Revenue Operations" in the title posted simultaneously.

**Why it predicts fit:** Multiple open ops roles = existing team is overwhelmed. They're trying to hire their way out of a process problem. High urgency, high budget approval likelihood.

**Detection method:**
```
Clay column: Job postings search
Query: "(RevOps OR 'Sales Ops' OR 'Revenue Operations') site:greenhouse.io OR site:lever.co"
Filter: 2+ results for same company domain
```

**Message hook:** "Two open RevOps roles usually means the team is underwater — curious if tooling is part of the fix or just headcount."

---

## Tier 2 Signals — Add to Active Sequences

### Signal: HubSpot + Salesforce Dual Stack
**Category:** Technographic
**Points:** 20
**Source:** BuiltWith / Clay technographics
**Refresh cadence:** Weekly

**Definition:** Company is actively using both HubSpot and Salesforce based on tech stack fingerprint.

**Why it predicts fit:** HubSpot + Salesforce is our highest-fit technographic. Bi-directional sync between the two is a constant ops headache and a core Relay use case. Close rate on this segment: 62%.

---

### Signal: LinkedIn Post About Manual Processes
**Category:** Behavioral / Intent
**Points:** 20
**Source:** Common Room / Trigify
**Refresh cadence:** Daily

**Definition:** A VP or Director-level person at a target account has posted on LinkedIn about CRM data quality, manual workflows, RevOps tooling, or ops scaling challenges in the last 14 days.

**Why it predicts fit:** Self-identified pain in a public forum. The timing creates a natural, non-awkward reason to reach out.

---

### Signal: G2 Review of Zapier Teams Mentioning Scale Issues
**Category:** Intent
**Points:** 15
**Source:** G2 Buyer Intent
**Refresh cadence:** Weekly

**Note:** This signal requires a paid G2 Buyer Intent subscription. Without it, you have no visibility into which company a reviewer works for — only the review text is public. Confirm your G2 package includes buyer intent data before building detection logic around this signal.

**Definition:** Someone at a target account has left a G2 review of Zapier Teams, Make, or Workato in the last 30 days that mentions limitations, scale issues, or switching intent.

---

## Tier 3 Signals — Monitor

- Recently followed Relay on LinkedIn (+5 pts)
- Visited relay.io pricing page (+5 pts)
- Downloaded a Relay piece of content (+5 pts)
- Connected with a Relay team member on LinkedIn (+5 pts)

---

## Signal Combinations

| Combination | Bonus | What it means | Action |
|-------------|-------|---------------|--------|
| New RevOps Hire + Series B | +15 | New hire at funded company — maximum urgency window | AE-owned, 24-hour outreach |
| Series B + Dual Stack | +10 | Scaling with existing complexity | Tier 1 treatment |
| 2+ Job Postings + G2 Intent | +10 | Active evaluation with urgency | Escalate to Tier 1 immediately |

---

## Suppression Rules

- Existing customer → suppress all outreach
- Active opportunity in Salesforce → suppress automated sequences, AE owns
- Unsubscribed in last 90 days → suppress email
- Contacted in last 45 days (Tier 1) / 60 days (Tier 2) / 90 days (Tier 3) → cooldown

---

## Signal Performance Log

| Signal | Sends (90d) | Reply rate | Meeting rate | Notes |
|--------|------------|------------|--------------|-------|
| New RevOps Hire | 84 | 11.9% | 7.1% | Best performing signal. Contact within 14 days of hire is key. |
| Series B | 62 | 8.1% | 4.8% | Strong. Decay curve is steep — contact within 30 days. |
| 2+ Job Postings | 41 | 9.7% | 5.6% | Small sample but strong. |
| Dual Stack (alone) | 210 | 3.2% | 1.4% | Weak alone. Use as amplifier, not primary trigger. |
