# cargo/

Your Cargo workspace, as code. Empty until you connect a workspace.

Cargo can be driven three ways: the UI, the CLI (`cargo-ai`, one command per change), and the CLI's project mode (formerly `cargo-ai cdk`), where every connector, model, play and tool is a TypeScript file and `cargo-ai project deploy` brings the workspace in line with the code. This folder is for the third. It is what lets Claude change a workflow and leave a trace you can review in a PR.

---

## What goes in here

Anything that runs on its own (a cron, a trigger), writes to your CRM, or spends credits every week.

What stays out: one-off backfills, tests, a single enrichment run. Do those with the CLI and keep the trace in `outputs/YYYY-MM-DD-[name]/` (the script, a short README, the result), so you can run it again without this folder carrying it forever.

---

## Setup

1. Install the CLI and sign in:

```bash
npm install -g @cargo-ai/cli
cargo-ai login
cargo-ai whoami        # confirm the workspace before any write
```

2. Copy the Cargo skills from [getcargohq/cargo-skills](https://github.com/getcargohq/cargo-skills) into `.claude/skills/`. Claude then knows the CLI and the project commands.

3. Ask Claude:

```
Set up cargo/ as a Cargo project and pull my live workspace into it.
```

That runs `cargo-ai project pull`, which writes one file per live resource and adopts it, so the next deploy changes nothing.

4. Commit everything, including `cargo.state.json`.

Typical layout once set up:

```
cargo/
├── connectors/          ← Secrets via secret("ENV_VAR"), never inline
├── models/
├── plays/
├── tools/
├── agents/
├── segments/
├── package.json
└── cargo.state.json     ← Commit it. The only link between the code and the live resources
```

---

## Rules that save you

- **Plan before every deploy.** `cargo-ai project plan --dir cargo` shows what will change. `cargo-ai project refresh --dir cargo` shows what changed in the UI since the last deploy.
- **The live workspace drifts.** Someone fixes a play in the UI, the code is now behind, and deploying it would undo the fix. Before changing a resource, compare it with what is live. If the live one moved, bring the code up to date first.
- **Adopt what was built outside the code.** A model or play created in the UI or the CLI gets added here in the same PR (`cargo-ai project import <kind:slug> <uuid>`), so this folder stays the full picture.
- **New plays ship disabled.** Dry run, check the credits, then switch on.
- **Tunable values live in records, not code.** Weights, thresholds and lists go in a model's records, so you change them without a deploy.
- **Name models by layer.** `src_` (raw from a source), `stg_` (cleaned), `sig_` (signals), `qa_` (checks). You can tell what a model does from its name.
