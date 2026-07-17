# Recommended plugins and skills roadmap

Proposed additions to this marketplace where no skill exists yet. Each entry names the source material (mostly the onboarding refresh decks and wiki training resources) so building the skill is a matter of distilling material we already teach. Groupings follow the same principle as the marketplace: skills are organized by craft, since most crafts (qualitative research, quantitative analysis, deliverables) serve multiple IDEAS stages; a stage gets its own plugin only where the methodology itself is the content.

## Fill out existing plugins

### qualitative-research (exists, 1 skill today)
| Proposed skill | What it does | Why |
|---|---|---|
| user-testing | Design user testing protocols (including remote), moderate sessions, capture findings against design hypotheses | Testing designs with end users spans Diagnosis, Engineer, and Assess; the wiki has remote user-testing recommendations to distill |
| interview-guide | Draft semi-structured interview and focus-group guides tuned to a learning goal and stage (diagnosis vs. evaluation vs. scaling) | Per Niko: interviews are used in diagnosis, design, evaluation, and scaling — the skill should ask which stage and adapt |
| qualitative-synthesis | Code transcripts and field notes, extract themes, tie observations to behavioral barriers | Source: Qualitative Research Methods Parts 1–2 trainings |

### deliverables (exists)
| Proposed skill | What it does | Why |
|---|---|---|
| show-dont-tell-presentations | Apply ideas42's presentation design principles: show-don't-tell slide construction, PPT tactics, fixer-upper critiques | Source decks exist in onboarding (Show, don't tell; PPT tactics workbook; Presentation design principles); highest-frequency deliverable craft at ideas42 |
| writing-guidelines | ideas42 writing prose and design guidance beyond copy editing — document templates and structure | Source: wiki Writing and Design, Writing Guidelines + Templates (complements i42-copy-editor in ideas42-comms) |

## New plugins to build

### behavioral-diagnosis (Diagnosis-stage methodology)
The methodology itself — distinct from the qualitative/quantitative crafts used within it.
| Proposed skill | What it does | Why |
|---|---|---|
| behavioral-mapping | Walk through b-mapping: actions, decision points, bottlenecks; generate swing sheets from process descriptions or transcripts | Source: B-mapping PPT + blank swing sheet template; the signature ideas42 diagnosis tool |
| process-mapping-auditing | Map a partner's operational process and audit it for behavioral friction | Source: Process Mapping & Auditing deck (June 2026) |
| behavioral-concepts | Reference skill embedding the BSci Canon (defaults, salience, scarcity, identity, hot/cold gaps...) with theory, field application, and ideas42 example for each | Source: BSci Canon Parts I–II folders; makes Claude cite concepts the way ideas42 teaches them, in diagnosis write-ups and design rationales |

### intervention-design (Engineer-stage methodology)
| Proposed skill | What it does | Why |
|---|---|---|
| commonly-applied-interventions | Match diagnosed barriers to ideas42's intervention patterns (commitment devices, implementation intentions, defaults...) | Source: wiki Commonly Applied Behavioral Interventions cheat sheet + Design Parts 1–3 |
| design-ideation | Facilitate generating and refining design concepts from practical insights, including stakeholder feedback loops | Source: Generating Design Ideas, IDEAS Session 4 (Engineer) |
| prototyping | Turn concepts into testable prototypes; HCD methods | Source: HCD 101 + Prototyping resources |

### experimental-design (Assess-stage methodology)
| Proposed skill | What it does | Why |
|---|---|---|
| testing-protocol | Design testing protocols: outcomes, sample, randomization, pre-registration | Source: Testing Parts 1–4, Overview of Testing Process |
| lean-experimentation | Scope lighter-weight experiments when an RCT isn't feasible | Source: Lean experimentation outline deck |
| impact-evaluation | Structure impact evaluations and interpret results; analysis conventions (R/STATA norms) | Source: Impact Evaluation training deck |

### scale-sustain (Scale-stage methodology)
| Proposed skill | What it does | Why |
|---|---|---|
| implementation-planning | Build implementation plans for scaling proven designs with partners | Source: Implementation Planning deck |
| cost-effectiveness | Assess cost-effectiveness and market landscape for scale decisions | Source: IDEAS Session 6 (Scale & Sustain) |

### project-delivery (cross-stage execution)
| Proposed skill | What it does | Why |
|---|---|---|
| project-management | ideas42 PM practices: workplans, RACI, partner cadences, risk flags | Source: PM Onboarding Deck; pairs with the Asana connector |
| designing-for-yourself | Apply behavioral science to your own execution and decision making | Source: wiki Execution + Judgment trainings |

### biz-dev (role plugin)
| Proposed skill | What it does | Why |
|---|---|---|
| proposal-scoping | Draft proposals, scope and price engagements per ideas42 norms | Source: wiki Pricing and Scoping, Budgeting, Proposal Resources |
| funder-research | Research funders and partners, prep briefs for BD conversations | Adapts deep-research patterns to the Partner + Funder Management bucket |

### people-ops (role plugin)
| Proposed skill | What it does | Why |
|---|---|---|
| feedback-and-goals | Draft feedback and goal-setting docs per ideas42 frameworks | Source: wiki Team Management (Feedback, Goal Setting) |
| manager-toolkit | Managing to change the world, managing up & across, new manager guidance | Source: wiki Team Management trainings |
| onboarding-navigator | Answer new-hire questions about benefits, software, and org processes | Source: wiki Administration + onboarding kickoff materials |

## Build order suggestion

1. behavioral-diagnosis (b-mapping is the most distinctive, highest-leverage ideas42 method; the canon reference skill improves every other output)
2. qualitative-research fill-out (Niko flagged this gap directly)
3. show-dont-tell-presentations (touches every project team weekly)
4. experimental-design, then intervention-design, then scale-sustain
5. Role plugins (biz-dev, people-ops) as demand appears

Conventions when adding: one craft per plugin; a skill lives in exactly one plugin; stage-specific methodology goes in the stage plugin, reusable craft goes in the craft plugin; bump the plugin version and the marketplace version on every change.
