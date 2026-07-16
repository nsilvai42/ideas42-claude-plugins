# Phase 1 — Scoping

## The dimensions

| Dimension | What it answers | Default strategy |
|---|---|---|
| Artifact | What is being reviewed: repo path, file set, URL, or an uploaded file (doc/deck/PDF) | Infer from project context files and the conversation; offer an upload/paste slot for anything not on disk |
| Sections | The artifact's natural units of review (pages, tabs, slides, chapters) | Derive from the file tree or document structure; show as a pre-filled list the user prunes |
| Canonical reference | Which existing section/page sets the quality bar that others should match | **Cannot be defaulted silently.** Propose the most polished section and ask the user to confirm |
| Audience & milestone | Who the artifact serves, and the event the review gates (launch / stakeholder review / publication / next iteration) | Infer audience from project docs; milestone usually needs the user |
| Focus question | The owner's #1 concern, in their words (e.g., "make tab set B match tab set A's styling") | Pre-fill from the triggering message |
| Severity bar | What counts as launch-critical for this milestone | Default: visible breakage, placeholder content, dead primary CTAs, trust damage |
| Out of scope | Files or concerns to leave alone (e.g., "don't touch the hand-coded canonicals") | Pre-fill from project conventions |

## Highly preferred: structured elicitation widget

If the `visualize` MCP is available, gather all dimensions in **one** form:

1. Call `mcp__visualize__read_me` with `modules: ["elicitation"]` to load the widget schema. Do this before the first `show_widget` call.
2. Render a single elicitation widget with one field per dimension, **pre-filled** with everything Pre-flight inferred. State defaults in the form copy so the user edits rather than answers cold. Use multi-select pills for Sections and Out-of-scope (user prunes, doesn't type). Put a recommendation at every point of decision.
3. Include an artifact slot: a file-upload / path / URL field for users whose artifact isn't already in the workspace. If a file is uploaded, re-derive Sections from it before Phase 2.
4. On submit, restate the confirmed scope in one short block and proceed.

Pre-filling is the point. A blank form is the placeholder problem with better styling; a pre-filled form is a 20-second confirmation.

## Worked example

Scoping form for a real run — reviewing an internal HTML hub's "Start Here" launch content. This is the shape to aim for (field labels, pre-fill, stated defaults, recommendation at the decision point):

> **Review Council — confirm scope** *(everything below is pre-filled from your project files; edit anything that's wrong)*
>
> **1. Artifact** — `02_Working/repo-audit-merge/cards/start-here/` (8 HTML pages, found via REPO-MAP.md)
> *Or upload / paste a path or URL if this isn't it:* [ upload / text field ]
>
> **2. Sections to review** *(prune the pills that don't apply)*
> [SP Overview] [SP Prompts] [SP Projects] [SP Skills] [MCY Overview] [MCY Custom Instructions] [MCY Memory] [MCY Writing Styles]
>
> **3. Canonical reference — which page is the quality bar?** *(Recommended: SP Prompts — it shipped through your polish pass and has the richest treatment. Confirm or pick another.)*
> ( • SP Prompts ) ( SP Overview ) ( other: ___ )
>
> **4. Audience & milestone**
> Audience: `ideas42 staff, mostly non-technical, time-pressed, some AI-skeptical` *(from CLAUDE.md)*
> Milestone this review gates: ( • Friday Jun 12 deploy ) ( stakeholder review ) ( next iteration ) ( other: ___ )
>
> **5. Focus question** *(pre-filled from your request — edit freely)*
> `Bring Make Claude Yours tabs up to canonical Starter Pack styling wherever the same element exists.`
>
> **6. Severity bar for "launch-critical"** *(default shown; edit if your bar differs)*
> `Visible placeholder content, broken/dead primary CTAs, state bugs visible on first paint, conflicting navigation.`
>
> **7. Out of scope** *(prune or add)*
> [Hand-coded canonical cards outside start-here] [Component library /library/] [Deploy/branch workflow]

Submitting this form replaces what was previously a page of unfilled `[INSERT ARTIFACT NAME]` placeholders.

## Fallback: AskUserQuestion

Without `visualize`, collect only the dimensions Pre-flight could NOT infer, in one `AskUserQuestion` call (≤4 questions, multi-select where natural). Canonical reference and milestone are almost always in that set. State the inferred values for everything else in the same message so the user can object.

## Handling uploaded artifacts

If the user uploads the artifact (doc, deck, PDF, zip):

- Derive Sections from its structure (headings, slides, pages) and restate them for confirmation.
- "Rendered screenshots" in Phase 2 means opening the file's pages/slides visually where tooling allows, not just extracting text.
- Citations in findings become `page/slide/section` references instead of `file:line`.
