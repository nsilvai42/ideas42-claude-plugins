---
name: review-council
description: Run structured multi-reviewer QA on docs, sites, decks, emails, prototypes, and launch artifacts, with evidence-backed findings.
---

# Review Council

Evaluate an artifact through five phases: **Scope → Evidence → Council → Verification → Synthesis & Delivery**. The council's job is to identify the highest-value improvements, risks, and fixes — not to rewrite the artifact.

Three design choices define this skill, each fixing a documented failure mode:

1. **Scoping is structured and pre-filled, not placeholder-driven.** Asking the user to fill `[ARTIFACT NAME]`-style blanks fails; instead, infer everything you can from project context, then confirm via one elicitation widget.
2. **Every factual claim is verified before it ships.** Reviewers confidently assert broken links and missing files that turn out to exist. No claim about a link, file, selector, or behavior appears in the final report unchecked.
3. **Findings cite evidence or they're rejected.** "The hierarchy feels off" is not a finding. `custom-instructions/index.html:91 — button has class 'on' while line 121's panel has 'is-active'` is.

## Phase map

| Phase | Output | Reference to read first |
|---|---|---|
| 1. Scope | Confirmed scope (artifact, sections, canonical reference, audience, severity bar) | `references/scoping.md` |
| 2. Evidence | File inventory, project QA-script results, rendered screenshots | — (procedure below) |
| 3. Council | Three independent reviewer reports with cited findings | `references/reviewer-prompts.md` |
| 4. Verification | Verified/rejected claim log | — (procedure below) |
| 5. Synthesis & Delivery | Final report with vote labels, saved into the project | `references/report-template.md` |

## Pre-flight

Read this file and `references/scoping.md` **before** any user-facing question. The scoping reference defines which dimensions to gather and how; questions composed before reading it tend to be generic deliverable questions ("what format do you want?") that the workflow doesn't need.

Then gather context silently:

- Read the project's memory/context files if present: `CLAUDE.md`, anything like `01_Context/status.md`, `REPO-MAP.md`, project overview docs. These usually answer artifact location, audience, brand conventions, and what "canonical" means before the user has to.
- Locate the artifact's files (Glob/ls). Note natural sections.
- Note any project conventions, brand tokens, style anti-patterns, and terminology — these get injected verbatim into reviewer prompts in Phase 3. Convention-grounded reviewers produce sharply better findings than generic ones.

## Phase 1 — Scope

Follow `references/scoping.md`. In short: if the `visualize` MCP is available, call `available connector visualize__read_me` with `modules: ["elicitation"]`, then render **one** elicitation widget collecting all scoping dimensions at once — pre-filled with everything Pre-flight inferred, defaults stated in the form copy so the user prunes and confirms rather than types from scratch. The widget includes a slot for the artifact itself (upload, path, or URL) for users who haven't provided it.

The one dimension that cannot be defaulted: the **canonical reference** — the existing section, page, or example that sets the quality bar. Consistency review without a declared canon produces vague "pick one of these" advice; with one, every divergence has a direction. If the user doesn't know, propose the most polished section as canon and ask them to confirm.

If `visualize` is unavailable, gather the same dimensions with a single `ask the user a concise clarifying question` call (max 4 questions) — never a long conversational questionnaire.

Do not start Phase 2 until the user confirms scope. Do not re-scope mid-run unless the user asks.

**Non-interactive runs** (scheduled task, subagent, or test where no user can answer): save the pre-filled widget spec as a document alongside the eventual report, proceed with the stated defaults, and flag in the report header that scope was assumed, not confirmed.

## Phase 2 — Evidence

Build the ground truth the council will review against:

1. **Inventory.** List the in-scope files with sizes/line counts. Read them. For large shared assets (CSS, component libraries), read the sections that govern the in-scope artifact rather than the whole file.
2. **Run the project's own checks first.** If the repo has QA scripts (`check-links`, lint, build validation, tests), run them and record results. Their output is evidence reviewers must not contradict — a passing link check pre-empts "this internal page may 404" findings.
3. **Render and screenshot — mandatory when possible.** Source reading cannot settle how things actually look: compensating CSS can make broken markup render fine, and `!important` layers can make apparent inconsistencies moot. If a dev server is running, a build output exists, or the artifact is a document/deck that can be opened, capture screenshots of (a) the canonical reference and (b) the top and any visually complex region of each reviewed section, using browser tools or available viewers. Browser/screenshot tools are often deferred — search for and load them (e.g., via ToolSearch) before concluding rendering is impossible. If rendering truly is impossible, write one line in the final report's limitations: *"Reviewed in source only; rendered output not inspected."* Do not silently skip this step.
4. For styled artifacts: when reviewers will make claims about visual treatment, trace **which rule actually wins** (cascade, specificity, `!important`), not the first matching rule. Verify computed outcome, not source order.

## Phase 3 — Council

Spawn three reviewers, each independently covering every in-scope section:

- **Visual / Structural Design** — hierarchy, spacing, consistency, polish; for non-visual artifacts, structure, formatting, scanability.
- **UX / Behavioral** — clarity of next action, friction, cognitive load, drop-off and trust risks, interaction correctness (test the JS/interaction paths in source).
- **Content / Information Architecture** — relevance, concision, redundancy, jargon, terminology consistency, contradictions between sections, link quality.

Use parallel subagents when available (launch all three in one message); otherwise run each role inline, sequentially, as a prompt-to-self. Build each prompt from `references/reviewer-prompts.md`, injecting: the artifact context and audience, the file list, the canonical reference, project conventions/anti-patterns from Pre-flight, any leads you already noticed (marked "verify, don't take on faith"), and the citation rule below.

**Citation rule (non-negotiable, include in every reviewer prompt):** every finding names the exact file and line/selector/section, why it matters, a severity (launch-critical / high / nice-to-have), and a one-line concrete fix. Findings without all four get dropped in synthesis. Each reviewer ends with a Top 5. Tell reviewers the final report is capped (~250 lines total) so they write tight findings from the start rather than relying on compression at synthesis.

## Phase 4 — Verification (mandatory)

Reviewers err confidently. Before synthesis, extract every **checkable factual claim** from the three reports and check each one:

- "Page/file X doesn't exist or will 404" → `ls` / Glob / the repo's link checker.
- "Selector/class/function X is unstyled or unused" → grep the asset; trace the cascade.
- "Element renders wrong" → compare against the Phase 2 screenshots.
- "These two states/labels mismatch" → re-read both cited lines.

Log each claim as **Confirmed** or **Rejected (with evidence)**. Rejected claims are excluded from the report body and listed in a short "Verification notes" section — showing rejected claims is what makes the confirmed ones trustworthy. Subjective judgments (hierarchy, tone, density) don't need verification, but their citations must point at real lines.

## Phase 5 — Synthesis & Delivery

1. **Cross-section pass.** Compare design, UX, and content treatments *across* sections: where the same element appears twice with different treatment, name the canonical version (per the declared canon) and the fix. Render this as the consistency table in the report template.
2. **Vote labels, no staged debate.** Do not roleplay reviewer arguments — it adds length, not insight. Instead, tag every recommendation with reviewer agreement: **Unanimous** / **Majority** / **Mixed Opinions — owner call** / **Rejected**. Where reviewers genuinely conflict (e.g., consistency vs. preserving a signature page), present both positions in two sentences under a *Mixed* label and leave the call to the owner.
3. **Write the report** using `references/report-template.md` exactly: Launch-Critical → High-Value → Nice-to-Have → Cross-Section Consistency Fixes (table) → Top 10 by impact ÷ effort → Verification notes. Cap per-item length at ~3 sentences; the raw council output is typically 3× too long and the template is the compression.
4. **Deliver into the project's workflow.** Save the report where the project keeps audit docs (e.g., `01_Context/` in six-folder projects) with a dated filename; present the file; update the project's status/tasks doc if one exists. In non-interactive or test runs, save to the designated outputs location instead and skip the status-doc update. Then offer — don't just perform — to apply the trivial fixes (anything under ~5 lines of diff) on the project's working branch, batched, with the owner's approval. Identification is the council's job; cheap fixes are a courtesy follow-up.

## Principles

- **The council identifies; the owner decides.** Never rewrite the artifact during the review. Genuine taste calls (heading conventions, section order) ship as *Mixed — owner call*, not as directives.
- **Severity is about the artifact's next milestone.** "Launch-critical" means visible breakage or trust damage at the event named in scope (launch, stakeholder review, publication) — not "I feel strongly."
- **Impact ÷ effort ranks the Top 10.** A one-line class fix that repairs a visible bug outranks a content rewrite of equal importance.
- **Bounded output beats complete output.** If the report exceeds ~250 lines, cut nice-to-haves before cutting evidence.
