# Numeric text parsing

Deterministic rule-based pipeline for cleaning a column that should be numeric but was fielded as open text. Always produces a ledger; always asks the user for approval after surfacing a sample.

## Input shape

Object-dtype column where most values look numeric but contain noise: currency symbols, ranges, qualifiers, abbreviations, "don't know" responses, unit indicators, etc.

## Output columns

- `{col}_raw` — preserved original (when the column was named in a way that needs to be overwritten in the analyst's mental model)
- `{col}_parsed` — best single-value parse, float, or NaN
- `{col}_min` — lower bound of a range if a range was detected
- `{col}_max` — upper bound of a range if a range was detected
- `{col}_flag` — categorical tag describing what kind of parse fired

## Flag taxonomy

| Flag | When it fires | Output |
|---|---|---|
| `clean` | Value was already directly numeric after stripping `$,` and whitespace | `parsed = value` |
| `range_midpoint` | Two numbers with a range operator (`-`, `to`, `–`) | `parsed = midpoint`, `min`, `max` populated |
| `word_form_range` | Range expressed in words ("four to eight thousand") | `parsed = midpoint`, `min`, `max` populated |
| `open_ended` | Single number with qualifier (`around X`, `X plus`, `X+`, `over X`, `X max`, `X?`, `Xish`) | `parsed = value` |
| `kabbrev` | K-suffix abbreviation (`5k`, `$10K`) | `parsed = value * 1000` |
| `word_form` | Word-form quantity ("a couple hundred", "a few thousand") | `parsed = heuristic value` |
| `free` | Literal "free" or "$0" | `parsed = 0` |
| `dk` | "Don't know" / "Not sure" / "Unsure" / "No clue" with no number | `parsed = NaN` |
| `self_resolved` | DK language followed by a final guess ("I'm bad at guessing… going to guess maybe 5000") | `parsed = final guess` |
| `wrong_unit` | Per-month / per-semester / per-year when the question asked for total | `parsed = NaN` (don't auto-convert; flag for analyst) |
| `vague` | "A lot", "many", "tons" — no quantifiable value | `parsed = NaN` |
| `off_topic` | Respondent reframed or declined without giving a number | `parsed = NaN` |

## Parsing rules (apply in order, return on first match)

1. **Normalize.** Unicode NFKC (handles full-width `＄`), replace en-dash/em-dash with hyphen, strip leading/trailing whitespace.

2. **Direct parse.** Strip `$`, `,`, whitespace. Try `float()`. If success → `clean`.

3. **Self-resolved DK.** If DK regex matches AND a "going to guess / will say / just guess" phrase appears with a number within 30 chars → use that number. Flag: `self_resolved`.

4. **DK-only.** DK regex matches and no digits anywhere → NaN. Flag: `dk`.

5. **Vague.** Matches `^(a lot|alot|many|tons|lots)$` → NaN. Flag: `vague`.

6. **Free.** Contains `\bfree\b` and no digits → 0. Flag: `free`.

7. **Wrong unit.** Contains `per month|per semester|per year|per week|a month|monthly` → NaN with the extracted number noted in the rationale. Flag: `wrong_unit`.

8. **Word-form range.** Pattern `(one|two|...|ten) (to|and|-) (one|...|ten) (hundred|thousand)` → midpoint. Flag: `word_form_range`.

9. **Word-form single.** Phrases from a lookup: "couple hundred" = 200, "few hundred" = 300, "a few thousand" = 3000, "several hundred" = 500, "several thousand" = 5000. Flag: `word_form`.

10. **Digit ranges.** Patterns:
    - `\$\s*(\d[\d,]*(?:\.\d+)?)\s*(k?)\s*(-|to)\s*\$?\s*(\d[\d,]*(?:\.\d+)?)\s*(k?)`
    - `between\s+(\d[\d,]*(?:\.\d+)?)\s*(k?)\s*(-|to|and)\s*(\d[\d,]*(?:\.\d+)?)\s*(k?)`
    - `\b(\d[\d,]*(?:\.\d+)?)\s*(k)\s*(-|to)\s*(\d[\d,]*(?:\.\d+)?)\s*(k?)`
    - `\b(\d[\d,]*(?:\.\d+)?)\s*(-|to)\s*(\d[\d,]*(?:\.\d+)?)\s*(dollars?|usd)?\b`
    
    Compute midpoint; populate min/max. Apply k-multiplier to either side if present. Flag: `range_midpoint`.

11. **K-abbreviation single.** `\$?\s*(\d+(?:\.\d+)?)\s*k\b` → value × 1000. Flag: `kabbrev`.

12. **Open-ended single.** In order:
    - `\$?\s*(\d[\d,]*(?:\.\d+)?)\s*(plus|\+|or more)` → plus_or_more
    - `(over|at least|easily over|more than)\s+\$?\s*(\d[\d,]*(?:\.\d+)?)` → over_x
    - `\$?\s*(\d[\d,]*(?:\.\d+)?)\s*(max|maximum)` → x_max
    - `\$?\s*(\d[\d,]*(?:\.\d+)?)\s*\?` → x_question_mark
    - `\$?\s*(\d[\d,]*(?:\.\d+)?)\s*ish\b` → ish
    
    Use the captured number. Flag: `open_ended`.

13. **Single number with text.** Find all numbers in the string. For each candidate, skip if immediately followed by a unit word (`semester|month|week|year|day|course|module|hour|class|certificate`). Skip 4-digit numbers in the range 1900–2100 if preceded by `since|in|year|around|circa` (they're years, not the answer). If a "final guess" phrase appears (`going to guess|i'll say|i will say|going with|so i am going to guess`), prefer the LAST candidate; otherwise prefer the first. Flag: `open_ended` (method `qualifier_stripped` if a qualifier word is present, else `single_num_with_text`).

14. **Fallback.** No usable number found → NaN. Flag: `off_topic`.

## Edge-case handling

- **Numbers attached to non-dollar units.** "$1000 per semester" or "125 a month" — flag as `wrong_unit`. Don't auto-convert assuming a duration; that's an analyst decision.
- **Sub-$1 values.** "0.50" → parse as 0.50. Don't reject as suspect.
- **Negative numbers.** Unusual for cost-type questions; flag with `flag=clean` but note in rationale.
- **Currency other than USD.** "€5000" or "¥500" — strip the symbol, parse the number, and add a note to the rationale that currency was non-USD. Don't auto-convert.
- **Typos in word forms.** "several hudred" (missing 'n') — leave as `off_topic`. Typo recognition is fragile; don't pretend you can fix it.

## After parsing, before finalizing

1. Save the ledger as `05_Decision-Ledger_{column_name}_parsing.csv` with columns: `{key}, raw_input, parsed_value, range_min, range_max, flag, method, rationale`.

2. Surface a stratified random sample of 5–10 rows in chat (one example per flag if possible).

3. Ask the user via elicitation: "Look right? / Show me more / Make changes."

4. If approval: write `{col}_parsed`, `{col}_min`, `{col}_max`, `{col}_flag` to the dataset; `{col}_raw` preserved.

5. If changes: iterate. Common adjustments — "treat ranges as upper bound, not midpoint" / "don't code 'free' as 0, leave as NaN" / "the column was per-semester all along, multiply per-semester values by 2".

## Reference implementation (Python)

See the SKILL workflow — emit a script in `06_Cleaning-Script.py` that implements this exact pipeline against the user's actual column, so the cleaning is reproducible end-to-end.
