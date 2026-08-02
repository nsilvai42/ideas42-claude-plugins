# Correction Workflow

Use this reference in Phase 3 when the user returns with verified results, a verified Citation Ledger, correction notes, or verifier output that must be applied before synthesis.

## Contents

1. When to use this file
2. Normalize verified results
3. File safety rule
4. Apply corrections surgically
5. Create Corrections Applied changelog
6. Produce corrected source reports / notes
7. Update the Citation Ledger
8. Validate ledger stage
9. Claude QA pass
10. Partial or narrative-only verifier output
11. Do-not-proceed gates

## When to use this file

Read this file before synthesis when any of these are true:

- the user provides a verified ledger with [P] or [X] rows
- the user provides narrative verification output instead of an updated ledger
- the user provides correction notes that need to be applied to reports
- the user asks to “apply these corrections”
- the user asks for final synthesis but the research reports have not yet been corrected

Do not read this file when the user provides already-corrected reports and a final ledger with no unresolved correction work.

This workflow usually handles up to 5 research reports, matching the maximum number of Phase 1 research prompts. If the user provides more than 5 reports, batch them or ask which 5 are highest priority before applying corrections.

## Normalize verified results

Before applying corrections, make sure verification results are represented in the Citation Ledger structure.

For each claim row, ensure:

- `Verified` contains [C], [P], [U], or [X]
- `Verification Notes` explains non-[C] rows
- `Correction` is filled for [P] and [X] rows
- cross-report inconsistency resolutions are captured when available

If an `.xlsx` ledger is available, run `scripts/validate_ledger.py --stage verified` after normalizing verifier output. Fix missing corrections or invalid verification codes before applying corrections.

Verification codes:

| Code | Meaning | Handling |
|---|---|---|
| [C] Confirmed | Source exists and supports the claim as stated | Preserve claim exactly |
| [P] Partially confirmed | Source exists but characterization is slightly off | Apply corrected wording from Correction column |
| [U] Unconfirmed | Source or claim cannot be verified | Preserve only if needed; visibly flag as unverified |
| [X] Corrected | Claim is inaccurate | Replace with corrected wording from Correction column |

If [P] or [X] rows are missing correction text, pause and ask for the specific missing corrections or generate a targeted verification follow-up prompt.

### Normalize non-canonical verifier output

Verifiers (Perplexity, fresh Claude chats, third-party tools) often return shapes that do not match the canonical ledger exactly. Normalize before applying corrections.

Common variants to handle:

- **Lower-case CSV column names** — verifiers commonly return `claim_id`, `claim_text`, `verification_status`, `correction_note` instead of `Claim ID`, `Claim`, `Verified`, `Correction`. Map to the canonical Title-Case ledger keys.
- **Status vocabulary mismatch** — verifiers commonly return statuses like `verified | partially_verified | contradicted | unsupported` instead of the canonical `[C] | [P] | [U] | [X]` codes. Use this default mapping unless the verifier's output makes a different mapping clearer:

  | Verifier status | Default ledger code | When to use a different code |
  |---|---|---|
  | `verified` | `[C]` | — |
  | `partially_verified` / `partial` | `[P]` | If the verifier's correction note shows the source materially contradicts the claim, escalate to `[X]`. |
  | `contradicted` | `[X]` | — |
  | `unsupported` | `[X]` | If the source could not be located at all (rather than located and not supportive), use `[U]` instead. The two read similarly but mean different things in synthesis. |
  | `unverified` / `not_found` / `cannot_locate` | `[U]` | — |

- **Free-form narrative-only verification** — see "Partial or narrative-only verifier output" below.
- **Extra columns** — verifiers sometimes add columns like `evidence_strength`, `include_in_synthesis`, or `confidence`. Preserve these in the ledger as extra columns; do not drop signal. Map `include_in_synthesis = no` rows to `[X]` or `[U]` if the verifier did not give an explicit verification status.

After normalizing, the ledger should pass `scripts/validate_ledger.py --stage verified`. If validation fails, fix the schema before applying corrections.

## File safety rule

Never overwrite source files.

Do not edit the user’s original research outputs, uploaded reports, uploaded ledgers, or source files directly. Always create new files alongside originals.

Use filename patterns such as:

```text
[Topic] — R1 (Corrected).md
[Topic] — R2 (Corrected).md
[Topic] — R3 (Corrected).md
[Topic] — R4 (Corrected).md
[Topic] — R5 (Corrected).md
[Topic] — Corrections Applied.md
[Topic] — Citation Ledger (Final).xlsx
```

## Apply corrections surgically

Apply only corrections specified by the verified ledger or verifier output.

Rules:

- Preserve [C] claims exactly.
- Replace [P] and [X] claims with the Correction column contents.
- Preserve [U] claims only when needed and keep them visibly flagged as unverified.
- Do not re-research or rewrite anything that was not flagged.
- Do not smooth over contradictions unless the verified ledger resolves them.
- Keep original report structure where possible.

When corrections arrived pre-specified, summarize in one line and proceed:

```markdown
Proceeding with the [N] corrections you specified.
```

Do not ask “do you want me to go ahead?” when the verifier output already includes correction text.

## Create Corrections Applied changelog

Create a new changelog file when any [P] or [X] corrections exist.

Filename:

```text
[Topic] — Corrections Applied.md
```

Template:

```markdown
# Corrections Applied: [Topic]

| Claim ID | Verified code | Original text | Corrected text | Reason |
|---|---|---|---|---|
| [R1-C01] | [P] | [original] | [correction] | [verification note] |
```

Include one row per flagged claim.

## Produce corrected source reports / notes

When original report text is available, write one corrected file per research report, usually up to 5 reports.

Filename pattern:

```text
[Topic] — R1 (Corrected).md
[Topic] — R2 (Corrected).md
[Topic] — R3 (Corrected).md
```

**Rationale.** Downstream tools such as NotebookLM cannot infer that the ledger corrects the reports. The corrected source report is the self-contained artifact that downstream re-ingest sees. It is a contract: if it claims to be corrected, every applicable correction must appear inside that file, full stop. Corrections that exist only in a separate cross-document changelog do not count as applied to the source report.

### Two-pass workflow (default)

Use this two-pass workflow as the documented default for producing corrected source reports. It scales linearly in main-thread tokens, preserves provenance by anchoring corrections to the original source text, and avoids the single-context overflow risk of regenerating full corrected text for ≥3 reports.

**Pass 1 — Inline targeted substitution.** For every [P] and [X] row in the verified ledger, locate the matching anchor passage in the original source report (verbatim substring match against the claim text or its closest unique fragment is the default; light fuzzy matching for typos / whitespace differences is acceptable; do not match across paragraph boundaries). Replace the matched anchor with the Correction column contents. Preserve [C] claims verbatim. Preserve [U] claims only if needed, visibly flagged as unverified. Do not rewrite unaffected prose except as needed to make a correction grammatically coherent. Do not silently remove contradictions; resolve only if the verifier resolved them.

`scripts/apply_corrections.py` automates this pass when available — it reads the verified ledger and the original report, applies the substitutions, and emits the per-document Corrections appendix described below for any [P] / [X] flag whose anchor it could not safely match. If the script cannot be run, do the same work inline.

**Pass 2 — Per-document Corrections appendix.** For every [P] / [X] flag the inline pass could not safely anchor in this report's text, append a structured "Corrections appendix" entry at the end of that same corrected source report. The appendix is part of the corrected-source-report file; it is not optional and it is not satisfied by the cross-document changelog.

Appendix template, appended to each corrected source report after the original prose:

```markdown
---

## Corrections appendix

The following corrections from the verified Citation Ledger apply to this report but could not be safely anchored to a specific passage in the original text. They are included here so that this corrected report remains a self-contained record of all corrections applied.

| Claim ID | Verified code | Location reference | Correction | Source |
|---|---|---|---|---|
| [R1-C12] | [P] | [section / heading / closest verbatim quote from the source] | [corrected wording from the ledger Correction column] | [verified source from the ledger] |
```

One row per unanchored [P] or [X] flag. `Location reference` should give the reader the closest reasonable pointer — section heading + a short verbatim quote is usually enough.

**Rule:** every [P] / [X] flag for a given report must end up either inline (Pass 1) or in that report's appendix (Pass 2). A flag that lives only in the cross-document Corrections Applied changelog does not satisfy this rule.

### Whole-document regeneration (fallback only)

Whole-document regeneration — rewriting the entire corrected report from scratch — is the original mechanism but should now be treated as a fallback, not the default. Use it only when:

- the report is short enough that regeneration costs are negligible
- the corrections are dense enough that targeted substitution would touch most of the prose anyway
- the original source text was provided in a form where verbatim anchor matching is unreliable (for example, transcribed PDF with OCR drift)

When regenerating, the same correction rules apply: swap [P] / [X] claims with Correction column contents, preserve [C] claims verbatim, preserve [U] claims only if needed and visibly flagged, do not silently rewrite unaffected prose. The Corrections appendix is still required for any flag that could not be cleanly placed during regeneration.

### Cross-document changelog stays as the audit trail

The `[Topic] — Corrections Applied.md` changelog file (see "Create Corrections Applied changelog" above) and the Corrections Applied tab in the final ledger remain useful as the analyst's audit trail and as a cross-document index. They are auxiliary records, not primary ones. The corrected source report is still the primary record of corrections to that source.

## Update the Citation Ledger

Update or create a final ledger that includes:

- verification codes
- verification notes
- corrections for [P] and [X] rows
- Corrections Applied tab populated
- cross-report inconsistency resolutions, when available
- Claude QA results for corrected rows

Preserve all verified [C] claims exactly.

If a user-uploaded ledger was provided, do not overwrite it. Save a new file:

```text
[Topic] — Citation Ledger (Final).xlsx
```

If `.xlsx` generation is unavailable, provide a structured Markdown fallback and state that it should be converted to `.xlsx` for archival use.

## Validate ledger stage

If the environment supports scripts, validate the ledger at each relevant checkpoint:

```bash
python scripts/validate_ledger.py "[Topic] — Citation Ledger.xlsx" --stage verified
python scripts/validate_ledger.py "[Topic] — Citation Ledger (Final).xlsx" --stage final
```

Use `--stage verified` after normalizing external verification output and before applying corrections. Use `--stage final` after corrections and Claude QA are complete.

Fix validation errors before synthesis unless they are explicitly documented as unresolved. Validation errors are not cosmetic; they usually mean the audit trail is broken.

## Claude QA pass

After applying corrections, re-scan corrected content against the ledger.

For every [P] and [X] row:

1. Verify the corrected output contains the Correction column text or an equivalent faithful correction.
2. Confirm the original inaccurate wording is no longer presented as verified.
3. Record the result in the `Claude QA` column:
   - `✓` if the correction is applied correctly
   - `✗` plus a note if the correction is missing, incomplete, or inconsistent
4. Re-apply corrections until all [P] and [X] rows pass QA or are explicitly flagged as unresolved.

Do not proceed to final synthesis while known correction mismatches remain unresolved.

## Partial or narrative-only verifier output

If the user returns with pasted text instead of a verified ledger:

1. Map the narrative back to Claim IDs.
2. Fill `Verified`, `Verification Notes`, and `Correction` wherever the narrative provides enough information.
3. Identify rows that remain unverified.
4. Offer to generate a targeted follow-up verification prompt for the missing rows.

If the verifier returned more than requested, such as a pre-filled Corrections Applied tab, preserve it and reshape it to the standard schema.

Extra signal is useful. Do not discard it just because it does not match the expected format.

## Do-not-proceed gates

Do not synthesize final evidence when:

- [P] or [X] rows lack correction text
- corrected reports contradict the final ledger
- Claude QA contains unresolved ✗ notes
- more than 30% of material claims are [U] or [X] and the user has not accepted the risk
- major cross-report inconsistencies remain unresolved and are central to the research question
- `scripts/validate_ledger.py --stage final` fails and the issue is not explicitly documented as unresolved

When a gate blocks synthesis, explain the issue and offer the smallest next step: targeted verification, narrowed synthesis, or re-running research.

