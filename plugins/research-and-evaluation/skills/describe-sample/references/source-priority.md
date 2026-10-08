# Source priority handling

When a dataset has multiple columns capturing the same underlying construct (e.g., a Qualtrics column and a Prolific column for income), the skill must decide which is primary. The default behavior is to **always ask the user** — never silently pick.

## Detecting source overlap

Heuristics for identifying same-construct columns from different sources:

| Signal | Example |
|---|---|
| Source prefix + matching root | `qualtrics_income` / `prolific_income` |
| Source suffix + matching root | `income_q` / `income_p` |
| Differ only by capitalization or punctuation | `Income` / `income`, `Education_2` / `education` |
| Same canonical values present in both | Two columns both have `{Female, Male, Prefer not to say}` |
| Documented in a column dictionary or handoff doc as duplicate-of |

When detected, do NOT auto-merge or auto-deduplicate. Surface to the user via Form 4 (`elicitation-templates.md`).

## What to show the user

For each overlap:
- The two (or N) column names
- Non-null count for each
- The disagreement rate (% of rows where the values differ, computed only after normalizing for case/whitespace)
- For numeric overlap: distance metric (e.g., median absolute difference)
- A 3-row sample showing the disagreement

## What the user picks

User chooses one of:
1. **Use source A as primary** — copy column A values into a new `_primary` column; keep both originals
2. **Use source B as primary** — same, with B
3. **Reconcile** — define a merge rule (e.g., "use A unless A is null, then B"; "average them"; "take the more recent")
4. **Keep separate; report both** — don't pick; just show both in the outputs side-by-side

## Documenting the choice

The decision is logged in the transformation ledger with `decision_type: source_pick`. The "source convention" appears in the end-of-process summary so future analysts understand which source's values were used in downstream charts and tables.

## Common rationales to capture

If the user chose without explanation, ask why (in a short follow-up textarea) so it can go in the ledger. Common rationales:
- Study-time data is more current than signup data
- The "primary" source has fewer nulls
- The "primary" source uses study-relevant category labels
- Pre-registered analysis specifies the source
- Survey wave is more authoritative than a recruitment panel's metadata

## Disagreement reporting

In addition to the primary-source value, always preserve:
- Both original columns (don't drop)
- A derived `disagree_<construct>` boolean (1 if A != B after normalization)
- For numeric, a derived `<construct>_distance` numeric column

These let downstream sensitivity analyses filter on "agreement subsample" if desired.
