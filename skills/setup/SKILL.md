# Skill: Setup

**Duration:** 15–30 minutes (including your review)
**Run once:** When you first clone this repo
**Output:** All context files pre-populated, CLAUDE.md ready to use

---

## Quick Start

```
Read skills/setup/SKILL.md and set up this repo for [your-domain.com]
```

That's it. Claude will research your company, pre-fill every context file with real data, ask you 5 targeted questions for what it couldn't find publicly, and write the full repo in one shot.

---

## What This Does

Instead of filling in 6 context files from blank templates, you provide a domain and Claude does the research. The output is a repo that's 70–80% complete from public information alone. You fill in the remaining 20–30% — the things only you know: your win patterns, your anti-ICP, your current priorities.

**What Claude can find publicly:**
- Company overview, product description, value proposition
- Funding stage and amount (Crunchbase)
- Headcount and growth (LinkedIn)
- Tech stack (BuiltWith, job postings)
- Key customers and use cases (website, case studies, G2 reviews)
- Competitors (G2, website, positioning language)
- Buyer personas (job postings, team page, customer titles)
- Existing signal indicators (hiring patterns, recent news)

**What Claude will ask you (5 questions max):**
1. ACV range and deal profile
2. Your #1 anti-ICP — who explicitly wastes your time
3. Top 3 signals you've observed or want to track
4. Current week's priorities
5. Any competitive dynamics not visible publicly

---

## Step 1: Research the Company

Given the domain, Claude researches:

### Company snapshot
- Visit the domain. Extract: what they do, who they sell to, what problem they solve, how they position themselves. Look for customer logos, case studies, and the language they use to describe their own ICP.
- Check Crunchbase (crunchbase.com/organization/[company]): funding history, total raised, last round, lead investors, date.
- Check LinkedIn (linkedin.com/company/[company]): headcount, growth rate, recent hires, team structure.

### Product and positioning
- Read their homepage, pricing page, and "customers" or "case studies" page.
- Extract: primary value proposition, who it's for, what they replace or displace, proof points they highlight publicly.
- Note any "what not to say" signals — language on their site that suggests what they want to avoid being confused with.

### Competitors
- Check G2 (g2.com) for their category. Note the top 3–5 alternatives listed.
- Look for "vs." pages on their site or competitors' sites.
- Note any direct competitor mentions in their positioning.

### Buyer personas
- Check their team page and job postings. Who do they hire for? What titles appear in customer quotes and case studies?
- Look for the titles of people writing reviews on G2.
- Identify 2–3 likely buyer personas based on what you find.

### Tech stack and signals
- Check BuiltWith (builtwith.com/[domain]) for their own tech stack — useful context.
- Look at recent job postings for signals about who they're targeting (required tools, experience with specific platforms).
- Note any recent press, funding announcements, product launches.

---

## Step 2: Ask 5 Questions

After completing the research, present what you found and ask exactly these 5 questions. Do not ask more.

```
Here's what I found about [Company]:

[2–3 sentence summary of what they do and who they sell to]

Funding: [round, amount, date]
Headcount: [X, growth direction]
Likely ICP: [what you inferred]
Top competitors: [list]
Likely personas: [list]

Before I write the context files, I need 5 things from you:

1. ACV range — what's a typical deal worth? (e.g., "$20k–$80k" or "sub-$5k self-serve to $200k enterprise")

2. Anti-ICP — who explicitly wastes your time? Which company types, sizes, or situations should never enter your pipeline?

3. Top 3 signals — what events or conditions tell you an account is ready to buy? These can be rough — I'll structure them properly. (e.g., "when they hire a VP of Sales," "when they raise Series B," "when they're using [competitor]")

4. This week's priorities — what's the #1 thing you're focused on right now? What campaigns are active or planned?

5. Competitive nuance — anything about your competitive situation that isn't visible publicly? A competitor you're seeing in most deals, or a positioning angle that's been working?
```

Wait for the answers before writing any files.

---

## Step 3: Write All Context Files

Using the research and the answers, write every context file simultaneously. Do not write placeholder text — every field should have real content or a specific, answerable question in brackets.

Write files in this order:

### 1. `context/profile.md`
Fill with: company overview from research, product description, deal profile using the ACV answer, reference customers from public case studies.

### 2. `context/icp-definition.md`
Fill with:
- Tier 1: the highest-fit segment you can infer from their positioning + what they told you
- Tier 2: adjacent segments visible from their customer base
- Anti-ICP: exactly what they gave you in question 2
- ICP evolution log: one entry dated today — "Initial definition from setup. Based on public positioning and founder input. Validate against first 90 days of scored accounts."

### 3. `context/signal-library.md`
Fill with:
- 3 Tier 1 signals: use what they gave you in question 3, structured with definition, detection method (Clay/LinkedIn/Crunchbase where applicable), point value (calibrate based on signal strength), decay curve, and message hook
- 2 Tier 2 signals: infer from what you know about the company type — hiring signals, tech stack signals, or intent signals that typically apply to their category
- Signal combinations: at least 1 combination using the signals above
- Performance log: empty table with column headers, ready to fill

### 4. `context/positioning.md`
Fill with:
- Core positioning statement: extracted from their homepage and pricing page
- Value pillars: 2–3 based on what they emphasize publicly (use their own language as a starting point, note where proof points are needed)
- Competitive positioning: use the research + question 5
- What not to say: infer from their positioning — what category do they want to avoid being lumped into?
- Reference customers: from public case studies

### 5. `context/competitor-radar.md`
Fill with:
- Top 3 competitors from research
- For each: what you infer about when they win vs. lose (based on G2 reviews, positioning language, question 5 answer)
- Note explicitly: "Win/loss patterns below are inferred from public data. Update after first 3 competitive deals."

### 6. `context/personas/`
Create one file per persona identified in research (2–3 personas). For each:
- Title, seniority, decision role
- What they measure themselves on (infer from job postings and G2 reviews)
- What gets their attention (infer from the content they engage with publicly)
- Outreach hooks: one hook per signal from the signal library

### 7. `CLAUDE.md`
Fill with all of the above — ICP summary, top 3 signals, persona table, positioning summary, current week's priorities from question 4.

---

## Step 4: Present the Summary

After writing all files, show a summary:

```
Setup complete. Here's what was written:

FILLED FROM RESEARCH:
- context/profile.md — company overview, product, reference customers
- context/positioning.md — value pillars, competitive summary (from public data)
- context/competitor-radar.md — [N] competitors with inferred win/loss patterns
- context/personas/ — [N] personas: [titles]
- CLAUDE.md — full context layer

FILLED FROM YOUR ANSWERS:
- context/icp-definition.md — ICP tiers, anti-ICP, evolution log
- context/signal-library.md — [N] signals with detection methods

NEEDS YOUR REVIEW (flagged in files with [VERIFY]):
- [List any specific fields that need human confirmation]

NEXT STEP:
Run this to stress-test your ICP definition against your current pipeline:

  Read skills/icp-scoring/SKILL.md and score [paste 10 company names]

Then run account research on your top account:

  Read skills/account-research/SKILL.md and research [top-account.com]
```

---

## Quality Standard

Before presenting the summary, verify:

- [ ] No file contains lorem ipsum, "TBD", or generic placeholder text
- [ ] Every signal has a detection method (not just a description)
- [ ] Every persona has at least one outreach hook
- [ ] CLAUDE.md is scannable in under 2 minutes
- [ ] The ICP definition is specific enough that two people would build the same list from it independently
- [ ] Anti-ICP has at least 3 explicit exclusions

If any of these fail, fix the file before presenting the summary.
