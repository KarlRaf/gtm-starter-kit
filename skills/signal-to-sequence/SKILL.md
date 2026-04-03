# Skill: Signal to Sequence

**Duration:** 2–4 hours per campaign
**Output:** `outputs/campaigns/[date]-[campaign-name]/`

---

## Quick Start

```
Read skills/signal-to-sequence/SKILL.md.
Build a Tier 2 campaign for accounts triggering the [signal name] signal.
Target the [persona title] persona.
```

For a complete example of what this produces, see:
`examples/sample-company/outputs/campaigns/2024-03-01-series-b-revops-tier2/`

---

## Purpose

Turn a signal — or a set of accounts sharing a signal — into a live outreach campaign. This skill connects the signal library to actual sequences. It answers the question: "We know who to target and why. Now what do we actually say?"

The output of this skill is not a rough draft. It is a sequence ready to load into your outbound tool.

---

## When to Run This Skill

- A new signal fires across multiple accounts simultaneously (e.g., batch of Series B announcements)
- You're launching a new campaign segment
- An existing campaign is underperforming and needs a full rebuild
- A new ICP tier needs to be activated for the first time

---

## Inputs

- Target signal(s) from `context/signal-library.md`
- ICP tier for this campaign from `context/icp-definition.md`
- Persona(s) being targeted from `context/personas/`
- Competitive context from `context/competitor-radar.md` (if relevant)
- Company profile from `context/profile.md`

---

## Step 1: Define the Trigger Logic (20 min)

Before writing a word, be precise about what fires this campaign.

**Single-signal trigger:** One signal alone justifies outreach.
- Which signal? [From signal library]
- Minimum score threshold to activate?
- Recency window: signal must have fired in last [X] days?

**Multi-signal trigger:** Two or more signals in combination.
- Signal A + Signal B = activate
- What does the combination tell you that neither signal alone tells you?

**Suppression conditions:** Accounts that match the signal but should NOT receive this campaign.
- Active opportunity in CRM
- Existing customer
- Contacted in last [X] days
- [Any other suppression rules from signal library]

Document the trigger logic in plain language before moving to Step 2. Ambiguous triggers produce wasted outreach.

---

## Step 2: Segment the Target List (20 min)

Pull all accounts matching the trigger logic. Segment by:

- ICP tier (Tier 1 vs. Tier 2 vs. Tier 3 gets different sequence intensity)
- Persona (different message for each role)
- Account status (cold prospect vs. previously contacted vs. dark opportunity)

Output: a clean list per segment with contact information and signal data attached.

---

## Step 3: Design the Sequence (45 min)

Build the sequence structure before writing copy. Define:

| Touch | Day | Channel | Goal | Personalization level |
|-------|-----|---------|------|-----------------------|
| 1 | 0 | Email | First impression + signal hook | High — signal-specific |
| 2 | 3 | LinkedIn | Connect + brief context | Medium |
| 3 | 6 | Email | Value prop + proof | Medium |
| 4 | 10 | Email | Different angle or asset | Low |
| 5 | 14 | Phone/VM | Direct ask | Medium |
| 6 | 21 | Email | Break-up + pivot | Low |

**Tier guidance:**
- Tier 1: 6–8 touches, all channels, manual personalization on touches 1–3
- Tier 2: 5–7 touches, email + LinkedIn, semi-automated
- Tier 3: 4–5 touches, email-first, templated with signal variable

---

## Step 4: Write the Copy (60–90 min)

Write each touch. Apply the PVP standard to Tier 1 and Tier 2 email 1.

### The PVP Standard (Permissionless Value Prop)

A message passes PVP if the prospect would find it valuable even if they never buy from you. It delivers market intelligence, not a sales pitch.

**Test:** Remove your CTA. If the message still has value, it passes. If it's pointless without the CTA, it's a pitch — rewrite it.

**Four questions every Tier 1 first touch must answer yes to:**
1. Does this contain an insight the prospect doesn't already have?
2. Would they forward this to a colleague?
3. Would they find this useful even if they never buy?
4. Is this market intelligence, not just personalization?

---

### Touch 1 — Email (Signal Hook)

**Subject line options (write 3, A/B test 2):**
- [Option A — curiosity-based]
- [Option B — direct/insight-based]
- [Option C — question-based]

**Body structure:**
```
[Signal hook — one specific, datable observation]

[Insight — what that signal means in context, something they may not know]

[Connection — how that maps to what you do, in one sentence]

[CTA — one ask, frictionless]

[Signature]
```

**Example:**
```
Subject: [Company]'s RevOps hire

[First name],

[Company] just posted for a Senior RevOps Manager — third ops hire in 90 days.
Teams at that growth rate typically hit the same wall: the tooling that worked at
50 people breaks at 150.

We've helped [anonymized: a developer platform at similar scale] cut their
pipeline-to-close variance in half by rebuilding the ops layer before it became
a bottleneck.

Worth 20 minutes to compare notes?

[Name]
```

---

### Touch 2 — LinkedIn Connection Request

```
[First name] — sent you an email [X] days ago about [one-sentence context]. Would be good to connect here too.
```

The connection note should be 1–2 sentences max. Reference something specific: the email you already sent, a recent post they published, or their new role. "Following your work" and "building something adjacent" read as spray-and-pray. LinkedIn accepts correlate with personalization quality — use the signal context you already have.

---

### Touch 3 — Email (Value Prop + Proof)

Shift the angle. Don't repeat touch 1. Lead with a different dimension of value or a proof point.

```
[First name],

Following up from last week. Wanted to share something relevant.

[Specific outcome or data point from a reference customer in a similar situation]

[One sentence connecting that to their current situation]

Happy to walk through how we approach it — [CTA].

[Name]
```

---

### Touch 4 — Email (Asset or Different Angle)

Offer something concrete: a framework, a benchmark, a piece of content, a question worth thinking about.

---

### Touch 5 — Phone / Voicemail

```
Talk track:
"[Name], [Your name] from [Company]. Reached out a couple times over email — not trying to be persistent,
just think the timing might be right given [specific signal/context]. If I'm wrong, happy to hear it.
Call me back at [number] or reply to my email — either works."
```

---

### Touch 6 — Break-up Email

```
Subject: Closing the loop

[First name],

I've reached out a few times — not going to keep at it.

If the timing isn't right or this isn't relevant, totally understood.

If something changes — [specific trigger that would make this relevant again] — feel free to reach out.

[Name]
```

---

## Step 5: Measurement Plan (15 min)

Define success before launch. Set targets by tier:

| Metric | Tier 1 target | Tier 2 target | Tier 3 target |
|--------|--------------|--------------|--------------|
| Reply rate | ≥ 8% | ≥ 4% | ≥ 2% |
| Meeting rate | ≥ 5% | ≥ 2% | ≥ 1% |
| Pipeline per 100 accounts | $[X] | $[Y] | $[Z] |

**What to track:**
- Reply rate by touch number (where are people responding?)
- Meeting rate by signal type (which signals convert best?)
- Signal-triggered vs. generic performance lift

**Review cadence:** First review at 2 weeks (enough volume to see patterns). Full review at 6 weeks.

---

## Output Structure

```
outputs/campaigns/[date]-[campaign-name]/
├── brief.md          ← Trigger logic, segments, objectives
├── sequences/
│   ├── tier1.md      ← Full sequence copy, Tier 1
│   ├── tier2.md      ← Full sequence copy, Tier 2
│   └── tier3.md      ← Full sequence copy, Tier 3
├── metrics.md        ← Targets and measurement plan
└── results.md        ← Updated as campaign runs
```
