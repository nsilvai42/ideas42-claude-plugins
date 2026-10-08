# Scripts reference

Invocation contracts for every helper script in `scripts/`. All scripts read a single `config.json` from the run's output folder and write outputs to that same folder. They are designed to be runnable standalone OR via the SKILL.md workflow.

## Common config (`config.json`)

Every script reads this:

```json
{
  "input_dataset": "/abs/path/to/cleaned_data.csv",
  "output_dir":    "/abs/path/to/output_dir/sample-description_2026-05-23/",
  "brand":         "ideas42",
  "brand_path":    "assets/brand-defaults/ideas42.json",
  "study_context": "behavioral",
  "n_total":       314,
  "primary_key":   "ResponseId",
  "columns": {
    "demographic": ["age", "sex", "income", ...],
    "behavioral":  ["caregiver", "prior_online_ed", "goals"],
    "quality":     ["Attention_Check", "Finished", "Duration"],
    "treatment":   ["arm"],
    "pii":         [],
    "exclude":     ["IPAddress", "LocationLatitude"]
  },
  "key_demographics": ["age", "income", "is_california"],
  "split_by": null,
  "min_cell_size": 10,
  "small_n_threshold": 100,
  "large_n_threshold": 5000
}
```

## `profile_data.py`

**Purpose:** Adaptive profiler. Reads the dataset, classifies columns by type and role, computes per-variable statistics, detects PII, generates retention waterfall, missingness patterns, and intersectional cell-size diagnostics.

**Inputs:**
- `config.json` in the output folder

**Outputs (into output_dir):**
- `05_Numeric-Profile.csv`
- `06_Categorical-Profile.csv`
- `07_Quality-Metrics.csv` (contains retention, missingness, cell-size sub-tables stacked with a `metric` discriminator column)
- `column_classification.json` (internal, used by downstream scripts)

**Usage:**
```bash
python scripts/profile_data.py --config /abs/path/to/config.json
```

## `build_charts.py`

**Purpose:** Adaptive chart builder. Reads classification + brand + config and produces the chart battery.

**Inputs:**
- `config.json`
- `column_classification.json` (from profile_data.py)

**Outputs (into output_dir/charts/):**
- `NN_Chart_<Topic>.png` — one per detected variable family
- `00_Chart_Overview-Grid.png` if `n_total <= large_n_threshold`

**Usage:**
```bash
python scripts/build_charts.py --config /abs/path/to/config.json
```

## `build_docs.js`

**Purpose:** docx-js builder. Reads charts + stats + brand and produces narrative + brief.

**Inputs:**
- `config.json`
- `column_classification.json`
- All chart PNGs in `output_dir/charts/`
- Profile CSVs

**Outputs (into output_dir):**
- `01_Sample-Description_Narrative.docx`
- `02_Sample-Description_Brief.docx`
- `08_Methods-Boilerplate.docx` if requested

**Usage:**
```bash
node scripts/build_docs.js --config /abs/path/to/config.json
```

## `build_data_dictionary.py`

**Purpose:** Generate a column glossary CSV.

**Outputs:** `03_Data-Dictionary.csv`

**Columns:** `column`, `label`, `type_inferred`, `role_inferred`, `n_nonnull`, `n_unique`, `example_values`, `derived_from`, `transformation_ledger_ids`, `notes`

## `build_public_variant.py`

**Purpose:** Generate a public-safe variant of the narrative — cells < 5 suppressed, PII columns stripped, watermark applied.

**Outputs:** `09_Sample-Description_Public.docx`

## `verify.py`

**Purpose:** Spot-check pass. Re-computes 10–20 headline numbers from the raw cleaned data and diffs against numbers that appear in the deliverables.

**Outputs:** `10_Verification.md` with PASS/FAIL per claim and any mismatches surfaced.

## Order of execution

```
profile_data.py
    ↓
(propose transformations, get user approval — orchestrated by SKILL.md)
    ↓
build_charts.py
    ↓
build_data_dictionary.py
    ↓
build_docs.js
    ↓
(if requested) build_public_variant.py
    ↓
verify.py
    ↓
(SKILL.md writes 00_SUMMARY.md as the final step)
```

## Dependencies

Python scripts require:
- pandas, numpy
- matplotlib (and the Figtree font files in `assets/fonts/`)
- scipy (for stats and t-tests on CI calculations)

Node scripts require:
- `docx` package (install: `npm install docx`)

If a dependency is missing, scripts emit a clear error with the install command. The SKILL.md orchestrator should detect this and run install before retrying.
