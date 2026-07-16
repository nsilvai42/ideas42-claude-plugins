# Intake Form Rendering

**Purpose:** How to render elicitation forms in project-setup — Round 1 (project framing + context method) and Round 2 (conditional gather + project-specific questions).
**Use when:** You're about to ask the user a structured question — to capture project type / purpose / stage / context method (Round 1), or to gather context and fill remaining checklist items (Round 2).
**Not for:** What items to ask about in Round 2's project-specific section. The checklist (`references/checklist.md`) and per-type follow-ups (`references/project-types.md`) are the source of truth for content — this file only specifies render mode and field shape.

## Render mode, in order of preference

The same three-tier fallback applies to both Round 1 and Round 2. The inline-prose path on claude.ai (where the widget MCP isn't available) is a first-class render — most users see Round 1 there — not a degraded fallback. The inline path must mirror the form shape question-for-question; do not invent a different design for inline.

### 1. Form widget (preferred when available)

If `interactive elicitation tool` is available, render as one form. Before the first widget call, read the elicitation schema:

```
tool schema reader({ modules: ["elicitation"], platform: "desktop" })
```

Then call `interactive elicitation tool` with the elicitation module.

Pre-fill where the elicitation shell supports it. **Pills do NOT support pre-fill via initial markup** — `aria-pressed="true"` is the CSS hook the shell applies on click, not a way to mark initial state. Pills always render unpressed.

For inferred values that would have been a pre-press, surface them in chat **before** rendering the form, then let the user confirm or adjust by actively pressing in the form. Example: *"I'd guess your Sensitivity is 'partner confidentiality' and 'DSA constraints in force' based on the brief and the draft DSA — confirm or adjust in the form below."* This makes inference visible and editable, replacing the missing pre-press affordance.

Native HTML inputs DO support pre-fill: textareas accept text content between tags (`<textarea class="elicit-textarea" data-name="x">inferred text here</textarea>`), `<input type="text">` and `<input type="date">` accept `value=""`, `<input type="range">` accepts `value=""`. Use these for any field where the inferred value is text or a number.

Apply pre-fill aggressively to native HTML inputs across both rounds: Q2 (purpose) from the user's first message + visible upload excerpts; Round 2 connector-pointers from any pointer-shaped phrase in chat or brief; project-specific text fields (partner name, deliverable + timeline) from upload contents. The user can edit; an empty field when material exists is a UX miss, not a precaution.

### 2. structured-question interface (widget unavailable)

Use one `structured-question interface` block per logical group. Mirror the form's options, defaults, and inline definitions.

### 3. Inline (last resort, but first-class on claude.ai)

Bullet the questions in chat, mirroring the form's groups question-for-question. Do not redesign — the inline path is a faithful text version, not a parallel structure. State defaults and define unfamiliar terms inline.

## N/A pill exclusivity (shell support required)

Some multi-select pill groups in Round 2 (specifically Tone and Common work patterns) include a **Not applicable** pill that needs to behave exclusively — pressing it should deselect all other pills in the group, and pressing any other pill should deselect N/A. The elicitation shell does not currently enforce this exclusivity; `data-multi="true"` accepts any combination by default.

Until the shell supports per-group exclusivity, render the N/A pill with an inline marker in the label (e.g., `Not applicable [exclusive]`) so the user sees the intent, and apply a parse-time guard in the form-return handler: **if N/A is present in a group's selections alongside any other pick, drop the others and treat the group as N/A-only.** The parse-time guard is correctness-only — the user may briefly see both N/A and another pill pressed at once before submit. That UX gap is acceptable; the parse-time guard prevents downstream effects.

This is flagged as a shell-feature ask separately. A future framework version with native exclusivity support can drop the inline marker and the parse-time guard without re-spec'ing the field.

When inline-rendered (claude.ai-typical), make the exclusivity explicit in the prose: *"Pick any combination — or pick 'Not applicable' if the field doesn't fit this project (skip the others if so)."*

## Round 1 form — project framing + context method

The Round 1 flow is a single form — one round trip. **No "what I can see" preamble** — the form itself implies the boundary (we won't pull from connectors until you tell us how to gather context). Do not list visible uploads / connectors / chat-so-far before the questions.

### Form structure — 4 groups, ordered

Order matters. Project type goes first because it's the upstream decision driving everything downstream. Purpose is second so the type's meaning is concretized. Stage is third so it's framed against a known type. Context method is last because it depends on what kind of project we're scoping.

#### Group 1: Project type — `.elicit-pills` single-select (cards)

The upstream decision. What every other answer is interpreted against.

- **A reusable tool or workflow** *(recurring deliverables, templated analyses, automated audits)*
- **A time-bound engagement** *(defined scope, deliverables, end date — partner work, grants, RFPs, workstreams)*
- **An ongoing program or operation** *(recurring rhythm without a specific end date — internal program management, ops, communities of practice)*
- **A reference or knowledge hub** *(making a body of knowledge accessible — research archives, partner libraries, decision logs)*
- **Personal exploration or tracker** *(personal use, learning, individual workflow)*
- **Other / something else**

Each option carries the bracketed example phrasing inline so the user can pick without scrolling to a definitions section.

#### Group 2: Main purpose — `.elicit-textarea`

- **What is the project's main purpose?** *(Examples: "a project pilot workstream in the Calbright project," "an internal operations project," "a reusable workflow to draft summaries from meeting notes." Leave broad if you want a wide first-pass.)*

This field is the primary search-narrowing parameter for any connector pulls in Round 2. If left blank, Round 2 runs a conservative first-pass search and confirms scope with the user before deepening.

#### Group 3: Project stage — `.elicit-pills` single-select (type-agnostic)

- **Just starting / setting up**
- **Actively in progress**
- **In review or wrap-up**
- **Built and in use**
- **Other**

Stage is intentionally type-agnostic and intentionally lifecycle-only — it captures *where in the build → use → retire arc* the project is, not *how often the work fires*. The cadence axis (one-time / recurring / always-on) is captured separately by Round 2's `update_cadence` field, so stage labels don't need to carry that signal.

This matters most for project types where lifecycle and cadence are independently meaningful (reusable tools, ongoing programs, knowledge hubs, personal trackers). For these types, "Built and in use" is the lifecycle answer post-setup; the cadence answer lives in Round 2. For time-bound engagements, the cadence axis collapses (engagements are inherently one-shot), so only the lifecycle reading is alive — same labels, fewer axes in play.

(Future framework versions that support pills changing based on a sibling pill's selection should switch to type-conditioned stage options; until then, type-agnostic.)

#### Group 4: Context-collection method — `.elicit-pills` with `data-multi="true"`

- **Use my connectors** *(if any allowlisted connectors are visible to the session, list them inline in the prompt copy: "I can pull from your connected [Slack, Gmail, Drive, Asana, Notion, Calendar — capped at 8 displayed, +N more]." If no allowlisted connectors are visible, **omit this option entirely** — do not render an option the user can't act on.)*
- **Project files I'll upload** *(file picker affordance comes in Round 2; just naming the option here)*
- **Ask me questions in chat** *(no connectors, no uploads — just walk me through what you need)*

Form copy above the pills:

> *"How would you like me to gather your project's context? Pick any combination — connectors are fast for what's already digitized; uploads work for project briefs and reference docs; chat works when context lives in your head or you'd rather walk me through it."*

If Q4 returns empty, default to chat-questions automatically — never proceed to silent gathering.

### After the Round 1 form returns

Carry forward into Round 2:

1. **Project type** — drives type-specific follow-up questions (`references/project-types.md` per-type "Round-2 follow-up questions") and knowledge file template variants (`references/standard-files.md`).
2. **Purpose textarea** — search-narrowing parameter for any connector pulls.
3. **Stage** — feeds the project-overview / status framing.
4. **Context-method selections** — drives Round 2's conditional sections (which appear, which are hidden).

Inferences from any of the above should be announced in chat **before** rendering Round 2, so the user can confirm or adjust. Hold the announced-inference list in working memory so the Step 3 review table can flag mismatches.

## Round 2 form — conditional fields by Round 1 answer

Round 2 is a single conditional form. Sections appear / disappear based on Round 1 Q4 (context method). Universal sections appear regardless. Order: connector picker → upload affordance → audience → project-specific questions. Sequencing rationale: connectors first because they're the longest async (pull happens in parallel with the rest of the form filling), uploads next so the user can drop files while connectors run, audience and project-specific questions at the end where the user is already focused on their project.

### Conditional Section A — connector multi-select (only if "Use my connectors" was picked in Round 1 Q4)

- **`.elicit-pills` with `data-multi="true"`**: one pill per connector visible to the session, **filtered to the org-context allowlist** in `references/checklist.md`. Pills always render unpressed (per the pill-no-pre-fill rule above). At parse time: no pills pressed = pull from all listed sources; one or more pressed = pull only from those. Same key-absent-or-empty handling as the connector-pointers textarea below.

Form copy above the pills:

> *"Pick which connectors I should pull from. Leave all unselected to use every source above; press any to include only those."*

- **Connector pointers** — `.elicit-textarea` labeled: *"Anything specific to point me at? Project URLs, channel names, folder IDs, search terms — leave blank for a broad search. One pointer per line; prefix with the connector name if it helps, e.g., `Asana: project XYZ` or `Drive: /partners/calbright/`."*

The connector-pointers textarea is parsed by line — lines matching `Connector: pointer` (e.g., `Asana: https://app.asana.com/0/1234`) bind to that connector and take precedence over the purpose-textarea scope token there. Lines without a recognized connector prefix fall back to a global pointer applied to all selected connectors.

If the textarea key is absent from the form return string entirely (the user skipped it), treat it as empty — same handling. The elicitation shell drops skipped fields from the return string (no "(Skipped)" stub, no empty-string stub — just absent), so the parser must handle both "key absent" and "key present but empty."

### Conditional Section B — file upload affordance (only if "Project files I'll upload" was picked in Round 1 Q4)

- **`.elicit-files` upload affordance + paired `.elicit-textarea` fallback** (see "File upload" in the elicitation schema):
  - **Drop in any useful files** *(file picker — accepts PDFs, docs, images, etc. Allow multiple.)*
  - **Or describe what's relevant** *(textarea fallback for users pointing at uploads already attached to the chat).*

Suggest concrete examples inline below the upload control, **sourced from `references/project-types.md`'s per-type "Ask for (uploads)" list**. For example:
- Time-bound engagement: *"project briefs, kickoff decks, charters, theory of change docs, partner correspondence, prior status notes, DSA / IRB if applicable."*
- Reusable tool or workflow: *"examples of good output, templates, style guides, runtime references, machine-reference docs (like instructions written for an AI auditor)."*
- Ongoing program: *"operating manuals, recurring deliverable templates, stakeholder maps, past instances of the recurring deliverable, decision logs."*
- Reference / knowledge hub: *"existing knowledge corpus or sample, taxonomy / index / glossary, examples of typical lookup questions."*
- Personal exploration: *"whatever notes, links, or material you've gathered."*

Per-type inline suggestions concretize the upload prompt and produce better material. The current run that surfaced this had four PDFs upload-ready in seconds because the suggestions matched what the user already had.

### Universal Section C — audience

- **`.elicit-pills` multi-select**: who is the project for?
  - internal team
  - partner / client
  - funder
  - external audience
  - personal workflow

### Universal Section D — project-specific questions (sourced per type)

Pull from `references/project-types.md`'s per-type "Round-2 follow-up questions" subsection that matches the Round 1 project type. Examples:
- Reusable tool or workflow: who runs it / what triggers a run / output shape / inputs needed each time
- Time-bound engagement: partner or funder / deliverable + timeline / parent project (if workstream) / DSA or IRB constraints
- Ongoing program: cadence / recurring deliverables / team / standing decisions
- Reference / knowledge hub: organizing principle / who consults it / how it's kept current
- Personal exploration: what's being tracked / return cadence / what "done" looks like

Field types depend on the question — single-select pills for cadence and organizing-principle questions, textareas for partner names and free-text follow-ups. Use form widget native HTML inputs (textarea, text input, date input) where pre-fill from earlier signal is possible.

### Sensitivity / DSA, sensitive content (universal but conditional)

If the project type is time-bound engagement, ALWAYS include sensitivity / compliance pills in Round 2 even if no DSA upload is visible — partner work usually has at least one constraint and silent omission is dangerous.

- **`.elicit-pills` multi-select** (sensitivity / compliance):
  - vulnerable population *(minors, justice-involved, low-income, etc.)*
  - IRB-approved research
  - DSA *(data sharing agreement)* constraints in force
  - partner confidentiality
  - non-public data only
  - none

Always define DSA inline anywhere it appears — don't rely on the term being defined elsewhere in the form.

For other project types, include sensitivity pills only if any signal in uploads or connectors flagged a constraint. Otherwise it stays out of Round 2.

### Common work patterns (universal)

Framing sentence above the pills (wording varies by project type; pull the per-type variant from `references/project-types.md`'s "Round-2 work-patterns wording" line). Default if the type isn't listed: *"What kinds of work happen most often in this project?"*

- **`.elicit-pills` multi-select** (pick 2–4 — I'll narrow in chat if you pick more): drafting / research-synthesis / data-analysis / project-management / brainstorming / presentation-deck / review-feedback / stakeholder-comms / **Not applicable [exclusive]**

The framing sentence is essential, not optional — without it, the field's referent is ambiguous for project types where the tool's work is *meta* to its inputs (reusable tools producing content about other content; reference hubs summarizing other docs). For these types, "common work patterns" can mean either (a) the topics the tool's *inputs* cover, or (b) what the project's *tasks* directly do. The per-type framing sentence picks one referent so the user isn't forced to.

**Not applicable** is the last pill, exclusive (see "N/A pill exclusivity" above). When N/A is the only selection: suppress the work-patterns input from any FORMAT-line generation; the project gets no work-patterns-derived defaults. Especially relevant for domain-agnostic tools where the field's value is genuinely low (a prompt-optimization tool that operates on any topic; a reference hub spanning many domains).

If the user picks 5+ (other than N/A), follow up in chat: "Pick your top 3 — instructions optimized for everything optimize for nothing." The "(2–4 — I'll narrow in chat...)" copy in the field label sets the expectation; the chat follow-up enforces it.

### Tone (universal)

Framing sentence above the pills:

> *"This is the tone of Claude's responses **during** a project run — how Claude talks to you while you're working. The tone of artifacts Claude produces (prompts, drafts, reports) should be specified per-run or captured in your DO behaviors, not here."*

The framing sentence is essential, not optional. Without it, this field conflates two distinct surfaces — Claude's voice during the conversation vs. the voice baked into deliverables — and for projects whose deliverable is itself tonal (a tool that outputs prompts, templates, style-guide rewrites, voice samples), the user is forced to pick which surface to answer for. The framing sentence picks the meta-conversation surface; the deliverable-tone surface is handled elsewhere (per-run, or in DO behaviors).

- **`.elicit-pills` multi-select**, mark one as primary:
  - ideas42 brand voice *(use the `ideas42-brand` skill if installed; recommend installing if not)*
  - partner / client voice *(when deliverables ship under the partner's name)*
  - casual internal *(working drafts, team-only)*
  - formal *(funder, board, regulator)*
  - concise / scannable
  - highly polished
  - rough working drafts
  - depends by task
  - **Not applicable [exclusive]**

If "depends by task" is chosen, follow up in chat — and explicitly re-anchor the meta-vs-deliverable axis so the user doesn't drift back to deliverable-shape semantics (the form-side framing sentence doesn't carry into the chat turn on its own). Use a template that restates the axis. Suggested wording: *"For each of the 1–2 most common task types, what **tone** should Claude use **with you** during the work? (Casual / formal / drafty / polished — same axis as the pills above.) The tone of the artifact itself — prompts, reports, drafts, deliverables — is a separate question, handled per-run or captured in your DO behaviors."* If the user still answers with deliverable types or shapes (HTML cards, video walkthroughs, skills, prompts) instead of tones, ask once more with the axis re-stated; on the second drift, encode a low-confidence default and flag it as an inference in the Step 3 review table. Don't leave the FORMAT block empty.

**Not applicable** is the last pill, exclusive (see "N/A pill exclusivity" above). When N/A is the only selection: suppress the FORMAT-tone block in the assembled instructions entirely — don't substitute a default. This handles projects where the meta-conversation tone is genuinely a non-issue (e.g., a reusable tool whose every interaction is task-focused and tonal defaults would feel forced).

### Guardrails / DO behaviors / format notes / update cadence

These remain as in the prior version of the form, all under "project-specific or general" Round 2 long-text fields. Form copy unchanged from previous spec:
- **Guardrails (DO NOT items)** — long text, **pre-filled with a starter guardrail**: *"A starter guardrail is pre-filled. Add more (lines 2 and 3, or beyond) or delete what doesn't fit. With the reason if you have one — 'Never X because Y' generalizes better than 'Never X.' Example: 'Never echo member names without consent because the TAG is a confidential space.'"*

  Pre-fill content (rendered as text content between `<textarea>` tags — native HTML mechanism, no shell support required):

  ```
  1. Never invent details, numbers, dates, names or other information not specified by the user
  2. 
  3. 
  ```

  Lines 2 and 3 are intentionally empty — the numbering is the affordance, inviting the user to extend without re-typing the structure. The line-1 default is near-universal (a hallucination guardrail every project benefits from); the user can delete it if it doesn't fit, but the cost-of-typing-from-scratch is removed for the common case. The DO field has stronger project-specific variation and is **not** pre-filled — most users' DO list is genuinely project-specific.
- **DO behaviors** — long text: *"Anything Claude should reliably do in this project — with the reason. 'Lead with a one-line takeaway because reviewers skim.' If you don't have specific behaviors yet, leave blank — we'll fill from real chats."*
- **Format / tone notes** — short text (optional, in addition to Tone pills): *"Anything specific about structure or length defaults? E.g., 'short paragraphs, max three sentences,' 'always end with a one-line summary.'"*
- **Update cadence** — single select: after major decisions *(recommended default — ties updates to events that actually change the project, not to a calendar)* / weekly / monthly / before key meetings / as needed

## After the Round 2 form returns

Summarize what was captured back using the snapshot table from SKILL.md Step 3 (the assembled-state review table — that's the *next* step after Round 2). If the user's selections contradict an inference you announced in chat **before** the form (e.g., you announced *"I'd guess your Sensitivity is 'partner confidentiality' and 'DSA constraints in force' based on the brief and the draft DSA"* and the form return only includes "partner confidentiality"), surface the conflict instead of silently encoding the override:

> "I'd called out vulnerable population and DSA constraints based on the brief and the draft DSA — the form return only includes partner confidentiality. Is that intentional, or should I keep the others?"

Because pills don't pre-press, the skill must remember which inferences it announced before the form so it can compare them to what the user actually selected. Hold the announced-inference list in working memory across the form round trip.

Treat anything ambiguous as a follow-up question rather than a quiet assumption. The skill's job is to catch these moments; the widget alone won't.

## Inline-prose path — Round 1 (claude.ai-typical)

When the widget is unavailable, render Round 1 as four numbered questions in chat. **Do not redesign for inline** — mirror the form question-for-question. Do not include a "here's what I can see" preamble.

```
A few quick framing questions before I gather anything:

1. **What type of project is this?**
   - A reusable tool or workflow (recurring deliverables, templated analyses)
   - A time-bound engagement (defined scope, deliverables, end date)
   - An ongoing program or operation (recurring rhythm, no end date)
   - A reference or knowledge hub (making knowledge accessible)
   - Personal exploration or tracker
   - Something else

2. **What is the project's main purpose?** *(Examples: "the Calbright affordability pilot," "an internal operations project," "a reusable workflow to draft summaries from meeting notes." Leave broad if you want a wide first-pass.)*

3. **What stage are you in?**
   - Just starting / setting up
   - Actively in progress
   - In review or wrap-up
   - Built and in use
   - Other

4. **How would you like me to gather context?** *(Pick any combination)*
   - Use my connectors *(only listed if allowlisted connectors are visible: "I can pull from [Slack, Gmail, Drive, Asana, Notion, Calendar — max 8 displayed]")*
   - Project files I'll upload here
   - Ask me questions in chat
```

If no allowlisted connectors are visible, omit Q4's first option entirely — don't render a non-actionable choice.

## Inline-prose path — Round 2 (claude.ai-typical)

Render conditional sections per the form spec. Do not include sections the user didn't pick in Round 1 Q4. Do not redesign — mirror the form's section-by-section shape.
