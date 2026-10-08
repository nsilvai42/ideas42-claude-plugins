# Ledger format

Every subjective transformation produces a CSV ledger documenting raw → output value, the method used, and a one-sentence rationale per row. The ledger is the audit trail. It's also the artifact the user reviews for approval before the transformation is finalized.

## When a ledger is required

Required:
- Text → numeric parsing (e.g., "$10k plus" → 10000)
- Open-text categorical coding (free response → one or more category labels)
- "Other" write-in reassignment (free text → existing or new category)
- Reverse-coded scale item re-scoring
- Fuzzy deduplication merge decisions
- Compound-column splits where the split rule is heuristic
- Unit standardization conversions
- Any transformation where the same input could plausibly produce different outputs under different reasonable interpretations

Not required:
- Binary flag creation from explicit boolean rules (e.g., `is_california = (state == "California")`)
- Ordinal mapping from a clean enum (e.g., income brackets → 1–5)
- Numeric column merges or arithmetic combinations
- ISO date format conversion
- Whitespace trimming / case normalization (note in process doc instead)
- Filling NaN with a documented sentinel
- Multi-select binary explosion via substring matching (deterministic)

## Minimum schema

```
{key_column}, raw_input, output_value, flag, method, rationale
```

Where:
- `{key_column}` — the row's primary identifier (ResponseId, customer_id, etc.). The user picks this in Discovery.
- `raw_input` — original value verbatim.
- `output_value` — what the transformation produced; can be NaN.
- `flag` — categorical tag describing the parse / coding category (e.g., `clean`, `range_midpoint`, `dk`, `off_topic`, `wrong_unit`).
- `method` — short label for the rule that fired (e.g., `direct`, `range_parsed`, `k_suffix`, `qualifier_stripped`).
- `rationale` — one human-readable sentence explaining what was changed and why.

## Extended schema (when applicable)

For numeric parsing where ranges or bounds are meaningful:
```
{key_column}, raw_input, output_value, output_min, output_max, flag, method, rationale
```

For categorical coding with multiple labels:
```
{key_column}, raw_input, [one boolean column per category], rationale
```

For deduplication merges:
```
{key_columns_of_both_records}, similarity_score, merge_decision, kept_record, dropped_record, rationale
```

## Approval workflow

1. Generate the full ledger CSV.
2. Save it as `05_Decision-Ledger_{operation_name}.csv`.
3. **Sample 5–10 rows randomly** from the ledger (stratified by `flag` if there are many flag values).
4. Present the sample to the user in chat using a clean table format. Show: raw_input, output_value, flag, rationale.
5. Ask: "Look reasonable? Y / make changes / show me more examples." Use `interactive elicitation tool` for the question.
6. If "make changes," ask which rows or methods to revisit and iterate.
7. Save the final approved ledger; finalize the transformation.

## Sampling principle for the chat preview

Don't just show the first 5–10 rows — that biases toward whatever flag fires first. Instead:
- If the ledger has multiple `flag` values, show at least one example per flag.
- Randomize within each flag.
- Cap at 10 rows total to keep the chat preview compact.
- If there are <10 ledger rows total, show them all.

## Example ledger row

For a text → numeric parsing operation on a cost-guess column:

```csv
ResponseId,raw_input,parsed_value,range_min,range_max,flag,method,rationale
R_3M4IdNNDYkRuMsd,"$15,000 - $30,000",22500.0,15000.0,30000.0,range_midpoint,range_parsed,"Range parsed: $15000-$30000; using midpoint $22500"
R_5xAeEhCel83YYW5,"1,000?",1000.0,,,open_ended,x_question_mark,"Open-ended estimate; used $1000"
R_1TuZnZ20aC5joYy,"not sure",,,,dk,dk_phrase,"Respondent said they don't know; no number extracted"
R_7VLaOn1DRc8tU2w,"free",0.0,,,free,free_keyword,"'free' coded as $0"
```

The user sees a sampled preview, approves, and the ledger lives alongside the cleaned dataset as the permanent audit trail for that transformation.
