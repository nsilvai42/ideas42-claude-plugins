# Pattern detectors

How to recognize each cleanable pattern in a column. Apply these heuristics during Phase 1 (Discovery profiling) and Phase 3 (per-column transformations). All thresholds are starting defaults — tune based on the user's stated analytic goal.

## Column-type classification (first pass)

For each column, assign one or more tags based on dtype, content, and metadata:

| Tag | Heuristic |
|---|---|
| `identifier` | Cardinality ≥ 95% of row count; name matches `id|key|uuid|email|phone` |
| `temporal` | Dtype is datetime, or values parse as dates in ≥80% of rows |
| `numeric_metric` | Dtype is numeric; cardinality > 20; positive skew or normal distribution |
| `numeric_bounded` | Numeric; all values in 0–1, 0–100, or 1–N (N≤10) range |
| `boolean` | Distinct values ⊂ {True/False, Yes/No, 0/1, T/F, t/f} |
| `categorical_low` | Object dtype; 3–15 distinct values; no length variance |
| `categorical_ordered` | `categorical_low` AND values match an ordinal pattern (Very/Somewhat/Neutral or bracket ranges) |
| `multi_select` | Object dtype; values frequently contain a delimiter (`,` `;` `|`); option strings repeat across rows |
| `text_short` | Object dtype; median length 10–80 chars; high cardinality; not categorical |
| `text_long` | Object dtype; median length > 80 chars; very high cardinality |
| `numeric_in_text` | Object dtype; ≥50% of values parse as numeric after stripping `$,%` and whitespace |

A column can carry multiple tags. Resolve conflicts based on which transformation the user would benefit from most.

## Numeric-in-text detection

Trigger when: column dtype is `object` AND ≥50% of values parse as numeric after applying:
1. Strip whitespace
2. Remove `$`, `,`, `%`, and unicode equivalents (`＄`)
3. Resolve `k` / `K` suffix (`5k` → 5000)
4. Resolve simple ranges (`100-200` → midpoint)

If trigger is met, propose the full numeric text parsing pipeline (see `numeric-text-parsing.md`).

## Multi-select detection

Trigger when:
- Dtype is `object`
- ≥30% of non-null values contain a delimiter (`,` `;` `|`)
- The set of substrings across rows is small (≤30 unique) — i.e., the same options repeat

**Critical:** before splitting, check whether any option string itself contains the delimiter (e.g., "Financial aid (Pell Grant, state grant, etc.)" contains commas). If so, use substring-match against a canonical option list rather than naive splitting. If the option list isn't visible from the data, ask the user — they probably have the survey instrument or the source spec.

## Likert-ordered text detection

Trigger when:
- Dtype is `object`
- 4–7 distinct non-null values
- Distinct values match one of these patterns:
  - `Strongly disagree / Disagree / Neutral / Agree / Strongly agree`
  - `Very unlikely / Somewhat unlikely / Neutral / Somewhat likely / Very likely`
  - `Very X / Somewhat X / Neutral / Somewhat ~X / Very ~X` (any antonym pair)
  - `Never / Rarely / Sometimes / Often / Always`

Map to 1–N where 1 = lowest valence and N = highest. For 7-point scales, use 1–7. Map "Prefer not to say" / "N/A" to NaN.

## Bracket/categorical-ordinal detection

Trigger when distinct values look like ranges or brackets:
- `Under $X` / `$X–$Y` / `$Y+`
- `0–17 / 18–24 / 25–34 / …`
- `Less than high school / High school / Some college / Bachelor's / Graduate`

Map to 1–N in natural order. Sentinel values like "Prefer not to say" → NaN.

## "Other" write-in detection

Trigger when a column name ends in `_OTHER`, `_OTHER_TEXT`, `_TEXT`, `_specify` AND there's a paired categorical column (same prefix without the suffix).

Process:
1. Inventory all values (typically 5–50 non-null).
2. Cluster by normalized string (lowercase, strip whitespace).
3. Identify themes with ≥3 mentions.
4. Propose: new binary column per theme, residual flag for everything else.
5. Optionally: if a written value matches an existing option in the paired categorical (e.g., respondent wrote "Parents" when "Family or partner" was already an option), offer to fold into the existing option's binary.

## Pseudo-categorical free text detection

Trigger when an open-text column has:
- Very high cardinality (≥80% unique)
- BUT many responses fall into a small number of semantic categories (detectable by clustering or by association with a paired closed-end question)

Process:
1. Ask the user for the category frame, OR
2. Infer from a paired closed-end question (e.g., a Likert similarity rating using 6 anchors → use those 6 anchors as the frame)
3. Multi-label code each response: one binary per category, plus an "uncoded" residual.
4. Always ledger (random sample of 10 codings for approval).

## Date string detection

Trigger when:
- Dtype is `object`
- ≥80% of values parse as dates with `pandas.to_datetime(errors='coerce')`
- OR column name matches `date|time|created|updated|started|ended|timestamp`

Process:
1. Detect the most common format(s).
2. Propose normalization to ISO 8601 (`YYYY-MM-DD` or `YYYY-MM-DD HH:MM:SSZ`).
3. Flag rows where parsing failed.

## Compound-text detection

Trigger when:
- Object dtype
- Median length 20–80 chars
- Values consistently contain a structural separator (`, ` for `City, State`; full names with spaces; addresses)

Common patterns:
- Full name → first name + last name (heuristic: split on first space; flag if ≥3 tokens)
- "City, State" → city + state
- Address → street + city + state + zip (use a library or regex)

Always ledger if the split is heuristic.

## Reverse-coded scale item detection

Trigger when a battery of Likert items (consecutive columns with same scale) is detected.

Process:
1. Compute pairwise correlations between items.
2. Items that correlate negatively with the majority are candidates.
3. Surface candidates with example wording — ask the user to confirm.
4. If confirmed, create `X_reversed` column with re-scored values: `(N+1) - X` for N-point scale.

## Outlier detection

For numeric metric columns:
- **IQR method:** values outside Q1 - 1.5×IQR or Q3 + 1.5×IQR → `X_outlier_iqr`
- **Percentile threshold:** values above the 95th or 99th percentile → `X_outlier_p95` / `X_outlier_p99`
- **Domain threshold:** if the user provides a context-specific limit (e.g., "cost shouldn't exceed $20k for an online cert"), use that → `X_outlier_domain`

Always offer all three; choose default based on distribution shape. Always flag-only, never drop.

## Cross-column consistency detection

Look for:
- Date pairs (`*_start` / `*_end`, `*_from` / `*_to`) → flag rows where start > end
- Numeric triples (`quantity` + `unit_price` + `total`) → flag rows where the relationship doesn't hold
- Ranges (`min` / `max` of same metric) → flag rows where min > max
- Conditional logic (if status=X then field Y should be populated) → flag violations

Surface detected pairs to user for confirmation before applying.

## Reference-data candidates

Columns that look like:
- Country names → validate against ISO 3166-1
- US states → validate against USPS state codes
- Currencies → validate against ISO 4217
- Email addresses → validate format
- Postal codes → validate against country-specific format

Offer validation; flag unknown values.

## Unit-mixed detection

Trigger when a numeric column has values with mixed unit indicators in adjacent text (e.g., `"5 kg"` and `"12 lb"`, or `$X` and `€Y`).

Process:
1. Detect the unit alongside each value.
2. Propose normalization to a single unit (ask user which target).
3. Apply conversion factors; ledger.

## Derived-variable opportunities

Common derivations to suggest based on what columns exist:
- DOB + reference date → age
- Height + weight → BMI
- Started_at + ended_at → duration
- Steps completed / steps total → completion rate
- First name + last name → display name

Always opt-in; ask the user if they want the derivation.
