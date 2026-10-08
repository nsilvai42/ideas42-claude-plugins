# Open-Text Theme Coding Audit Template

Use when the original analysis used regex / keyword dictionaries / an LLM to tag open-text responses with themes (e.g., "concerns about refund", "pace/time pressure"), and downstream claims report theme counts or percentages.

## Default disposition (no audit run)

If no audit has been run, theme counts are **directional only**. The downstream prose must say "% of respondents whose response matched the [theme] keywords" or similar — not "% of respondents concerned about [theme]". Theme counts cannot be promoted to precise percentages until an audit completes.

## Audit inputs

- Raw text responses
- The theme dictionary or coding rule used (verbatim)
- A list of the themes whose counts are referenced downstream

## Audit procedure

For each theme used in a downstream claim:

1. Pull all responses tagged as this theme. Spot-check 20.
2. Pull 30 random responses *not* tagged as this theme. Check for false negatives.
3. Have a second coder independently tag the same 50 responses without seeing the first coder's tags.
4. Compute inter-rater reliability (% agreement; Cohen's κ if appropriate).

## Audit columns

| Column | Description |
|---|---|
| response_id | Stable ID |
| theme | The theme being audited |
| ai_tag | 1 if AI tagged this response with this theme, 0 otherwise |
| human_tag | 1 if human reviewer tags this response with this theme, 0 otherwise |
| disagreement_type | If ai ≠ human: false_positive / false_negative / boundary |
| reviewer_note | Free text |

## Reporting

| Threshold | Permitted downstream language |
|---|---|
| ≥ 90% agreement, κ ≥ 0.75 | Precise percentage: "23% of respondents raised refund-mechanic concerns." |
| 80–90% agreement, κ 0.6–0.75 | Approximate percentage with caveat: "About a quarter (~23%) raised refund-mechanic concerns, based on regex theme coding." |
| < 80% agreement or κ < 0.6 | Directional only: "Refund-mechanic concerns were a leading theme in open-ended responses." |
| No audit run | Directional only. |

## Output

A passing audit produces (a) the agreement scores per theme, (b) the dictionary changes (if any) needed before next use, and (c) explicit clearance for the precise-percentage language in the corrected outputs.
A failing audit means the downstream language stays directional and the master ledger marks those claims with status `Directional only`.
