# Cost / Open-Ended Numeric Parsing Audit Template

Use whenever the original analysis converted a free-text numeric field (e.g., open-ended cost estimate, hours studied, expected salary) into a structured number.

## Inputs

- Raw column (verbatim text from respondents)
- Cleaned column (parsed numeric values)
- The parsing rule the AI used (prompt or code, verbatim if available)
- A statement of what NaN means (e.g., "respondent skipped" vs. "respondent gave a non-numeric answer")

## Stratified sample

Pull 30 rows in three strata of 10 each:

| Stratum | What you're checking |
|---|---|
| Low-end (cleaned <$200 or <$5/hour) | Did "free" / "0" / "very little" get correctly coded? Are placeholder "1" values legitimate? |
| Mid-range (typical bulk of the distribution) | Verbal expressions like "five hundred", "1k", "around 2 grand" — do they convert correctly? |
| High-end / outliers (cleaned > 90th percentile) | Real outliers vs. accidental zeros (e.g., "$50,000" entered when respondent meant "$5,000")? Ranges ("$10k–$20k") collapsed to one endpoint? |

Also include any rows where the cleaned value is `NaN`:

| Stratum | What you're checking |
|---|---|
| NaN cleaned values | Was the raw value genuinely non-numeric ("I don't know") or did the parser fail on a parseable answer ("about $400")? |

## Audit columns

| Column | Description |
|---|---|
| row_idx | Index in the raw file |
| raw_text | Verbatim respondent answer |
| cleaned_value | Parsed numeric |
| expected_value | What a human reviewer thinks the value should be (or NaN with reason) |
| match | Yes / No |
| miscoding_type | If No: undercoded / overcoded / wrong-units / wrong-range / verbose-not-parsed / placeholder-vs-NaN |
| reviewer_note | Free text |

## Pass thresholds

| Stratum | Pass threshold (for H-stakes claims) |
|---|---|
| Low-end | 95% match |
| Mid-range | 95% match |
| High-end | 90% match (outliers are inherently noisy) |
| NaN | 95% (NaN is a categorical claim that matters as much as a numeric one) |

## Common patterns

- "I don't know" / "no idea" / "depends" / "varies" → `NaN`, not 0.
- Ranges: by convention either take the midpoint, take the low end, or flag for human review. Be consistent.
- Currency symbols and commas should be stripped, not coded as missing.
- "$1k" / "1k" / "1,000" / "one thousand" should all parse to 1000.
- "Free" should parse to 0, not NaN.
- "100s" / "thousands" — flag, do not parse to a specific number.

## Output

A passing audit produces a short memo with the pass rate and the parsing-rule changes (if any) needed for the next analysis run.
A failing audit produces a list of row indices to re-parse and a note in the master ledger saying which claims depend on this field.
