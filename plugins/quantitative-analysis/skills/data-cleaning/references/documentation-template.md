# Documentation templates

Every run produces a process document (`04_Cleaning-Process_Documentation`) and a one-page summary (`09_Summary.md`). Use these templates as the structural backbone — fill with the actual decisions and findings from the run.

## Process document template

Emit as a Google Doc if a Drive folder is specified (use HTML content with `mcp__76238cea-5e51-4cfe-9470-2099020745e3__create_file` and content type `text/html` → convert to Doc). Otherwise emit as `04_Cleaning-Process_Documentation.md`.

```markdown
# {Dataset Name} — Data Cleaning Documentation

**Source data:** {input file paths}
**Cleaned on:** {date}
**Final analytic dataset:** `08_Cleaned-Data_FINAL.csv` · {rows} rows × {cols} columns

## 1. Overview

This document records every decision made to transform the raw input ({raw_rows} rows, {raw_cols} columns) into the analysis-ready dataset ({final_rows} rows, {final_cols} columns). Each step is reproducible from the inputs and the rules described below — see `06_Cleaning-Script.{py,R}`.

**Input files:**
- `{primary_file}` — {description}
- `{secondary_file}` — {description, if any}

## 2. Discovery (Phase 1)

{One paragraph summary of what was learned during profiling.}

**Key facts:**
- Unit of analysis: one row per {unit}
- Primary key: `{primary_key_column}` ({uniqueness}% unique)
- {Other relevant Phase 1 findings}

**Outputs:**
- `01_Data-Profile.md` — initial profile
- `02_Column-Dictionary.csv` — per-column inventory

## 3. Row Filtering (Phase 2)

{Filters applied and rationale. If no filters were applied, say so explicitly.}

| Step | Filter | Rows after | Dropped |
|---|---|---|---|
| 0 | Raw | {raw_rows} | — |
| 1 | {filter} | {after} | {dropped} |
| ... | ... | ... | ... |

**Retention:** {final_rows} / {raw_rows} = {pct}%

See `03_Row-Cleaning-Audit.csv` for the machine-readable audit.

## 4. Secondary-Source Merge (Phase 3b, if applied)

{Only include this section if a secondary merge was performed.}

**Sources merged:** {source_name_1}, {source_name_2}
**Join key:** `{key_column}`
**Coverage:** {n_matched} / {n_primary} rows had a match
**Strategy on overlapping columns:** {Primary or secondary preferred for which fields, and why}

Secondary-source columns are prefixed with `{source_prefix}_`. Disagreement flags surface where the two sources tell different stories — see `disagree_*` columns.

## 5. Column Transformations (Phase 3)

{One subsection per transformation type that was applied. Drop subsections that didn't apply.}

### 5.1 Multi-select binary explosion

{Which columns; canonical option lists; substring-matching approach; coverage check.}

New columns: `{list}`

### 5.2 Numeric text parsing

{Which column; parse-rule taxonomy; coverage; sample edge cases.}

See `05_Decision-Ledger_{column}_parsing.csv` for the full ledger.

### 5.3 Likert ordinal recodes

{Which columns; scale used; mapping.}

### 5.4 Categorical ordinal recodes

{Income, education, etc.}

### 5.5 "Other" write-in recoding

{Which columns; themes promoted vs. left in residual.}

### 5.6 Open-text categorical coding

{Which columns; category frame; multi-label coding rules.}

### 5.7 Reverse-coded item detection

{If applicable.}

### 5.8 Outlier flagging

{Which columns; threshold methods; no rows were dropped.}

### 5.9 Strategic segment binaries

{is_X binaries created; what each represents.}

### 5.10 Cross-source disagreement flags

{If a merge happened, which disagreement flags exist and what they signal.}

## 6. Optional Modules Applied

- [ ] Reference-data validation
- [ ] Unit standardization
- [ ] Derived variables
- [ ] Fuzzy deduplication
- [ ] Long ↔ wide reshape
- [ ] Schema suggestion

{Drop this section if none applied; expand on each that did with what was done.}

## 7. Limitations

- **Subjective decisions to revisit:** {list with pointers to ledgers}
- **Outlier handling:** No rows were dropped. Flags exist for sensitivity tests. Decide at analysis time whether to filter on specific flag columns.
- **Fields not coded:** {list any open-text columns that were deferred}
- **Source disagreements:** {if applicable, summarize key disagreements between merged sources}
- **Sample representativeness:** {anything relevant about who the data does and doesn't represent}

## 8. File Manifest

| File | Description |
|---|---|
| `00_Source-Manifest.md` | Input files used, with timestamps |
| `01_Data-Profile.md` | Initial profile |
| `02_Column-Dictionary.csv` | Column metadata |
| `03_Row-Cleaning-Audit.csv` | Row filter audit |
| `04_Cleaning-Process_Documentation` | This document |
| `05_Decision-Ledger_*.csv` | One per subjective transformation |
| `06_Cleaning-Script.{py,R}` | Reproducible end-to-end script |
| `08_Cleaned-Data_FINAL.csv` | The analytic dataset |
| `09_Summary.md` | One-page recap |
```

## Summary template (`09_Summary.md`)

```markdown
# Cleaning summary — {Dataset Name}

**Raw input:** {raw_rows} rows × {raw_cols} columns
**Final dataset:** {final_rows} rows × {final_cols} columns
**Retention:** {pct}%
**Cleaned on:** {date}

## Decisions made

- {One bullet per interactive decision — what was asked, what was chosen, link to relevant artifact}
- Example: "reCAPTCHA threshold set to 0.5 (Google + Qualtrics default) → 11 rows dropped. See `03_Row-Cleaning-Audit.csv`."

## Artifacts produced

- `01_Data-Profile.md` — Initial dataset profile
- `02_Column-Dictionary.csv` — Per-column metadata
- `03_Row-Cleaning-Audit.csv` — Row-filter step audit
- `04_Cleaning-Process_Documentation` — Full process narrative
- `05_Decision-Ledger_*.csv` — Approval ledgers per subjective transformation
- `06_Cleaning-Script.{py,R}` — Runnable script
- `08_Cleaned-Data_FINAL.csv` — Analytic dataset
- `09_Summary.md` — This file

## Recommended next steps

- **Quantitative analysis** → a data-analysis workflow
- **Qualitative coding of open-text fields** → {list uncoded text fields, recommend qual workstream}
- **Sensitivity tests** → re-run analyses with these flag filters: {list relevant flag columns}
- **Upload artifacts** → recommend uploading raw, intermediate, and final files to the working folder ({path or Drive folder}) so collaborators can find them

## Limitations to revisit at analysis time

{List of subjective decisions an analyst should double-check before publishing. Each gets a one-line explanation and a pointer to the relevant ledger or audit row.}
```

## When to use Google Doc vs Markdown

- **Google Doc:** If the user specified a Drive folder during Discovery and the Drive connector is available. Generates richer formatting (headings, tables, bold) that's easier to skim.
- **Markdown:** Default if no Drive folder. Lives in the working folder.

In either case, the file is named `04_Cleaning-Process_Documentation` (without extension for Google Doc, with `.md` for markdown).

## Style notes

- Sentence case for all headings (not Title Case, not ALL CAPS).
- Use tables for any tabular content; readers skim those faster than prose.
- Code style for column names: `cost_guess_parsed` not "cost_guess_parsed".
- One sentence per bullet; no nested bullets more than one level deep.
- Always end with a Limitations section. Never claim the data is fully clean — every cleaning operation introduces decisions that an analyst should be able to question.
