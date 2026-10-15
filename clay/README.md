# clay/

Clay tables live in the Clay UI and cannot be deployed from code. So this folder is the record of your tables, not their source. Its job: anyone, Claude included, can tell what a table does, what it costs and where its output goes, without clicking through 40 columns.

---

## One file per table

Name it `clay/[table-name].md`. Only tables that run more than once need a file. A one-off table gets a line in `outputs/` if its result matters.

```markdown
# [Table name]

Link: [Clay URL] | Owner: [name] | Status: [live / paused]
Last updated: [YYYY-MM-DD]

## Purpose
[One sentence. Which workflow it serves, e.g. workflows/enrichment.md, Tier 2.]

## Input
Source: [CSV / CRM view / webhook / another table]
Trigger: [manual / scheduled / webhook]

## Columns, in run order
| Column | Provider or action | Runs when | Fallback |
|--------|-------------------|-----------|----------|
| [Work email] | [Provider A] | [LinkedIn URL found] | [Provider B] |

## AI columns
[Paste each prompt in full. Prompts change most often and are the first thing lost.]

## Output
[Which CRM or tool fields it writes, and how: CRM action, webhook, export.]

## Cost
[Credits per row, roughly] x [rows per month] = [credits per month]

## Change log
| Date | What changed | Why |
|------|-------------|-----|
```

---

## What never goes here

Row data. No CSV exports, no contact lists. The root `.gitignore` already blocks `*.csv`.
