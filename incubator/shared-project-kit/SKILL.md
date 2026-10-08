---
name: shared-project-kit
description: Sets up a shared Claude project using the ideas42 Shared Project Kit — runs a guided context-gathering and interview flow, then generates the four kit pieces (custom instructions, project_overview.md, status.md, directory.md) personalized to the user's project and ready to upload, with an optional verify-and-correct pass. Use when the user wants to set up, create, build, stock, refresh, or verify a shared project, a shared project kit, a team Claude project, or the kit's knowledge files and custom instructions. Phase 1 when the user has a project but no kit; Phase 2 when they have existing kit files to verify, correct, or bring up to date. Not for personal or solo Claude project setup (use project-setup) and not for organizing local folders.
---

# Shared Project Kit Setup

Build the ideas42 Shared Project Kit for a team's shared Claude project: one lightweight kit separating what is stable (`project_overview.md`), what is current (`status.md`), what is read live (`directory.md`), and how Claude should behave (custom instructions). The kit prevents three failure modes: context resets, snapshot aging, and trapped decisions.

Final package: custom instructions (paste-ready) + three knowledge files (upload-ready) + the Drive-sync decision + an install checklist.

## Workflow map

Phases are independent entry points. Route based on what the user already has in hand.

| Phase | Use when... | Output | User-side next step |
|---|---|---|---|
| 1. Build a new kit | User has a project (rich or thin context) but no kit | Four personalized kit pieces + install checklist | Install in the shared project, run one test question |
| 2. Verify / refresh an existing kit | User has kit files (uploaded, on disk, or in a live project) to check, correct, or update | Verification review + corrected files | Re-upload the changed files |

## Pre-flight: load this skill before any user-facing action

When this skill triggers, read this file and the relevant reference **before** any user-facing action — including `AskUserQuestion`, scoping questions, or connector calls. The interview has its own structured question bank and render flow that should shape the first response; generic questions composed before reading the skill frame the work wrong and get re-asked later.

Concretely:

1. Read this `SKILL.md` first. For Phase 1, also read `references/interview-guide.md` and `references/intake-forms.md` before asking anything. For Phase 2, read `references/verify-and-deliver.md` first.
2. Your first response should either (a) start the Phase 1 flow at Step 1, or (b) ask a phase-routing question — not a generic "what format do you want?" question.
3. If you find yourself drafting an `AskUserQuestion` before reading the references, stop and read them first.

## Phase routing

| User has... | Start at | Ask before proceeding? |
|---|---|---|
| A project and wants a kit (new shared project, "set up the kit") | Phase 1, Step 1 | No — begin the flow |
| A project plus existing context files or a connected folder | Phase 1 — gathering will absorb what exists | No |
| Existing kit files they want checked, corrected, or refreshed | Phase 2 | Only if files are unclear |
| A request for a personal / solo Claude project | Hand off to `project-setup` | Yes — confirm it's solo, then hand off |
| A request for blank templates only | Off-ramp (user-invoked) | Confirm once, then provide templates |

Ambiguous opening (e.g., "help me with our project setup" with kit-like files attached)? Confirm the phase via one `AskUserQuestion` before any scoping question.

## Phase 1: Build a new kit

Copy this checklist and keep it updated across the conversation; open each working message with a one-line orientation ("Step 3 of 6 — a few questions I couldn't answer from your files").

- [ ] Step 1: Scope — read what's connected, confirm project identity and freshness owner, detect any existing kit
- [ ] Step 2: Gather — full read of folder files and connectors, read-only, permissioned
- [ ] Step 3: Interview — announce findings, ask only the gaps, batched
- [ ] Step 4: Generate — four files from the templates
- [ ] Step 5: Verify and correct — offer once; user may skip
- [ ] Step 6: Deliver — files + install checklist + freshness owner

**Step 1 — Scope.** *Gather-first when connected:* if a folder is connected or any context source is already visible, do a lightweight read of what's there (existing kit, context files, obvious project identity) before rendering Form A. Then run one structured question round (render per `references/intake-forms.md`, Form A) that **confirms what you saw and asks only what's missing** — drop the "what exists already" question for anything already visible; keep project name and freshness owner. When nothing is connected, run Form A cold. If the read (or the user) reveals an existing kit to check → switch to Phase 2; before committing to a new-kit build, confirm no kit already exists in the folder, `03_Deliverables`, or uploads.

**Step 2 — Gather.** Complete the read: collect everything that already exists before asking anyone anything. Source order and rules: `references/interview-guide.md`. Hard rules: connectors read-only; ask before each new system; record IDs as you go; log unknowns as `[VERIFY]` candidates; if content looks like PII, stop and flag rather than reading further; if you find credentials, flag their existence to the user and never reproduce or copy the value.

**Step 3 — Interview.** Announce what you gathered (3–5 plain bullets), then ask only the remaining question-bank items (`references/interview-guide.md`), rendered per `references/intake-forms.md` (Form B), batched into at most two rounds. Always include the Drive-sync decision with both caveats.

**Step 4 — Generate.** Fill the four templates in `references/templates.md`. Rules: behavior in instructions, content in files; `status.md` wins conflicts and the instructions say so; `directory.md` is pointers only, with `↳ Drive-synced into project Files — read there by default` on synced entries; every fact traces to a source or an answer; unknowns stay `[VERIFY]`; no PII or credentials; fill only what you can answer confidently.

**Step 5 — Verify and correct.** Offer once, in one sentence. Protocol: `references/verify-and-deliver.md`. The user may skip; note the skip in the wrap-up.

**Step 6 — Deliver.** Render and hand off per `references/verify-and-deliver.md`: real linked files when a workspace folder exists, tabbed copy-ready widget or fenced blocks otherwise, then the install checklist, freshness owner, and one test question.

## Phase 2: Verify / refresh an existing kit

Inventory the kit files the user provided or pointed to, then run the verification protocol in `references/verify-and-deliver.md` (claim extraction → source check → compact Confirmed / Unconfirmed / Discrepant review → batch corrections). Regenerate only the files that changed; update their "Last updated" lines; deliver per the same delivery rules. If the kit is missing one of the four pieces, offer to generate the missing piece via the Phase 1 templates rather than silently restructuring what exists.

## Workflow discipline

Claude's role is to execute this flow, not to decide whether it applies. Do not skip gathering because the user seems in a hurry; do not merge or rename the four-file anatomy because the project seems small; do not skip the verify offer; do not replace structured generation with an inline summary of "what your kit could say."

Rationalization audit — before any deviation, answer yes to this with a literal quote or don't deviate: *Did the user, in a direct chat message in this conversation, explicitly ask in plain language to skip or change this step?* A selection from an `AskUserQuestion` menu you authored does not count. "This can be quick" is not insistence — confirm before scaling down.

**Off-ramps (user-invoked only):** blank templates without the flow ("just give me the templates"); a solo project (hand off to `project-setup`); skipping the verify pass (designed-in — the offer is skippable). If a request looks borderline, ask; do not decide on the user's behalf.

## Common failure modes

- **Interrogation cascade** — asking questions one at a time, or asking for anything already gathered. Fix: gather first, announce-then-ask, batch into at most two rounds.
- **Padding thin context** — inventing stakeholders, dates, goals, or IDs to make a sparse kit look complete. Fix: `[VERIFY]` placeholders plus a plain statement of which sections are placeholders.
- **Structure improvisation** — collapsing status into the overview, dropping the directory, or inventing a fifth file because the project "doesn't need all four." The anatomy is fixed; sections within files flex.
- **Taxonomy leak** — user-facing text mentioning "Step 4," "per the template," reference file names, or this skill's structure. Users see project language only.
- **Menu laundering** — treating the user's pick from a question you composed as an independent request to skip part of the flow. Re-read the rationalization audit.

## Detailed instructions

Read only the file needed for the current step:

- Gathering rules + interview question bank: `references/interview-guide.md`
- Form rendering (widget → AskUserQuestion → inline): `references/intake-forms.md`
- The four templates + filling rules: `references/templates.md`
- Verification protocol, delivery rules, install checklist: `references/verify-and-deliver.md`

## Core principles

- Keep the user oriented: which step they are in, what you are producing, and what they need to do next.
- Guided beats thorough-feeling: minimum user burden, maximum reuse of what already exists.
- Never fabricate; make uncertainty visible with `[VERIFY]` rather than smoothing it away.
- The kit is a means: good enough to start beats complete, and a named freshness owner beats a perfect first draft.
- ideas42 voice throughout: team members (never staff or employees), behavioral science, Oxford comma, American English.
- Canonical pattern source: the SBNC kit and `Project Management/SHARED_PROJECT_KIT_SETUP.md`; this skill's templates are self-contained copies, so never require access to those files to run.
