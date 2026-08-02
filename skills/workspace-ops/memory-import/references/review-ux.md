# Review UX

How to present the bounced set (conflicts + items needing explicit confirmation) to the user. The goal is single-surface, low-friction review with progress visibility and partial completion as a real outcome.

## Format defaults

In priority order:

1. **Interactive HTML form** — primary surface for >5 decisions. Single page, one card per decision, inline radios/dropdowns, free-text fields where useful, export-to-markdown button at the end.
2. **Word doc with comments** — fine for ≤5 decisions where prose context matters more than throughput.
3. **xlsx** — only when the data is genuinely tabular and the user already lives in spreadsheets. Multi-tab spreadsheets are high-friction for review.
4. **Markdown** — never the primary review surface. Reference companion only.

If the bounced set is ≤5 items, drop the form entirely and ask inline in chat, one item at a time. The form's overhead isn't worth it at low volume.

## Granularity defaults

Within the HTML form:

- **Card-at-a-time.** One decision visible at a time. Keyboard shortcuts: ← drop, → keep, ↑ skip.
- **Category-level batch.** Where items share a category (e.g., stakeholders for one project), offer a single batch action: "approve all," "redact all names," "skip this category."
- **Source-confidence batch.** Surface a header like "12 items labeled `inferred` — review individually, or auto-confirm all." Default is per-item, but the batch is one click away.

## Required UI elements

Every review surface must include:

- **Progress indicator** (e.g., "12 of 47 decisions").
- **"Stop and use what I've marked so far" button**, present on every section. Partial completion is a first-class outcome — what's marked imports, the rest is dropped.
- **Merge-target field** wherever "merge with another" is an option. A bare "merge" choice with no destination is a dead-end.
- **Export-to-markdown** (or copyable summary) at the end so the user can audit what they decided.

## Anti-patterns

Things to actively avoid (each one was a real failure mode):

- Per-item review with no batch escape hatch.
- Markdown templates as the working review surface — fine to read, fiddly to mark up.
- Multi-tab xlsx for non-tabular review data.
- "Merge with another" with no merge-target field.
- Asking the user to review items the source already labeled as `saved memory`.
- 80-decision forms with no skip-rest button.
