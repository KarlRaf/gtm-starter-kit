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

**What gets marked `[inferred]` — and can be sharpened in the optional refinement pass:**
- ACV range and deal profile
- Anti-ICP — who explicitly wastes your time
- Top 3 signals you've observed or want to track
- Current week's priorities
- Competitive dynamics not visible publicly

Claude writes the repo first. No questions upfront. After you see the result, it offers a 3-minute refinement pass (5 questions) to replace inferred fields with your actual data. Skip it and the repo still works.

---

## Step 1: Research the Company

**If public data is limited** (bootstrapped company, stealth stage, minimal web presence): use what's available and mark more fields as `[inferred]`. A company with no Crunchbase entry → mark funding stage as `[inferred: bootstrapped or undisclosed]`. No G2 presence → skip competitor reviews, infer from their own positioning language. No case studies → infer personas from job postings and team page only. The repo will be less complete but still usable — the refinement pass in Step 5 exists exactly for this situation.

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

## Step 2: Write All Context Files From Public Data

Do not ask any questions yet. Write every context file immediately using what was found in the research. Make the best inference you can for fields that aren't publicly confirmed — mark those fields with `[inferred]` so the user knows what to verify.

The goal is a working repo the user can immediately run skills against. Speed of first value over completeness.

Do not write placeholder text — every field should have a real value or a clearly marked inference. "Series B SaaS companies" is not an ICP — infer the actual employee range, industry, and technographic signals from the customer base you found.

Write files in this order:

### 1. `context/profile.md`
Fill with: company overview from research, product description, deal profile inferred from customer base and pricing page (mark as `[inferred]`), reference customers from public case studies.

### 2. `context/icp-definition.md`
Fill with:
- Tier 1: the highest-fit segment you can infer from their positioning and customer base
- Tier 2: adjacent segments visible from their customer base
- Anti-ICP: infer from their positioning — who do they explicitly not target? Mark as `[inferred]` if not confirmed
- ICP evolution log: one entry dated today — "Initial definition from setup. Based on public positioning. Validate against first 90 days of scored accounts."

### 3. `context/signal-library.md`
Fill with:
- 3 Tier 1 signals: infer from hiring patterns, funding events, and job postings visible in research. Structure each with definition, detection method (Clay/LinkedIn/Crunchbase where applicable), point value, decay curve, and message hook. Mark as `[inferred]` — these will be replaced in the refinement pass if the user has better ones
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

## Step 3: Present the Summary and Offer Refinement

After writing all files, show a summary — then offer the refinement pass as optional.

```
Setup complete for [Company].

Here's what was written from public data:

- CLAUDE.md — full context layer
- context/profile.md — company overview, product, [N] reference customers
- context/icp-definition.md — [N] tiers inferred from customer base and positioning
- context/signal-library.md — [N] signals with detection methods
- context/positioning.md — value pillars, messaging matrix, competitive summary
- context/competitor-radar.md — [N] competitors with inferred win/loss patterns
- context/personas/ — [N] personas: [titles]

Fields marked [inferred] are Claude's best guess from public data.
They're good enough to run skills against — but may not reflect your actual win patterns.

---

You can start using the repo right now:

  Read skills/account-research/SKILL.md and research [example account from their ICP]

---

Want to sharpen what was inferred? Answer 5 quick questions and I'll
update every file with your actual data. Takes 3 minutes.

Type "refine" to continue, or skip and start running skills.
```

If the user types "refine" (or similar confirmation), proceed to Step 5. Otherwise, stop here — the repo is ready to use.

---

## Step 4: Refinement Pass (Optional)

Ask exactly these 5 questions in a single message. Do not split them across multiple prompts.

```
5 questions to sharpen your context:

1. ACV range — what's a typical deal worth?
   (e.g., "$20k–$80k" or "sub-$5k self-serve to $200k enterprise")

2. Anti-ICP — who explicitly wastes your time?
   Which company types, sizes, or situations should never enter your pipeline?

3. Top 3 signals — what tells you an account is ready to buy?
   Can be rough — I'll structure them. (e.g., "when they hire a VP of Sales,"
   "when they raise Series B," "when they're evaluating [competitor]")

4. This week — what's your current focus? Any active or planned campaigns?

5. Competitive nuance — anything not visible publicly?
   A competitor you're seeing in most deals, or an angle that's been working?
```

After receiving the answers, update every relevant file — replace `[inferred]` fields with confirmed data, add anti-ICP to the ICP definition, update signal library with the signals they named, update CLAUDE.md priorities. Then confirm what changed:

```
Updated with your answers:

- context/icp-definition.md — anti-ICP added, Tier 1 criteria sharpened
- context/signal-library.md — replaced inferred signals with your 3 named signals
- CLAUDE.md — priorities updated
- [any other files that changed]

All [inferred] flags removed from updated fields.
Remaining [inferred] fields: [list any that still need confirmation]
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
