# Workflow: Campaign Build

*How we go from a target segment to a live campaign. The end-to-end process — from list to launch.*

---

## Purpose

A campaign is not a sequence. A sequence is copy and timing. A campaign is a defined target segment, a clear trigger, a measurement plan, and a sequence — in that order. This workflow ensures we never write copy before the strategy is clear.

---

## Pre-Campaign Checklist

Before starting any new campaign:

- [ ] Is there a clear signal or trigger defining this audience?
- [ ] Is the ICP tier and persona defined?
- [ ] Is the estimated audience size ≥ 50 accounts? (Below this, the data won't be statistically meaningful)
- [ ] Is the value prop differentiated from campaigns already running?
- [ ] Is there a success metric and a timeline for evaluation?

If any of these are "no," resolve them before proceeding.

---

## Phase 1: Audience Definition

**Time:** 30 minutes

Define the exact accounts this campaign targets. Be specific enough that two people would build the same list independently.

```markdown
## Campaign Target Definition

Signal(s): [From signal library]
ICP Tier: [1 / 2 / 3]
Persona: [Target title(s)]
Account status: [Cold / Previously contacted / Dark opportunity]
Additional filters:
  - Industry: [List]
  - Size: [Range]
  - Geography: [If applicable]
  - Technographic: [If applicable]
  - Recency: Signal must have fired in last [X] days

Estimated list size: [X accounts]
Estimated contacts: [Y people]
```

---

## Phase 2: Enrichment

Run the enrichment workflow (`workflows/enrichment.md`) on the target list.

Quality gate: do not proceed until enrichment is ≥ 80% complete on required fields.

---

## Phase 3: Message Strategy

**Time:** 45 minutes

Before writing copy, answer these questions in writing:

1. **What is the hook?** The specific, datable, observable trigger that justifies this outreach right now. Not a general pain point — the specific event.

2. **What is the insight?** What does that signal tell us that the prospect may not have fully considered? What can we add to their thinking?

3. **What is the ask?** One action. Not "let me know if you're interested." A specific, low-friction next step.

4. **What proof point is most relevant?** One customer outcome or data point that is most relevant to this specific segment.

5. **What does the competitor angle look like?** If there's competitive context, how do we acknowledge it without making it the centerpiece?

---

## Phase 4: Sequence Build

Run the Signal to Sequence skill (`skills/signal-to-sequence/SKILL.md`).

Outputs:
- [ ] Touch 1 email (3 subject line variants)
- [ ] LinkedIn connection request
- [ ] Touch 3 email (different angle)
- [ ] Touch 4 email (asset/value add)
- [ ] Phone script / voicemail
- [ ] Break-up email

---

## Phase 5: QA

Before launch, every campaign goes through this review:

**Copy review:**
- [ ] Touch 1 passes PVP standard (see Signal to Sequence skill)
- [ ] No generic language ("I noticed..." / "I wanted to reach out...")
- [ ] Signal hook is specific and datable
- [ ] CTA is one action, not multiple options
- [ ] Links work, personalization variables are filled

**List review:**
- [ ] No existing customers in the list
- [ ] No active opportunities in the list
- [ ] No suppressed contacts
- [ ] Unsubscribe compliance check

**Tooling review:**
- [ ] Sequence loaded in outbound tool
- [ ] Personalization variables mapped and tested
- [ ] Send time set (Tuesday–Thursday, 7–9am local time recommended)
- [ ] Tracking enabled

---

## Phase 6: Launch and Monitor

**Week 1–2:** Monitor reply rates daily. Pause and adjust if reply rate < 1% after 50 sends.

**Week 3–4:** First performance review. Compare to targets set in measurement plan.

**Week 6:** Full campaign review. Decision: continue, iterate, or retire.

### Continue / Iterate / Retire Decision Framework

| Situation | Decision | Action |
|-----------|----------|--------|
| Reply rate ≥ target, meetings booking | **Continue** | Keep running. Add more accounts to the segment. |
| Reply rate ≥ target, but no meetings | **Iterate** | Rewrite the CTA and qualification criteria. The message is landing but the ask or fit is wrong. |
| Reply rate 50–80% of target | **Iterate** | Test a new subject line variant and rewrite touch 1 body. |
| Reply rate < 50% of target after 6 weeks | **Retire** | Kill the campaign. The signal-persona combination isn't working. Document what you learned in the campaign archive. |
| Strong week 1–2, then drops off | **Iterate** | The signal hook works but later touches don't. Rewrite touches 3–4. |
| Signal volume drying up | **Retire** | The signal is seasonal or exhausted. Archive and wait for next cycle. |

When you retire a campaign: write two sentences in the campaign brief on why it didn't work. That note is worth more than the campaign itself.

---

## Campaign Performance Benchmarks

Use these to calibrate expectations and catch underperformance early.

| Metric | Strong | Average | Weak — investigate |
|--------|--------|---------|-------------------|
| Email open rate | > 50% | 30–50% | < 30% |
| Reply rate | > 5% | 2–5% | < 2% |
| Positive reply rate | > 3% | 1–3% | < 1% |
| Meeting rate | > 2% | 0.5–2% | < 0.5% |

**If open rate is low:** Subject lines are the problem.
**If open rate is high but reply rate is low:** The body copy or CTA is the problem.
**If reply rate is high but meeting rate is low:** The qualification or ICP is the problem.

---

## Campaign Archive

Every completed campaign gets archived in `outputs/campaigns/` with:
- Original brief
- Final sequence copy
- Performance results
- Key learnings

The archive is searchable context for future campaigns. Before building a new campaign for a similar segment, check what's already been tried.
