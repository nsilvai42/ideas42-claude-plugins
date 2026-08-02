---
name: data-cleaning
description: Clean tabular datasets interactively, preserve raw columns, ledger subjective choices, generate reproducible scripts, and document the process.
---

# Data cleaning

## Tool availability

Use interactive elicitation, files, scripts, or inline questions depending on the current environment. If an interactive form tool is unavailable, ask only the smallest set of chat questions needed to make the cleaning decision.

A guided, interactive cleaning workflow for any tabular dataset. Detect the shape of the data, ask the user about intent and edge cases, propose pattern-appropriate transformations, and produce a documented audit trail plus a reproducible script.

## When to use

Use this skill when the user:
- Uploads a CSV, Excel, TSV, JSON, or Parquet file and wants it cleaned
- Says "this data is messy" or "get this analysis-ready"
- Has a tool export (Qualtrics, SurveyMonkey, Prolific, CRM dump, etc.) that needs normalization
- Wants a quality audit before analysis
- Needs to merge multiple data sources

Do not use for:
- Analysis on already-clean data → a data-analysis workflow
- Qualitative thematic coding of open-text → hand off after structural cleaning is done
- Visualization or dashboard building → a visualization workflow or a dashboard workflow
- Spot-checking a single calculation → use `verify-data-analysis`

## Operating principles

1. **Interactive by default.** Every meaningful decision goes to the user through a `an available interactive elicitation or preview tool` elicitation form. Fall back to `the available structured-question interface` if the interactive visualization capability is unavailable. Mark the clear best-practice option with `(recommended)`.

2. **Pattern-driven, not meaning-driven.** Detect what kind of data each column holds — numeric-in-text, multi-select string, Likert text, free response, date string, compound name, etc. — and propose cleaning steps appropriate to the type. Never hardcode column-name-specific behavior. During Discovery, ask the user what each section of the data represents and what the analytic goal is, then map detected patterns to that context.

3. **Preserve and augment, never replace.** Original columns are always kept untouched. Derived columns are suffixed with the operation (`X_clean`, `X_ord`, `X_flag`, `X_binary`, `X_parsed`). When a column comes from a different data source, prefix it with the source name (`prolific_X`, `salesforce_X`). See `references/column-naming.md` for the full convention.

4. **Ledger every subjective decision.** Any transformation that involves judgment produces a CSV ledger documenting raw → output value, method, and rationale. Always surface a randomly sampled 5–10 row subset to the user for spot-check approval before finalizing. See `references/ledger-format.md`.
   - **Ledger required:** text → numeric parsing, fuzzy categorical recoding, "Other" write-in reassignment, open-text pseudo-categorical coding, reverse-coded item detection, fuzzy deduplication.
   - **Ledger not needed:** binary flag creation from explicit rules, ordinal mapping from a clean enum, numeric column merges, ISO date format conversion, whitespace trimming.

5. **Flag, don't drop.** Outliers, suspect values, and quality concerns get binary flag columns rather than row removal, so the analyst can run sensitivity tests. Only drop rows when the user explicitly asks (e.g., bot-suspected responses, unfinished submissions, non-consenters).

6. **Document everything.** Every run produces a complete artifact bundle (see Phase 4). The process documentation includes a Limitations section covering subjective decisions to revisit, outlier-handling deferrals, fields not coded, and any cross-source disagreements.

7. **Use understandable artifact names.** Files are numbered to show process order and named with human-readable descriptions, not internal codes. See the file-naming convention in Phase 4.

## Workflow

### Phase 1 — Discovery

1. **Load the file(s).** Handle CSV, TSV, Excel (with sheet selection), JSON, Parquet. Auto-detect multi-header formats (e.g., Qualtrics 3-row headers) and preserve them.

2. **Build initial profile.** Row count, column count, dtype per column, null rates, distinct counts, top values per column, date range if temporal columns exist, approximate file size. Classify each column heuristically (identifier / dimension / metric / temporal / text / boolean / structural). See `references/pattern-detectors.md`.

3. **Ask the user via `an available interactive elicitation or preview tool`** (fall back to `the available structured-question interface`):
   - What is this data about? (free text)
   - What's the unit of analysis (one row per ___)?
   - Which column is the primary/unique key? (offer detected candidates)
   - What analytic question will this support?
   - Are there secondary data sources to join in? (yes / opt-in later / no)
   - Output script language: Python or R? (default Python, recommended)
   - Working folder: confirm path; if Drive, note for later upload

4. **Save:** `01_Data-Profile.md` (narrative profile) and `02_Column-Dictionary.csv` (column → original metadata / question text if present → inferred type → null rate → distinct count → notes).

### Phase 2 — Row filtering (interactive)

Detect candidate row-filter conditions by pattern. For each detected condition, surface an elicitation form with options including drop / flag-only / skip.

Common patterns the skill knows how to detect:

- **Completion / partial responses** — columns named `Finished`, `Status`, `Progress`, `Complete`, or boolean columns where values cluster at endpoints.
- **Consent / opt-in gate** — columns where one value is overwhelmingly dominant and the column name suggests permission (`consent`, `agree`, `terms`, `opt_in`).
- **Duplicate identifying values** — any column with cardinality close to but not equal to row count; offer dedup with strategies (keep first / keep last / keep most-complete / merge).
- **Bot or quality scores** — columns named `*Recaptcha*`, `*BotScore*`, `quality_score`, or any 0–1 float distribution. Default threshold 0.5 (matches Google reCAPTCHA v3 and Qualtrics defaults). Offer 0.3 / 0.5 (recommended) / 0.7 / custom.
- **Speeders / fast completion** — duration columns with a heavy left tail. Offer flag-only (recommended), not drop.

Each applied filter logs to `03_Row-Cleaning-Audit.csv` (step / rows-after / rows-dropped / rationale). Skip silently if no filter patterns are detected.

### Phase 3 — Column transformations (interactive, pattern-by-pattern)

Run pattern detectors across all columns. For each pattern detected, surface a single elicitation form with:
- What was detected (with example values)
- Suggested operation (with `(recommended)` on best practice)
- Output column names that will be created
- Whether a ledger will be produced

Apply, then if subjective, present 5–10 random ledger rows in chat for approval.

Patterns to detect and the operations to offer:

- **Numeric-in-text** — column is object dtype, but >50% of values look numeric after stripping `$ , %` etc. → propose deterministic parsing pipeline (see `references/numeric-text-parsing.md`). Outputs: `X_parsed`, `X_min`, `X_max`, `X_flag`, `X_raw`. Always ledgered.

- **Multi-select string** — values consistently contain a delimiter (comma, semicolon, pipe), repeated option strings across rows → propose substring-matching binary explosion. **Critical:** never naive-split on delimiter when option labels may contain that delimiter; instead match each canonical option as a substring. If the canonical option list isn't visible from the data, ask the user. Outputs: one `X_optionname` binary per option plus `X_n_selected`. Not ledgered.

- **Likert-ordered text** — 5–7 distinct values with recognizable ordinal labels (`Very X` / `Somewhat X` / `Neutral` / etc.) → propose ordinal recode (1–N). Output: `X_ord`. Not ledgered.

- **Bracket/categorical ordinal** — clear ordered buckets (income ranges, age groups, education levels) → propose ordinal recode with the "Prefer not to say" / "Other" values mapped to NaN. Output: `X_ord`. Not ledgered.

- **Low-cardinality categorical** (3–15 distinct, no order) — propose label normalization (case/whitespace) and optional binary explosion for top categories. Output: `X_normalized` and optional binaries. Light ledger only if any merges happen.

- **"Other" write-in text** (paired with a categorical) — cluster into themes, propose new binary columns for themes with ≥3 mentions, leave the rest in residual. Output: `X_themename` binaries + `X_other_residual` flag. Ledgered (which themes were promoted, what residual values look like).

- **Pseudo-categorical free text** (open text where many responses actually fall into a closed-end frame — e.g., "what does this remind you of") — ask user for the category frame (or infer from a paired closed-end question) and propose multi-label coding into those categories plus emergent ones. Output: one `X_category` binary per category. Ledgered.

- **Date strings (mixed format)** — propose ISO parse + canonical format. Output: `X_iso`. Not ledgered.

- **Compound text** (full names, addresses, "city, state, zip" strings) — propose split. Output: `X_part1`, `X_part2`, etc. Ledgered if rule is fuzzy.

- **Reverse-coded scale items** — Likert items in a battery where semantic loading reverses (e.g., "I dislike X" among "I like X" / "I enjoy X" items). Detect via inter-item correlation sign reversal. Output: `X_reversed` (re-scored). Ledgered.

- **Numeric outliers** — IQR-based or percentile-based. Always flag-only by default. Output: `X_outlier_p95`, `X_outlier_iqr`, etc.

- **Cross-column consistency** — pairs like `start_date` / `end_date`, `quantity` / `unit_price` / `total`, `min` / `max` — propose validation flags. Output: `consistency_check_X` flag.

### Phase 3b — Optional opt-in modules

After the main pattern pass, offer these if the data supports them (do NOT always-ask):

- **Secondary-source merge.** If the user indicated secondary sources in Discovery, prompt to join. Detect shared key columns. After merge, offer disagreement flags for any column that exists in both sources (`demo_disagree_X` for overlap; `X_source_distance` for numeric/ordinal mismatch magnitude). Source-derived columns get the source prefix.

- **Reference-data validation.** If a column looks like countries, US states, ISO currency codes, postal codes, etc., offer validation against canonical lists. Flag unknown values.

- **Unit standardization.** If values look like measurements with mixed units (kg/lb, USD/EUR, mm/in), propose normalization to a single unit.

- **Derived variables.** Suggest common derivations from detected columns: age from DOB, time-on-task from timestamps, BMI from height + weight, completion-rate from steps.

- **Fuzzy deduplication.** Beyond exact key dupes, detect near-duplicates using normalized string similarity. Always surface a ledger of candidate matches for approval before merging.

- **Long ↔ wide reshape.** If the data shape would aid the stated analytic goal, propose reshape.

- **Schema suggestion.** Propose dtype + value-domain spec per column for downstream validation systems.

- **Strategic segment binaries.** Ask the user if there are slices that matter for analysis (e.g., "California vs. rest", "primary caregiver yes/no"). Create explicit `is_X` binaries from existing columns. Not ledgered.

### Phase 4 — Documentation + handoff

Generate the final artifact bundle:

| # | File | Format | Always? |
|---|---|---|---|
| `00_Source-Manifest.md` | Source files used, with paths and timestamps | md | ✓ |
| `01_Data-Profile.md` | Initial profile (Phase 1 output) | md | ✓ |
| `02_Column-Dictionary.csv` | Per-column metadata | csv | ✓ |
| `03_Row-Cleaning-Audit.csv` | Step-by-step row filter log | csv | If Phase 2 ran |
| `04_Cleaning-Process_Documentation` | Narrative explainer | Google Doc if Drive, else md | ✓ |
| `05_Decision-Ledger_{operation}.csv` | One per subjective transformation | csv | If any ledgered op |
| `06_Cleaning-Script.{py,R}` | Runnable raw → final pipeline | py or R | ✓ |
| `07_Cleaned-Data_Intermediate_{stage}.csv` | Optional snapshots between phases | csv | If user requests |
| `08_Cleaned-Data_FINAL.csv` | Analytic dataset | csv | ✓ |
| `09_Summary.md` | One-page recap of decisions + manifest + limitations + next steps | md | ✓ |

**Required content of `04_Cleaning-Process_Documentation`:**
- Overview (input files, output dataset, retention rate)
- Phase 1: discovery findings + decisions made
- Phase 2: row filters applied (table from audit)
- Phase 3: each transformation with rationale
- Phase 3b: optional modules applied
- Limitations (subjective decisions to revisit, deferrals, uncoded fields, source disagreements, sample-representativeness notes)
- File manifest (mirrors the table above)

**Required content of `09_Summary.md`:**
- One sentence per interactive decision made (with link to the relevant ledger or audit)
- Full file manifest with one-sentence descriptions
- "Recommended next steps" — e.g., qualitative coding for remaining open text, a data-analysis workflow for analysis, sensitivity tests using specific flags

**At the end of the run:**
1. Recommend uploading all raw, intermediate, and final artifacts to the working folder (Drive or local).
2. If a Drive folder was specified, ask whether to auto-upload now (use the Drive `create_file` connector if available).
3. If open-text columns remain uncoded, suggest a follow-up qualitative coding pass as a separate workstream.

## Conventions

### File naming
Numbered in process order, sentence-case descriptive names, underscores between words within a label, hyphens within a label for word separators. See Phase 4 table.

### Column naming
See `references/column-naming.md` for the full table. Quick reference:

| Pattern | Example | When |
|---|---|---|
| Original | `respondent_age` | Never overwritten |
| Parsed numeric | `X_parsed`, `X_min`, `X_max`, `X_flag`, `X_raw` | From text → number |
| Ordinal recode | `X_ord` | Text scale → numeric |
| Binary flag | `is_california`, `passed_quality` | Boolean derivation |
| Multi-select binary | `funding_financial_aid` | One per exploded option |
| Source-prefixed | `prolific_income` | Joined from a different source |
| Disagreement flag | `demo_disagree_income` | Cross-source comparison |
| Outlier flag | `X_outlier_p95` | Suspect value flag |
| Recoded categorical | `X_recoded` | Merged "Other" + base |

### Ledger format
See `references/ledger-format.md`. Minimum schema:
`{key_column}, raw_input, output_value, [output_min, output_max,] flag, method, rationale`

### Folder structure
If a six-folder structure is already in use in the working folder (`01_Context/`, `02_Working/`, `03_Deliverables/`, `04_Assets/`, `05_Parking Lot/`, `06_Archive/`), place all skill outputs in `02_Working/`. Otherwise place them directly in the working folder. Never modify files in `04_Assets/` — copy source files there if they're not already.

### Task tracking
Use TaskCreate / TaskUpdate to track the four phases. Mark each phase in_progress when starting and completed when done. Surface phase completion to the user.

## Tool usage

- **Interactive questions:** `an available interactive elicitation or preview tool` with the `elicitation` module. Fall back to `the available structured-question interface` if visualize is unavailable. See `references/elicitation-template.md` for the form pattern.
- **File loading and saving:** Read/Write/Edit for files in the working folder. Use bash with pandas for the actual data manipulation.
- **Drive upload (end of run):** Drive connector's `create_file` if available and a Drive folder was specified.
- **Skill task tracking:** TaskCreate, TaskUpdate.

## Limitations

- This skill does not perform statistical analysis. Hand off to a data-analysis workflow after cleaning.
- This skill does not perform thematic coding of long-form open text. Hand off to a qualitative coding skill or workstream after cleaning.
- This skill does not modify source files. Always work from copies.
- Subjective decisions are surfaced for approval but not exhaustively second-guessed. Analysts should review the Limitations section of the process documentation before publishing results.
- For very large datasets (>10M rows), some pattern detectors sample rather than scan full data. The skill flags this when it occurs.
