# Verify-and-Correct Pass and Delivery

## When this runs

- **After generating a new kit** (Step 5): always offer it in one sentence — "Want a quick verification pass before you upload? I'll check every fact against its source and flag anything shaky." The user may skip it.
- **On an existing kit** (entry from Step 1): the user uploaded or pointed to kit files they want checked or refreshed. Run the same protocol against the current files, then regenerate only what changed.

## Verification protocol

1. Re-read each generated (or existing) file and extract its checkable claims: names, roles, dates, phases, IDs, decisions, guardrails.
2. For each claim, identify its source: a gathered document, a connector record, or the user's interview answer. With permission, re-check IDs against the live system (does the Drive file open, does the Asana GID resolve).
3. Classify each claim: **Confirmed** (source found and matches), **Unconfirmed** (no source — interview-only or `[VERIFY]`), or **Discrepant** (source conflicts with the draft).
4. Present one compact review — a table or elicitation widget, not a per-item interrogation:

| File | Claim | Status | Suggested fix |
|---|---|---|---|
| directory.md | Asana GID [x] | Discrepant | Replace with [y] (from live Asana) |
| project_overview.md | [Partner contact] role | Unconfirmed | Confirm or keep `[VERIFY]` |

Show Discrepant and Unconfirmed items only; report the Confirmed count in one line. Offer batch actions: "apply all suggested fixes," "keep all `[VERIFY]` flags," or per-row correction.

5. Apply the user's corrections, update each touched file's "Last updated" line, and summarize what changed in one or two sentences.

Rules: never silently "fix" a discrepancy in favor of the draft — the live source or the user decides; never resolve an Unconfirmed item by inventing a value; if more than about 10 items surface, group them by file and resolve file by file.

## Delivery

Render the four pieces with the lightest available format, in upload order (instructions first):

1. **Workspace folder available (Cowork) — preferred.** Write four real files and link them; do not paste contents inline. Suggest saving to the project's `01_Context/` (or a `chat-project-kit/` subfolder) if the project follows the six-folder system.
2. **`mcp__visualize__show_widget` available — fallback.** Render a tabbed copy-ready widget: one tab per piece, copy-to-clipboard on each.
3. **Otherwise — final fallback.** Four clearly separated fenced Markdown blocks, each preceded by a one-line label naming the destination ("Paste into Custom Instructions field" / "Upload as project_overview.md" / …).

Never expose internal step names, this skill's structure, or phrases like "per the template." Delivery sections are destination-named ("Custom instructions," "Knowledge files"), not step-numbered.

## Standard wrap-up

End the session with: a one-line summary of what was produced; the files or blocks; the install checklist below; the named freshness owner and refresh moment; and re-invocation language — "When the project changes phase or you want the kit checked, ask me to *verify the shared project kit* and I'll run the review pass." If the user skipped the verify pass, note that in one clause, without pressure.

Close with this checklist, addressed to the user:

1. Paste the custom instructions into the project's Custom Instructions field.
2. Upload the three knowledge files (`project_overview.md`, `status.md`, `directory.md`).
3. Add the Drive-synced file(s) to project Files from Drive (reminder: text-only processing; every member needs Drive access).
4. Connect the relevant connectors (Google Drive, Asana, Miro, Notion) in the project.
5. Test with one real project question — for example, "what needs a decision before the next check-in?" — and confirm Claude reads status first and follows pointers.
6. Confirm the freshness owner and the weekly refresh moment (usually right after a standing check-in).
