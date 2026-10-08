---
name: describe-sample
description: Describe who is in a cleaned dataset with sample profiles, demographic charts, data dictionaries, decision ledgers, and verification checks.
---

# describe-sample

## Tool availability

Use interactive forms and file-writing tools when available. If not, ask concise inline questions and provide copy-ready tables, scripts, and narrative outputs.

A workflow skill for producing a polished sample-description bundle from a **cleaned** tabular dataset. Output is what you'd put in front of a stakeholder to answer "who took our survey / who's in our dataset" — not the analysis of what they said.

> Sample description is the "who" of a dataset. Response analysis is the "what they said." This skill is strictly about the WHO. If the user wants to summarize responses, scale ratings, or fee-structure preferences, suggest a different workflow.

---

## When to use this skill

Triggers (any of these phrasings):
- "describe my sample"
- "sample profile" / "build a sample profile"
- "who responded to my survey"
- "demographic summary"
- "describe the data"
- "participant characteristics"

Also use when the user is starting the descriptive-statistics phase of a survey / behavioral-study / panel project and needs a baseline characterization of the sample before any modeling.

**Do NOT use this skill when:**
- The data is uncleaned (recommend a cleaning skill first — this skill assumes a clean analytic dataset)
- The user wants response/outcome analysis ("how did people answer Q5?" is not sample description)
- The dataset is non-tabular (images, text corpora, time-series sensor data)
- The user wants inferential statistics or modeling (use a different skill)

---

## Scope of "sample description" (default, per the org's convention)

This skill, by default, produces output covering:

1. **Who the respondents are** — demographics: age, sex, race/ethnicity, geography, education, income, employment, language, nationality, etc.
2. **Sample-quality metrics** — retention waterfall, attention-check pass rates, completion-time patterns, missingness patterns, intersectional cell-size diagnostics.
3. **Behavioral / contextual traits** — caregiver status, prior experience with the topic, goals, recruitment channel, etc. — descriptive but not strictly demographic.

This skill does **NOT** produce:
- Response distributions on outcome variables
- Treatment vs. control comparisons of outcomes (it WILL detect treatment columns and report sample composition by arm, but not outcome effects)
- Statistical tests, effect sizes, or modeling output

---

## Operating principles (non-negotiables)

These come from the org's process conventions. Apply on every run.

### 1. Scope-check first
Before any computation, confirm with the user what the sample description should cover. Use the elicitation template in `references/elicitation-templates.md` → "scope_check". Never assume; "describe the sample" can be misread as "describe the responses".

### 2. Pause on PII
If the dataset contains columns that look like PII — names, email, IP, lat/long, full address, SSN, government IDs, financial accounts, medical records — stop reading data and request authorization before proceeding. See `references/pii-detection.md`.

### 3. Preserve raw, suffix derived
Never overwrite an original column. Cleaned/derived columns get a suffix (`_recoded`, `_binned`, `_clean`); when the data has multiple sources, prefix to indicate origin (`prolific_education`, `qualtrics_education`).

### 4. Propose, then confirm — for subjective transformations
Whenever a transformation involves a subjective call (age binning, race collapse, "Other"-recoding, low-income threshold), produce a transformation ledger with three random illustrative examples and offer the user an approval step. See `references/transformation-ledgers.md`.

### 5. Always ledger; always cite n
Every derived column has a ledger row. Every chart and table has an n caption. No exceptions.

### 6. Verification at the end
After all outputs are produced, run a spot-check pass that recomputes headline numbers from the raw data and compares to what appears in the deliverables. Surface any mismatches.

### 7. End with a summary memo
The final user-facing output is a summary that lists: (a) decisions made, (b) all files produced, (c) suggested uploads to a sample-description folder, (d) what was NOT done and why. See `references/end-summary-template.md`.

### 8. Date-stamp outputs, never overwrite
Outputs go in a dated subfolder of the user's chosen output location (e.g., `sample-description_2026-05-23/`). Old runs stay intact for comparison.

### 9. Recommend uploading raw + intermediate + final
At the end-summary stage, remind the user to upload all dataset states (raw, intermediate cleaned, analytic) to whatever shared folder is being used so the descriptive outputs are reproducible.

---

## Workflow

The skill is a sequenced, gated process. Each step has a clear hand-off to the next.

### Step 0 — Detect and scope

**Inputs to gather (preferring inference from conversation/context):**
- Path to the cleaned dataset (CSV, Excel, TSV, Parquet)
- Output destination (folder where deliverables should land; default = current working directory + dated subfolder)
- Study context (clinical / survey / HR / marketing / behavioral / other) — affects framing and methods language
- Brand to apply (default = ideas42 unless project context suggests otherwise; see `references/brand-styling.md`)

**Always ask via the interactive visualization capability elicitation form (fall back to the available structured-question interface if visualize is unavailable):**
- What "describe my sample" should cover (the three pillars above; user may scope down)
- Which deliverables to produce (always-on defaults are: long narrative, exec brief, individual charts, CSV profile, data dictionary; on-demand: methods blurb, public-safe variant)
- Whether there's benchmark / prior-wave data to compare against
- Whether there are key split-by columns (treatment arm, specific demographic) — adapt outputs accordingly
- Which specific demographics matter most (multi-select); whether any are particularly important to highlight

Use `references/elicitation-templates.md` for the canonical form layouts. Always mark the best-practice default with "(Recommended)".

### Step 1 — Load, profile, classify

Run `scripts/profile_data.py` against the dataset. It produces:
- A structural summary (rows, cols, dtype mix, primary-key uniqueness)
- A column classification (ID / temporal / numeric / categorical / boolean / text / structural) and a guess at each column's "role" (demographic / quality-flag / behavioral / outcome / metadata / pii-candidate)
- A null-rate and completeness report
- A flag for any PII-candidate columns

If PII is detected, **stop and request authorization** before proceeding.

### Step 2 — Multi-source reconciliation

If two or more columns appear to capture the same construct (e.g., a `qualtrics_income` and `prolific_income`), ask the user — using the elicitation form — which source is primary and document the choice. Output a "source convention" record. See `references/source-priority.md`.

### Step 3 — Adaptive subjective-transformation pass

For each column the user has confirmed is "demographic" or "behavioral":
- If the column is categorical with >10 unique values that look like they could be collapsed (e.g., 50 states → 4 regions, 9 race categories → 4 collapsed buckets), propose a collapse rule, generate a 3-example ledger, and ask the user to confirm before applying.
- If the column is continuous (age, income proxy), propose binning rules and confirm.
- If a column has obvious sentinel codes (-1, 99, 999), propose treatment.

All transformations land in `transformation_ledger.csv` with `column_in`, `column_out`, `decision`, `rationale`, `examples_shown`, `user_approved` columns.

### Step 4 — Compute statistics

Run the statistical helpers per variable type. See `references/variable-types-and-stats.md` for the canonical list. Includes:
- Numeric: n, mean, median, SD, percentiles, range, missing
- Categorical: n, %, missing
- Continuous demographics: histogram-ready bins + summary stats (per the org's adaptation preference: always include hist + box, not just bars)
- Quality metrics: retention waterfall (raw → eligible → consented → completed → quality-passed → analytic)
- Missingness patterns: per-column null rate + pairwise co-missingness + drop-vs-impute heuristic flag
- Intersectional cell-size diagnostics: for the demographics the user flagged as most important, compute pairwise crosstab cell sizes and flag any < min-cell-size threshold (default 10)
- Geographic enrichment (if state/ZIP detected): roll up to region/division/urban-rural

### Step 5 — Build charts (adaptive)

Run `scripts/build_charts.py`. The chart battery adapts to the variables present and the user's "important demographics" selection from Step 0:
- One chart (or panel) per major demographic family — Geography, Age + Sex, Income + Education, Employment, Ethnicity + Origin, Behavioral traits
- Continuous demographics get histogram + summary stats annotation
- Geographic columns get a top-N bar with the user's "key region" (if any) highlighted
- Each chart has: descriptive title that states the finding (not just the metric), branded colors, n caption, source footer
- Always produce: individual PNGs in `charts/`; on demand: overview grid PNG, slide-ready PPTX
- If the dataset is large (n > 5,000), simplify (top categories only, condensed tables)
- If the dataset is small (n < 100), every chart caption includes a small-n caveat
- If a treatment-arm column was identified in Step 0, produce arm-stratified versions of headline charts

### Step 6 — Build documents

Run `scripts/build_docs.js` to produce:
- **`Sample-Description_Narrative.docx`** — multi-section write-up with every chart embedded inline; sections for each variable family; limitations section; one-line summary
- **`Sample-Description_Brief.docx`** — 1–2 page exec summary with the overview chart and 5–7 key takeaways
- On demand: **`Methods_Boilerplate.docx`** — a paragraph suitable for a journal / IRB / proposal methods section
- On demand: **`Sample-Description_Public.docx`** — public-safe variant with cells < 5 suppressed and PII columns stripped

### Step 7 — Build the data dictionary

Run `scripts/build_data_dictionary.py`. Produces `Data-Dictionary.csv` with: `column`, `label` (from header row 2 if Qualtrics-style, otherwise the column name), `type`, `n_nonnull`, `n_unique`, `example_values`, `derived_from`, `notes`.

### Step 8 — Verification pass

Spot-check 10–20 headline numbers from the deliverables against fresh recomputations from the raw cleaned data. Report any mismatches in a `verification.md` file. If mismatches exist, halt and surface to the user before delivering.

### Step 9 — End-of-process summary

Produce `00_SUMMARY.md` in the output folder containing:
- The decisions made with the user (scope, source priorities, transformation ledger highlights)
- An outline of every file produced, organized by category
- Recommended next steps (e.g., "upload raw + intermediate + analytic datasets to the project folder")
- What this skill explicitly did NOT do and why
- Suggested next workflow (response distribution analysis, etc.)

---

## Output folder layout

The skill places all outputs in a single dated subfolder of the user's chosen output location:

```
<user-chosen-output-dir>/
└── sample-description_YYYY-MM-DD/
    ├── 00_SUMMARY.md                         # end-of-process summary memo
    ├── 01_Sample-Description_Narrative.docx
    ├── 02_Sample-Description_Brief.docx
    ├── 03_Data-Dictionary.csv
    ├── 04_Transformation-Ledger.csv
    ├── 05_Numeric-Profile.csv
    ├── 06_Categorical-Profile.csv
    ├── 07_Quality-Metrics.csv               # waterfall, missingness, cell sizes
    ├── 08_Methods-Boilerplate.docx          # if requested
    ├── 09_Sample-Description_Public.docx    # if requested
    ├── 10_Verification.md
    └── charts/
        ├── 01_Chart_Geography.png
        ├── 02_Chart_Age-Sex.png
        ├── 03_Chart_Income-Education.png
        ├── 04_Chart_Employment.png
        ├── 05_Chart_Ethnicity-Origin.png
        ├── 06_Chart_Behavioral-Traits.png
        ├── 07_Chart_Overview-Grid.png
        └── (more if adaptive)
```

**Naming convention:** human-readable, Title_Case with kebab-case-separated multi-word elements. Numeric prefixes for sort order. No underscores in display names that the user might read.

---

## Cloud upload behavior

After all outputs are produced, ask the user (via elicitation form) whether to:
- Stage in the local output folder for manual drag-and-drop into Drive/Box/OneDrive (recommended default — Drive MCP can't reliably push large binaries)
- Attempt API upload via available connector
- Skip the upload step

If staging, also output a `UPLOAD-MANIFEST.txt` listing every file with its full local path so the user has a clean copy-paste reference.

---

## Brand styling

Default is ideas42 (Figtree font, Indigo / Green Apple / Cayenne palette). The skill loads brand config from `assets/brand-defaults/<brand>.json`. To use a different brand, the user can:
- Supply a brand JSON at runtime
- Override individual settings via the elicitation form

See `references/brand-styling.md` for the brand config schema.

---

## Sub-skill loading (when to read references/)

Read each reference doc only when its concern becomes relevant — don't preload all of them at once.

- `references/variable-types-and-stats.md` — Step 4, when computing per-variable stats
- `references/adaptive-charts.md` — Step 5, when choosing what to render
- `references/transformation-ledgers.md` — Step 3, when proposing subjective transformations
- `references/elicitation-templates.md` — Any time user input is needed (Steps 0, 2, 3, and final upload prompt)
- `references/brand-styling.md` — Step 5/6, before any visual output
- `references/source-priority.md` — Step 2, only if multi-source overlap is detected
- `references/pii-detection.md` — Step 1, always
- `references/end-summary-template.md` — Step 9
- `references/scripts-reference.md` — invocation contracts for each helper script

---

## Failure modes to handle gracefully

- **Input file doesn't load** → ask user to confirm path, file format, encoding
- **No demographic-looking columns detected** → tell user the dataset doesn't look like sample-description input; offer to describe what columns ARE present
- **All columns flagged as PII** → halt and ask user whether to proceed with anonymized analysis
- **Single-row or empty dataset** → halt; explain
- **Wide dataset with hundreds of columns** → ask user to scope which variables matter
- **Multi-language dataset (mixed encodings)** → flag and confirm desired output language (default English)
