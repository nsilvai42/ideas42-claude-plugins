# Column naming convention

Originals are sacred. Derived columns are suffixed (and prefixed when sourced externally).

## Rules

1. **Never overwrite an original column.** Every cleaning operation creates a new column.
2. **Suffix derived columns with the operation type**, not the meaning. The suffix tells you *what was done*; the column body tells you *what it represents*.
3. **Prefix with source name when joining from another file/system.** Source prefix is lowercase, separated by underscore.
4. **Use snake_case throughout.** Convert from any other naming convention in originals (`PROLIFIC_PID` → `prolific_pid` for new columns).
5. **Keep the original column name intact** as the base for suffixed derivatives. Don't rename the base.

## Suffix table

| Suffix | Meaning | Example |
|---|---|---|
| `_raw` | Preserved original (when an operation overwrites in place would have been more natural) | `cost_guess_raw` |
| `_parsed` | Cleaned numeric extracted from text | `cost_guess_parsed` |
| `_min` | Lower bound of a range parse | `cost_guess_min` |
| `_max` | Upper bound of a range parse | `cost_guess_max` |
| `_ord` | Ordinal recode of a categorical scale | `income_bracket_ord` |
| `_clean` | General normalization (whitespace, case, encoding) | `state_clean` |
| `_iso` | Date normalized to ISO 8601 | `started_at_iso` |
| `_flag` | Categorical tag from a parsing operation | `cost_guess_flag` |
| `_recoded` | Categorical with "Other" merged or labels remapped | `employment_recoded` |
| `_normalized` | Standardized value (units, references, etc.) | `currency_normalized` |
| `_reversed` | Reverse-coded scale item, re-scored | `item_7_reversed` |
| `_outlier_{method}` | Boolean: is this row an outlier by the named method | `revenue_outlier_iqr` |
| `_n_selected` | Count of selected options in a multi-select | `funding_n_selected` |

## Prefix table

Used when a column comes from a different data source than the primary dataset.

| Prefix | Meaning | Example |
|---|---|---|
| `{source}_` | Column originated in the named source | `prolific_income` |
| `disagree_` | Cross-source disagreement flag | `disagree_income` (between Qualtrics & Prolific) |
| `is_` | Boolean derivation from existing column(s) | `is_california` |
| `has_` | Boolean for "row has X" | `has_consent` |
| `n_` | Numeric count derived | `n_categories_selected` |

## Binary column naming

For multi-select explosions: `{base_column}_{normalized_option}`. Normalize option label by:
- Lowercase
- Replace spaces and special chars with underscore
- Truncate to ~40 chars if very long
- Resolve duplicates by appending an index

Examples:
- `funding_financial_aid` (from option "Financial aid (Pell Grant, state grant, etc.)")
- `funding_checking_savings` (from option "Checking/savings account")
- `funding_other_specify` (from option "Other (please specify)")

## Strategic segment binaries

When the user identifies analytically important slices, create explicit `is_X` binaries:
- `is_california`
- `is_first_time_buyer`
- `is_active_subscriber`

These should be clearly documented in the process doc with the rule used.

## When the same data passes through multiple operations

Chain suffixes in operation order:
- `cost_guess_raw` → `cost_guess_parsed` (text → number) → `cost_guess_parsed_outlier_p95` (flag for outlier)

Avoid chains longer than two suffixes — at three suffixes deep, the column is doing too much; consider whether the intermediate column is actually needed in the final dataset.

## Sanity check at end of run

Before finalizing, verify:
- No original column was overwritten
- All derived columns have a recognizable suffix
- All cross-source columns have a source prefix
- Strategic binaries are named `is_*` or `has_*`
- All suffixes appear in the file manifest with explanations
