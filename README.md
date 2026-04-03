# GTM Starter Kit

Built by [The Revenue Architects](https://therevenuearchitects.com) — a GTM engineering firm based in San Francisco. We work with growth-stage B2B SaaS companies to build the signal systems, data infrastructure, and AI-powered workflows that make outbound systematic rather than manual.

This repo is the open-source version of what we build with clients. Clone it, fill in your context files once, and run AI-powered GTM tasks from a single prompt — no rebuilding context every session.

---

## How It Works

Claude Code reads `CLAUDE.md` automatically at the start of every session. That file contains your company overview, ICP, signals, personas, and current priorities. Once it's filled in, you can run any task with a one-line prompt — no re-explaining your context each time.

```
Read skills/account-research/SKILL.md and research stripe.com
```

Claude reads your ICP, signals, and personas from the repo and produces a full account research brief. You didn't paste any context. It was already there.

---

## What's Inside

```
gtm-starter-kit/
│
├── CLAUDE.md                           ← Fill this in first. Claude reads it every session.
│
├── context/                            ← Your GTM institutional knowledge
│   ├── profile.md                      ← Company overview, product, team, reference customers
│   ├── icp-definition.md              ← ICP tiers, filters, anti-ICP, qualification criteria
│   ├── signal-library.md              ← Signals with scoring, detection methods, hooks
│   ├── positioning.md                 ← Value pillars, competitive positioning, what not to say
│   ├── competitor-radar.md            ← Battlecards, win/loss patterns
│   └── personas/
│       └── template.md                ← Persona template — duplicate for each buyer role
│
├── sync/                               ← Scripts for pulling live data into the repo
│   ├── README.md                       ← Setup and usage
│   ├── .env.example                    ← Copy to .env and fill in API keys
│   ├── sync-campaign-results.py        ← Pull reply/meeting rates from outbound tool
│   └── sync-signal-performance.py     ← Aggregate signal performance across campaigns
│
├── skills/                             ← Claude executes these. One-line prompts.
│   ├── account-research/SKILL.md      ← Deep research on any account before outreach
│   ├── signal-to-sequence/SKILL.md    ← Turn a signal into a live outbound campaign
│   ├── icp-scoring/SKILL.md          ← Score accounts against your ICP, assign tiers
│   └── weekly-update/SKILL.md        ← Keep context current. Run Monday mornings.
│
├── workflows/                          ← How your team operates. Human process docs.
│   ├── enrichment.md                  ← Data waterfall: free sources → Clay → proprietary
│   ├── signal-routing.md              ← Decision tree: signal fires → what happens next
│   └── campaign-build.md             ← End-to-end: audience → launch → measurement
│
├── playbooks/                          ← Step-by-step for specific situations
│   ├── new-signal-response.md         ← Signal fires: validate → score → research → send
│   └── competitor-switch.md          ← Four scenarios: unknown, active eval, intent, locked in
│
├── outputs/                            ← All skill outputs land here
│   └── .gitkeep
│
└── examples/
    └── sample-company/                 ← Relay — a fully built-out example
        ├── CLAUDE.md
        ├── context/
        │   ├── profile.md
        │   ├── icp-definition.md
        │   ├── signal-library.md      ← Has real performance data attached
        │   ├── positioning.md         ← Value pillars, messaging matrix, what not to say
        │   ├── competitor-radar.md
        │   └── personas/
        │       └── head-of-revops.md
        └── outputs/
            ├── weekly-log.md          ← Change history from weekly-update skill runs
            ├── 2024-03-15-research-northstar-analytics.md   ← Sample research brief
            └── campaigns/
                └── 2024-03-01-series-b-revops-tier2/
                    ├── brief.md       ← Campaign brief with results tracking
                    └── sequences.md  ← Full email sequences, live copy
```

**Skills vs. Workflows — what's the difference?**
- **Skills** are for Claude to execute. You run them with a prompt and Claude produces an output. This includes the weekly-update skill, which keeps the repo current rather than producing a deliverable.
- **Workflows** document how your team operates — the decision trees and processes that connect your tools. They're reference documents for humans, not execution instructions for Claude.

---

## Getting Started in 4 Steps

### Step 1: Fork and clone

```bash
git clone https://github.com/[your-org]/gtm-starter-kit.git
cd gtm-starter-kit
```

Open the repo in Claude Code:
```bash
claude .
```

---

### Step 2: Fill in CLAUDE.md (45 min)

This is the highest-leverage thing you can do. Claude reads this file first on every session.

Open `CLAUDE.md` and fill in:
- Company overview (2–3 sentences, not a pitch)
- ICP — one sentence plus the 3 firmographic filters you'd use to build a list
- Anti-ICP — be explicit, this prevents wasted outreach
- Persona table — titles, primary concern, best channel
- Top 3 signals — name them, even if the full library isn't built yet
- Current priorities — what you're focused on this week

Not sure what "done" looks like? Open `examples/sample-company/CLAUDE.md` and use it as a reference.

---

### Step 3: Fill in your context files (2–3 hours)

Work through these in order. Start with the ones that will unblock the most tasks.

| File | Time | Start here if... |
|------|------|-----------------|
| `context/icp-definition.md` | 60 min | You want to run ICP scoring or build campaigns |
| `context/signal-library.md` | 45 min | You want to run signal-triggered outreach |
| `context/personas/` | 30 min each | You want personalized first touches |
| `context/positioning.md` | 45 min | You want competitive angles in outreach |
| `context/competitor-radar.md` | 30 min per competitor | You're in active competitive deals |

For each file: open the template, open the corresponding file in `examples/sample-company/context/` side-by-side, and fill in your version. The example shows what a completed file looks like.

---

### Step 4: Run your first skill

Once CLAUDE.md and at least `context/icp-definition.md` are filled in, you're ready.

**Research an account:**
```
Read skills/account-research/SKILL.md and research [company.com]
```

**Score a list of accounts:**
```
Read skills/icp-scoring/SKILL.md and context/icp-definition.md.
Score these companies and output a table sorted by score, Tier 1 flagged:
[paste company names or domains]
```

**Build a campaign from a signal:**
```
Read skills/signal-to-sequence/SKILL.md.
Build a Tier 2 campaign for accounts that triggered the [signal name] signal.
Target the [persona title] persona.
```

All outputs get saved to `outputs/` — see the naming convention below.

---

## Output Naming Convention

```
outputs/YYYY-MM-DD-[type]-[name].md

Examples:
outputs/2024-03-15-research-northstar-analytics.md
outputs/2024-03-01-scoring-q1-prospect-list.md
outputs/campaigns/2024-03-01-series-b-revops-tier2/brief.md
```

---

## Keeping It Current

Run the weekly-update skill every Monday morning:

```
Read skills/weekly-update/SKILL.md and run the weekly context update.
```

Claude reads the repo, identifies what's stale, drafts every section that changed, and asks you to fill in the parts it can't know. 10 minutes instead of 45.

Manual cadence for the rest:

| Cadence | What to update |
|---------|---------------|
| Weekly | Run `/weekly-update` skill |
| After every win/loss | Update `context/competitor-radar.md` win/loss patterns |
| Quarterly | Review `context/icp-definition.md` — add an entry to the ICP evolution log |

---

## What Not to Put in This Repo

- **CRM data or contact lists** — never commit customer or prospect data to git
- **API keys or credentials** — use environment variables, never hardcode
- **Raw meeting transcripts** — summarize and synthesize into the relevant context file
- **Pricing** — keep commercial terms out of the repo

---

## Example

`examples/sample-company/` is a fully built-out version of the repository for Relay, a fictional workflow automation platform. Every context file is populated. Two real sample outputs are included: an account research brief and a live campaign with email sequences and performance tracking.

Use it as a reference when filling in your own files. The signal library in particular (`examples/sample-company/context/signal-library.md`) shows what a mature, data-backed signal library looks like — with detection methods, decay logic, performance tracking, and signal combination rules.

---

## License

MIT
