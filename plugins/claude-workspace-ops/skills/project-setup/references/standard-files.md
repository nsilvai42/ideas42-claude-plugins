# Standard Knowledge File Templates

**Purpose:** Fillable templates for the standard files every Claude Project should have, with per-type variants where the shape changes.
**Use when:** Generating the knowledge file pack at the end of project setup.
**Not for:** Project-specific files. The user's domain content (interview summaries, prior reports, source material) is on top of these standard ones, not instead of them.

## The standard set, by project type

Every project gets `project-overview.md` + `status.md` + `setup-checklist.md`. The *shape* of each varies by the Round-1 project type. Use the variant that matches the user's selection; for **knowledge hub** and **personal exploration**, start from the closest analog (knowledge hub → ongoing program; personal exploration → reusable tool) and adapt.

| Project type | project-overview shape | status shape | Setup checklist focus |
|---|---|---|---|
| Reusable tool or workflow | Framework / schema / glossary | Phase: initial setup → in use | First-run sanity checks |
| Time-bound engagement | Partner / team / timeline / workstreams | Current phase / decisions / milestones | Kickoff items |
| Ongoing program / operation | Program / team / recurring deliverables / cadence | Last cycle / next cycle / standing decisions | Cadence checks |
| Reference / knowledge hub | Index / map / taxonomy | Recent additions log | Retrieval tests |
| Personal exploration | Light: what / when / why | Optional | Minimal — first sanity check |

`style.md` is optional everywhere; skip if the project uses ideas42 brand voice (use the `ideas42-brand` skill instead) or if the runtime tone is determined by inputs (common for reusable tools).

## File metadata header (required on every file)

Every knowledge file gets this 3-line block at the top:

```markdown
**Purpose:** [One sentence: what this is]
**Use when:** [One sentence: when Claude should reference this]
**Not for:** [One sentence: what this isn't]
```

Three lines. Costs nothing. Single highest-leverage technique for retrieval quality.

## Template: project-overview.md — time-bound engagement

```markdown
**Purpose:** Stable reference for what this project is, who's on it, and what it's trying to accomplish.
**Use when:** Starting any new conversation in this project, or when context about scope/team/goals is relevant.
**Not for:** Current status or recent decisions — those live in status.md.

# [Project name]

## What this is
[1-2 sentences: the project in plain language. What problem are we working on, for whom.]

## Why we're doing it
[1-2 sentences: the goal, the success criteria, why now. What changes if we succeed.]

## Who's involved
- **[Name, role]** — [their role on this project, decision-making authority if relevant]
- **[Name, role]** — [...]
- **Partner: [Org name]** — [their role, primary contact]

## Workstreams
- **[Workstream name]** — [one-line description, who leads]
- **[Workstream name]** — [...]

## Key terms and acronyms
- **[Term]** — [definition]
- **[Acronym]** — [expansion + meaning]

## Out of scope
[Optional but useful. What this project is *not* doing, especially if it's adjacent to something it could be confused with.]

## Connected resources
- Asana: [link]
- Drive folder: [link]
- Slack channel: [link]
- Other: [link]
```

## Template: project-overview.md — reusable tool or workflow

```markdown
**Purpose:** Stable reference for what this tool does, how it's used, and what runtime references it depends on.
**Use when:** Any conversation in this project — the tool's framework, schema, and glossary are always relevant.
**Not for:** First-run setup state or last-run notes — those live in status.md.

# [Tool name]

## What this tool does
[1-2 sentences: the workflow in plain language. What input → what output.]

## Who runs it and when
- **Operator(s):** [who runs it]
- **Trigger:** [what kicks off a run — meeting, event, request, schedule]
- **Cadence:** [how often]

## Inputs and outputs
- **Inputs needed each run:** [list]
- **Output shape:** [format, length, structure]
- **Quality bar (examples):** [link to canonical good outputs]

## Framework / schema
[The tool's governing structure. Could be a checklist, a rubric, a decision tree, a set of behavioral lenses. Keep this stable — it's what makes runs comparable.]

## Key terms and acronyms
- **[Term]** — [definition]

## Runtime references
- **[Reference doc]** — [what role it plays at runtime; AI-voice files belong here]
- **[Style guide]** — [...]

## Connected resources
- Drive folder: [link]
- Other: [link]
```

## Template: project-overview.md — ongoing program or operation

```markdown
**Purpose:** Stable reference for the program — its rhythm, its team, its standing commitments.
**Use when:** Starting a conversation about program work, or when cadence / team / standing decisions context matters.
**Not for:** Last-cycle notes or upcoming-cycle prep — those live in status.md.

# [Program name]

## What this program does
[1-2 sentences: program purpose, who it serves, what it produces on its rhythm.]

## Recurring rhythm
- **Cadence:** [weekly / monthly / quarterly / event-driven]
- **Recurring deliverables:** [list]
- **Standing meetings or events:** [list]

## Team
- **[Name, role]** — [their standing role on the program]

## Standing decisions and guardrails
[Decisions made early that shape every cycle's work. The institutional memory bedrock.]
- **[Decision]** — [Date]. *Why:* [rationale]

## Stakeholders
- **[Name or role]** — [what they care about, when they weigh in]

## Key terms and acronyms
- **[Term]** — [definition]

## Connected resources
- Notion: [link]
- Asana: [link]
- Slack channel: [link]
```

## Template: status.md — time-bound engagement

```markdown
**Purpose:** Living state of this project. Current phase, recent decisions, active work.
**Use when:** Anything time-sensitive — what's happening now, what's blocking, what's next.
**Not for:** Stable context (use project-overview.md). Historical archive (use a separate decisions log if needed).

_Last updated: [YYYY-MM-DD]_
_Update cadence: [weekly / after major decisions / monthly]_

## Current phase
[One sentence: where we are in the project arc.]

## Active workstreams
- **[Workstream]** — [status: green / yellow / red] — [one-line progress note]
- **[Workstream]** — [...]

## Recent decisions
- **[YYYY-MM-DD]** — [Decision made]. *Why:* [Brief rationale.]
- **[YYYY-MM-DD]** — [...]

## Upcoming milestones
- **[YYYY-MM-DD]** — [Milestone or deliverable]
- **[YYYY-MM-DD]** — [...]

## Open questions / blockers
- [Question or blocker]. Owner: [name]. Needed by: [date].
- [...]

## Recent activity
- **[YYYY-MM-DD]** — [What happened, briefly. One line per entry.]
- **[YYYY-MM-DD]** — [...]
```

## Template: status.md — reusable tool or workflow

```markdown
**Purpose:** Living state of this tool. Current phase of the tool's lifecycle, recent runs, recent revisions.
**Use when:** Starting a run, deciding whether to revise the tool, looking up what last run produced.
**Not for:** The tool's framework or schema (those live in project-overview.md).

_Last updated: [YYYY-MM-DD]_
_Update cadence: [after each run / weekly / as needed]_

## Current phase
[One sentence: initial setup / actively used / under revision / shelved.]

## First-run sanity checks
- [ ] Inputs flow through cleanly
- [ ] Output shape matches the quality bar
- [ ] Runtime references resolve (no broken pointers)
- [ ] [Type-specific check]

## Recent runs
- **[YYYY-MM-DD]** — [run subject / input]. *Output:* [link or note]. *Notes:* [anything off]

## Recent revisions to the tool itself
- **[YYYY-MM-DD]** — [What changed in framework/schema/prompts]. *Why:* [trigger]

## Open improvements
- [Improvement idea]. Triggered by: [run].
```

## Template: status.md — ongoing program or operation

```markdown
**Purpose:** Living state of the program. Last cycle's activity, the next cycle, and the running list of standing decisions.
**Use when:** Prepping for a cycle, looking up what last cycle decided, checking standing commitments.
**Not for:** Program structure or team (those live in project-overview.md).

_Last updated: [YYYY-MM-DD]_
_Update cadence: [tied to the program's rhythm — weekly / monthly / quarterly]_

## Last cycle
- **Cycle:** [identifier — date range or cycle number]
- **Deliverables shipped:** [list]
- **Decisions made:** [link to running decisions log below]
- **What surprised us:** [optional but valuable]

## Next cycle
- **Cycle:** [identifier]
- **Planned deliverables:** [list]
- **Watch-fors / known risks:** [list]

## Running decisions log
- **[YYYY-MM-DD]** — [Decision]. *Why:* [rationale]. *Cycle:* [when]
- **[YYYY-MM-DD]** — [...]

## Open questions / cross-cycle threads
- [Thread]. Owner: [name]. Cycle to resolve by: [target]
```

## Template: setup-checklist.md (first-class deliverable)

The setup checklist is the action-dense file the user actually checks off. It varies materially by project type — pick the variant that matches.

### Variant — reusable tool or workflow

```markdown
**Purpose:** First-run sanity checks plus a return-and-revise rhythm for this tool.
**Use when:** Right after setup, then again after the first 2–3 real runs.
**Not for:** Day-to-day tool operation (that's the runtime documentation in project-overview.md).

# [Tool name] — setup checklist

## First run
- [ ] Run the tool against [first real input]
- [ ] Compare output to the quality-bar example — does it match shape, tone, depth?
- [ ] Verify all runtime references load (uploads visible, AI-voice files treated as documentation)
- [ ] Check that guardrails fire on [the test edge case]

## After 2–3 runs
- [ ] Note any prompts or framework pieces that needed manual override
- [ ] Update project-overview.md framework section to encode learned defaults
- [ ] Decide: stable, or still iterating?

## Maintenance rhythm
- [ ] Re-read instructions after every 5 runs (or monthly, whichever first)
- [ ] Quarterly prune of stale runtime references

## What NOT to add to this Project later
- Conditional rules for one-off run types — those go in the run input, not the project
- Long source documents — summarize and link, don't dump
```

### Variant — time-bound engagement

```markdown
**Purpose:** Kickoff checklist plus a maintenance rhythm for the engagement.
**Use when:** Right after setup; revisit at major project milestones.
**Not for:** The engagement's actual workplan (that's in Asana / your PM tool).

# [Engagement name] — setup checklist

## Kickoff
- [ ] Confirm DSA / IRB / compliance constraints are reflected in instructions DO-NOT list
- [ ] Verify partner brand voice doc is in knowledge files (or skill is referenced)
- [ ] Schedule first status.md update (suggest: end of this week)
- [ ] Add Asana / Drive / Slack links to project-overview.md "Connected resources"

## Maintenance rhythm
- [ ] Revisit instructions after 3–5 chats
- [ ] Update status.md weekly or after major decisions
- [ ] Quarterly prune of context that's become stale

## What NOT to add to this Project later
- Raw transcripts or 30-page PDFs — summarize first
- Mechanical rules linters can handle
- Always-on rules that only apply sometimes — those go in a Skill
```

### Variant — ongoing program or operation

```markdown
**Purpose:** Cadence checks for the program's recurring rhythm.
**Use when:** Setup, then on the program's recurring rhythm.
**Not for:** A single cycle's workplan (that's last/next cycle in status.md).

# [Program name] — setup checklist

## Initial setup
- [ ] Standing decisions captured in project-overview.md
- [ ] Cadence reflected in status.md update frequency
- [ ] Stakeholder map current

## Each cycle
- [ ] Update status.md "Last cycle" before the next cycle starts
- [ ] Decisions made this cycle logged in the running decisions log
- [ ] Cross-cycle threads checked — anything ready to resolve?

## Quarterly
- [ ] Prune project-overview.md — anything no longer true?
- [ ] Review running decisions log — anything to retire?
- [ ] Confirm stakeholder map still accurate

## What NOT to add to this Project later
- Cycle-specific minutiae — those die after the cycle, no need to persist
- Personal preferences not specific to the program
```

### Variants — knowledge hub and personal exploration

For **knowledge hub**, adapt the ongoing program variant: replace "cycles" with "additions" and add a retrieval-test row in initial setup ("Pose 3–5 typical lookup questions; do answers come back cleanly?").

For **personal exploration**, use a minimal version: one first-sanity-check row, one return-cadence row. The user picks both.

## Template: style.md (optional)

Skip this if the project uses the standard ideas42 brand voice — install/reference the `ideas42-brand` skill instead. Use `style.md` only when the project has tone needs that aren't covered by the brand standard (e.g., a partner whose voice differs significantly).

```markdown
**Purpose:** Voice, tone, and formatting conventions specific to this project.
**Use when:** Producing any written output for this project — internal or external.
**Not for:** Mechanical rules that linters or spell-checkers handle better.

# Voice and style — [project name]

## Tone
[Describe the tone in 2-3 sentences. Use examples where you can.]

## Audience
[Who reads what we produce. What they care about. What they don't.]

## Formatting defaults
- Paragraph length: [short / medium / long]
- Headings: [used liberally / used sparingly / not used]
- Lists: [bullets / numbered / both]
- Tone marker: [conversational / formal / depends]

## Things to do
- [Specific stylistic move with reason]
- [...]

## Things to avoid
- [Specific thing with reason — "the partner reads anything in passive voice as evasive"]
- [...]

## Examples
- [Link to a piece of past work that exemplifies the voice]
```

## Filling these out

When generating these for the user, pre-fill as much as you can from what you've gathered. Don't leave a section blank if you have material that fits — the user can edit. The whole "gather first, infer, confirm" principle applies to the templates too.

For sections where you genuinely don't have information, leave a `[fill in: …]` placeholder rather than guessing. Better that the user fills it in than that Claude eventually retrieves a fabricated detail with confidence.
