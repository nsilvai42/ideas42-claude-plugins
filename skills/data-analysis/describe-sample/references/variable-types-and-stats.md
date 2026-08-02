# Variable types and statistics

For every column the user has confirmed should appear in the sample description, compute statistics matched to its detected type. This file is the canonical reference for what to compute.

## Type detection — heuristics

| Detected as | Heuristic |
|---|---|
| **ID** | Column name contains `id`, `uuid`, `pid`, `response_id`; OR `n_unique == n_rows` and dtype is string/int |
| **Temporal** | dtype is datetime; OR column name contains `date`, `time`, `created`, `_at`; OR string parses as ISO date |
| **Numeric – continuous** | dtype is float OR int with > 20 unique values AND range > 50 |
| **Numeric – ordinal** | dtype is int with 2–10 unique consecutive values, OR column name ends in `_ord`, `_rank`, `_scale` |
| **Boolean** | dtype is bool; OR values are exactly {0,1} / {True,False} / {Yes,No} |
| **Categorical – nominal** | dtype is string/object with 2–50 unique values |
| **Categorical – high-card** | dtype is string with > 50 unique values (e.g., free text, ZIP code) |
| **Text – free** | dtype is string with avg length > 50 chars |
| **Structural** | Contains JSON, arrays, or nested data |
| **PII-candidate** | See `pii-detection.md` |

## Role inference — heuristics

After type detection, infer the column's analytic role.

| Role | Signal |
|---|---|
| **Demographic** | Name matches `age`, `sex`, `gender`, `race`, `ethnicity`, `income`, `education`, `employment`, `state`, `country`, `nationality`, `language`, `marital`, `household` |
| **Behavioral / contextual** | Name matches `caregiver`, `prior_*`, `experience`, `goals`, `interest`, `recruitment_*`, `referral` |
| **Quality flag** | Name matches `attention_check`, `recaptcha`, `consent`, `finished`, `duration`, `progress`, `status` |
| **Treatment / arm** | Name matches `treatment`, `arm`, `condition`, `group`, `variant`, `cohort` |
| **Outcome** | Name matches `q\d+`, `score`, `rating`, `_ord`, `likelihood`, `fairness`, `_response` — flag but DO NOT include in sample description by default |
| **Metadata** | Name matches `start_date`, `end_date`, `device`, `browser`, `ip` |
| **PII-candidate** | See `pii-detection.md` |

**Important:** Always present the role assignments to the user via the elicitation form before computing. Do not assume.

## What to compute per type

### Numeric – continuous (e.g., age, income proxy)

- `n_nonnull`, `n_missing`, `null_pct`
- `mean`, `median`, `sd`
- Percentiles: `p1, p5, p25, p75, p95, p99`
- `min`, `max`
- Skewness (Fisher-Pearson) — surface only if |skew| > 1
- Suggested bins for histogram (default: Freedman-Diaconis if n > 100, otherwise 10 equal-width bins)
- Outlier flag: any value outside [p1, p99]

### Numeric – ordinal (e.g., Likert, education ladder)

- All of the above EXCEPT skewness (irrelevant for ordinals)
- Plus: mode, % at mode, % at extremes (1 and max)
- Distribution as percentage table

### Boolean

- `n_true`, `n_false`, `n_missing`
- `pct_true` (of non-null)
- Both n and % for both states

### Categorical – nominal

- Frequency table: `value`, `n`, `pct_of_total`, `pct_of_nonnull` — top 15 if cardinality > 15
- `n_unique`, `n_missing`
- Mode + mode share
- For each value: cumulative coverage (useful when checking if top-5 covers 80% of sample)

### Categorical – high-card (states, ZIPs, free text)

- Top-12 frequency table
- Aggregate the long tail as "Other (N categories)"
- For state/ZIP: geographic enrichment (region, division, urban/rural)

### Text – free

- `n_nonnull`, `n_missing`
- Length stats: min, median, max characters
- Don't try to summarize content — flag for separate qualitative coding workflow

### Temporal

- min date, max date, range
- For each year/month present: count of records
- Day-of-week and time-of-day patterns (useful for completion-time analysis)
- Gaps in coverage (if expected to be continuous)

## Sample-quality metrics (always compute)

### Retention waterfall

If the dataset has columns indicating filter steps, build a waterfall:

```
Raw recruited        n=___
  passes screener    n=___ (-X% to —Y%)
  consented          n=___
  completed          n=___
  attention-check    n=___
  analytic           n=___
```

Auto-detect via columns like `Finished`, `Status`, `Attention_Check`, `recaptcha_score`, `consent`, etc. If detection fails, ask the user to identify gate columns.

### Missingness patterns

Beyond per-column null %:
- **Pairwise co-missingness matrix**: of cells where col A is null, what % are also null in col B?
- **Missingness clusters**: columns that are null together (suggesting a skipped survey section)
- **MAR/MCAR heuristic flag**: does null-status correlate with any other column? If yes → flag as "missingness not random; consider sensitivity analysis"
- **Drop-vs-impute hint per column**: > 50% missing → flag as unusable; 20-50% → recommend sensitivity test; < 20% → safe to use

### Intersectional cell-size diagnostics

For the demographics the user flagged as "key" in Step 0:
- Generate pairwise crosstabs (e.g., income × race, age-bucket × education)
- Report any cell with n < min_cell_size (default 10)
- Output a `thin-cells.csv` listing each combination, n, and recommended treatment (collapse, exclude, or proceed with caveat)

## Continuous demographic special handling

When a demographic is continuous (age, income proxy), don't just produce a bar chart. Produce **both**:
- A histogram with mean + median lines
- A box plot with outlier dots

The chart-builder script handles this; this reference exists so per-variable stats include both representations' inputs.

## Geographic enrichment

When a column is identified as state or country:
- For US states: map to region (Northeast / Midwest / South / West) and division (9 Census divisions)
- For ZIPs: map to state, region, urban/rural classification (Rural-Urban Commuting Area codes)
- For countries: map to UN region / sub-region; flag if non-US in a study assumed US-only

Output rolled-up columns as suffixed derived columns: `state_region`, `state_division`, `zip_rural_urban`.

## Adaptation rules (apply automatically)

| Condition | Adaptation |
|---|---|
| n < 100 | Add "small-sample caveat" to every chart caption |
| n > 5,000 | Simplify outputs: top-10 categories per chart, no overview grid by default |
| Longitudinal data detected (wave/timepoint column) | Add a wave column to every frequency table; chart by wave when relevant |
| Treatment/arm column detected | Produce arm-stratified versions of headline charts |
| Multi-language data | Confirm output language with user before writing docs |

See `adaptive-charts.md` for how these affect chart selection.
