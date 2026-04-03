# Playbook: New Signal Response

*What to do when a signal fires. Step-by-step from detection to first touch.*

---

## Trigger

A Tier 1 or Tier 2 signal fires on an account in your ICP.

---

## Step 1: Validate the Signal (5 min)

Before doing anything else, confirm the signal is real and the account is qualified.

- [ ] Is the signal genuine? (Not a duplicate, not a data error)
- [ ] Is the account ICP-qualified? (Check against `context/icp-definition.md`)
- [ ] Is the account currently suppressed? (Existing customer, active opportunity, recent contact, unsubscribe)
- [ ] Is the signal fresh? (Within the recency window defined in `context/signal-library.md`)

If any check fails: log the signal, do not proceed.

---

## Step 2: Score the Account (10 min)

Run ICP Scoring skill or calculate manually using `context/signal-library.md`.

```
Read skills/icp-scoring/SKILL.md and score [company] given that the [signal name]
signal just fired.
```

Record the score and tier in CRM.

- Score ≥ 80 → Tier 1 process (below)
- Score 60–79 → Tier 2 process (below)
- Score < 60 → Add to automated Tier 3 sequence, no further manual action

---

## Tier 1 Response (Score ≥ 80)

**Time budget: 45–60 minutes. Outreach within 48 hours.**

### 2a. Research the Account

```
Read skills/account-research/SKILL.md and research [company.com].
Signal context: [signal name] fired [X] days ago.
Save output to outputs/[date]-[company]-research.md
```

### 2b. Identify the Right Contact

From the research output, select the primary contact. Criteria:
- Closest match to target persona (reference `context/personas/`)
- Verified email or LinkedIn reachable
- No previous contact in last 45 days

### 2c. Write the First Touch

Don't use a template. This is Tier 1 — it should read like you wrote it specifically for them.

```
Read the research at outputs/[date]-[company]-research.md and
context/signal-library.md.

Write a first touch email for [contact name] at [company].
The signal is [signal name]. Use the message hook from the signal library
as the starting point, but personalize it to the specific context you found
in the research.

Apply the PVP standard from skills/signal-to-sequence/SKILL.md —
the message should contain an insight they don't already have.
```

### 2d. Review and Send

- Read it out loud. If it sounds like an AI wrote it, rewrite the opening.
- Remove anything that could apply to any company.
- Confirm the signal hook is accurate and specific.
- Send from the assigned AE or founder, not a generic account.

---

## Tier 2 Response (Score 60–79)

**Time budget: 15 minutes. Sequence triggered within 48 hours.**

### 2a. Find the matching campaign

Check `outputs/campaigns/` for an existing campaign that matches this signal and persona. If one exists and is still active, add the contact to it.

If no matching campaign exists:
```
Read skills/signal-to-sequence/SKILL.md.
Build a Tier 2 sequence for the [signal name] signal targeting [persona].
```

### 2b. Personalize touch 1

Even in automated sequences, touch 1 should have one personalized element — a reference to the specific signal event.

### 2c. Add to sequence and log

- Add contact to sequence in outbound tool
- Log the action in CRM
- Set a reminder to review reply status in 7 days

---

## After First Touch

Regardless of tier, log the following in CRM after outreach:

- Signal that triggered outreach
- Date of first touch
- Contact reached
- Sequence enrolled (or manual outreach noted)
- Signal score at time of outreach

This data is what lets you calibrate the signal library over time.
