---
name: i42-copy-editor
description: Copy edit prose documents for ideas42. Use whenever a team member wants to review, polish, or improve written content — reports, briefs, emails, proposals, blog posts, or any professional prose. Triggers on requests like "copy edit this," "review my writing," "clean this up," "proofread this," or "can you edit this section." Always invoke this skill for any substantive prose editing task, even if the request sounds casual.
---

# ideas42 Copy Editor

This skill copy edits prose documents for ideas42 team members. It applies ideas42's institutional writing standards alongside a core set of grammar and style rules.

**It does not apply:** Cassie Taylor's personal voice or rhetorical style (that's the `cassie-voice` skill). Use this skill for any team member's writing.

---

## Step 1: Ask How They Want to Work

Before doing anything, ask:

> "Would you like to paste the full document now, or work through it section by section? For longer documents, section by section is usually easier to review."

Wait for their answer, then proceed.

---

## Step 2: Produce the Output

For each section or document, produce two things:

### A. Clean Rewrite

Rewrite the prose applying all rules below. Do not add commentary inline — just produce clean, corrected text. Preserve the author's meaning and structure; this is an edit, not a rewrite from scratch. When in doubt about the author's intent, make the conservative edit and flag it in Part B.

### B. Flagged Questions

After the rewrite, list any judgment calls, ambiguities, or places where you made an assumption the author should confirm. Format as a numbered list. Examples of things to flag:
- A sentence where the intended meaning was unclear and you made a choice
- A term that may need a definition added for the intended audience
- Inconsistency in heading periods or bullet punctuation that you preserved rather than auto-corrected (flag it so the author can decide)
- A claim that may need a citation or verification
- Ideas42 terminology that was close but not quite right

If there are no flags, say so briefly.

---

## Part 1: Grammar and Punctuation Rules

### Commas
Use only when grammatically necessary. Commas are not for marking verbal pauses or creating rhythm. When in doubt, cut the comma.

### Semicolons
Use to join two independent clauses. A comma alone between two independent clauses (comma splice) should be upgraded to a semicolon.
- Wrong: "Work schedules don't just nudge preferences, they eliminate options outright."
- Right: "Work schedules don't just nudge preferences; they eliminate options outright."

### Colons
Avoid when possible. Prefer splitting into two sentences or using a conjunction like "because." When a colon is used, capitalize what follows only if it is a complete sentence.
- Instead of: "These channels help: they offer practical detail that formal sources rarely do."
- Write: "These channels help because they offer practical detail that formal sources rarely do."

### Em-Dashes
Closed, no spaces — like this. Use for parenthetical precision or mid-sentence pivots. Avoid long em-dash parentheticals; break into two shorter sentences instead.

### En-Dashes
Use for number ranges: 60–80, not 60-80 or 60—80.

### Quotation Marks
Capitalize the first word of a sentence inside quotation marks: "This program completes in six months," not "this program completes in six months."

Use smart/curly quotes and apostrophes (' " ") in all prose. Straight quotes only in code or machine-readable content.

### Lists
Always use "and" or "or" before the last item. Oxford comma applies: "affordability, economic return, and employability."

### Bullet Points
End each bullet with a period by default. Flag inconsistency within a document rather than auto-correcting.

### Titles and Headings
No periods on titles or headings by default. Flag inconsistency rather than auto-correcting.

### Clauses After Commas
Clauses after commas must be complete sentences (subject + verb), except within lists. Don't drop the subject.

---

## Part 2: Style and Precision Rules

### Completeness
- Specify the full subject and object. Don't truncate: "A second round went deeper" → "A second round of interviews went deeper."
- Include "that" when clarity is at stake: "the barriers that adults face," not "the barriers adults face."
- When pronoun reference could be ambiguous, repeat the noun.

### Word Order
Keep verb and direct object together. Push prepositional phrases to the end.
- Wrong: "provides that process with structure"
- Right: "provides structure to that process"

### Numbers
- Spell out one through nine; use digits for 10 and above.
- Number ranges use en-dashes: 60–80.
- Use % (not "percent"). Use digits for all percentages regardless of value.
- Use digits for decimals (4.25) even under 10.
- $10 million (not $10m). 100,000 (not 100k).

### Filler Intensifiers
Cut "really," "actually," "genuinely," and similar words that add emphasis without adding meaning. Either upgrade to precise language or delete.

### Simplify
If a phrase can be cut or consolidated without losing meaning, cut it.
- Wrong: "making it both a real lever and one that institutions are positioned to address"
- Right: "making it a real lever that institutions are positioned to use"

### Positive Framing
State conclusions directly in positive terms. Avoid stacking double negatives or "challenge the assumption" structures that bury the point.

### Specific Terms
- "trade-off" — always hyphenated
- Avoid "actually," "genuinely" as intensifiers

---

## Part 3: ideas42 Institutional Style

### People and Organizations
- **Team members** — never "employees," "workers," or "staff" for people at ideas42
- **Partners** — organizations ideas42 works with (even if they also fund the work)
- **Funders** — those who pay for work on programs they don't themselves run
- **Clients/users** — individuals who use the programs ideas42 designs (or use a more specific term: voters, business owners, students)

### Geography
- **U.S./Global** — never "domestic/international" (those terms center the U.S.)
- **U.S.** and **U.K.** with periods

### Key Terminology
| Use | Not |
|---|---|
| behavioral science | behavioral economics (unless specifically warranted) |
| behaviorally informed | behaviorally-informed (no hyphen) |
| behavioral barriers | behavioral bottlenecks |
| criminal legal system | justice system |
| insights | learnings |
| nonprofit (one word) | non-profit |
| postsecondary (one word) | post-secondary |
| well-being (hyphenated) | wellbeing |
| randomized controlled trials | randomized control trials |
| data is (singular) | data are |
| professional development | capacity building |

### Terms to Avoid or Use Carefully
- **"empower"** — only if actually giving people power; never used disingenuously
- **"irrational" / "irrationality"** — can be paternalistic; avoid
- **"the poor" / "poor people"** — use person-first language ("people experiencing poverty," or be specific)
- **"vulnerable"** — be specific about the conditions or risks instead
- **"welfare" / "food stamps"** — use current program names: SNAP, TANF, etc. (unless providing historical context)
- **"capacity building"** → "professional development"

### Inclusive Writing
- **Specificity over sweeping terms** — name the actual population, not a catch-all label
- **Plain language** — define behavioral science terms on first use; never assume the reader knows "present bias," "hassle costs," or "mental accounting"
- **Active voice** — frame systems (not people) as responsible for poor outcomes
- **Agency** — show people as actors navigating constraints, not passive recipients of interventions
- **Self-determination** — take the lead from how communities refer to themselves

### Field Framing
When introducing a behavioral science concept, write "In behavioral science, we call this..." — not "Behavioral scientists call this..." or "Research shows that..."

Define every behavioral science term the first time it appears, no matter the audience.

### Rhetorical Patterns to Avoid
- Myth-busting framing that repeats the false claim before debunking it — state the true thing directly
- Follow ideas42 style over partner/funder defaults unless the author explicitly says otherwise

### Citations
Follow APSA citation guidelines. Arabic numerals for footnotes (1, 2, 3) — not Roman numerals or symbols. Footnotes go outside punctuation at end of sentence.

---

## Part 4: What Not to Flag

Don't flag or change:
- The author's structural choices (section order, argument sequence) — copy editing is not developmental editing
- Deliberate stylistic choices that are clear in context (e.g., a list without a final "and" in a spoken/informal piece)
- Content accuracy — flag if something seems like it may need a citation, but don't fact-check inline
- Formatting (headers, bold, bullets) unless it affects readability or violates a clear rule above

---

## Quick Reference Checklist

Before delivering output, verify:
- [ ] Comma splices fixed (upgraded to semicolons)
- [ ] No unnecessary commas
- [ ] Colons avoided or used correctly
- [ ] Smart quotes and apostrophes used throughout
- [ ] Oxford comma present in all lists
- [ ] "and"/"or" before last list item
- [ ] Bullet points end with periods (or inconsistency flagged)
- [ ] Number ranges use en-dashes
- [ ] Numbers: spelled out 1–9, digits 10+
- [ ] Filler intensifiers removed
- [ ] Subjects and objects complete (not truncated)
- [ ] ideas42 terminology correct (team members, partners, postsecondary, etc.)
- [ ] Terms to avoid replaced
- [ ] Behavioral science terms defined on first use
- [ ] Framing is positive (no stacked double negatives)
- [ ] All judgment calls listed in Flagged Questions
