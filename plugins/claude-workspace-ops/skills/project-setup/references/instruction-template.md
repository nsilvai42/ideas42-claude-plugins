# Custom Instructions Template

**Purpose:** Structured template for generating Claude Project custom instructions.
**Use when:** Producing the instructions output at the end of the project-setup interview.
**Not for:** Knowledge file content. Knowledge files are *what* Claude knows; instructions are *how* it behaves.

## Length target

200–500 words. Shorter is too vague to shape behavior. Longer and Claude starts losing pieces across long conversations — important rules get buried.

If the draft is over 500 words, ask: which guidelines have never been violated in practice? Drop those.

## Structure

Use XML tags to demarcate each section. Anthropic's prompt-engineering guidance treats XML tags as the most reliable way to signal section boundaries to Claude — they reduce ambiguity in long custom-instructions blocks and let Claude reference the right section unambiguously when behaviors conflict (e.g., a `<format>` rule vs. a `<guidelines_do>` rule). Use lowercase, snake_case tags. Do not nest tags unnecessarily; each top-level section is its own block.

```
<role>
[One sentence. What Claude is in this project. Be specific about role and audience.]
Example: "You are a research analyst supporting the Bottom Line student outcomes team. Your audience is internal staff who use your output to inform partner conversations."
</role>

<context>
[2-3 sentences. What the project is for, who's involved, what's at stake. This is the "why this project exists" framing.]
Example: "This project supports the Why No Jobs message campaign — a 24-message sequence (M1-M24) sent to Bottom Line students about their post-graduation employment. Messages get reviewed in cycles by Cara, then Sarena, then sometimes Cassie. Voice and tone matter: Bottom Line's students are juggling multiple priorities and respond to messages that respect their time."
</context>

<guidelines_do>
[3-5 specific behaviors. Each one includes a "because" — the intent behind the rule.]
Examples:
- Use Oxford commas because we publish for international funders who expect them.
- Lead with the one-line takeaway, then back into the reasoning, because reviewers skim.
- When citing data, link to the underlying source so reviewers can verify.
</guidelines_do>

<guidelines_do_not>
[3-5 specific things to avoid. Negative framing is often more effective than positive.]
Examples:
- Don't draft external messages without flagging them for human review.
- Don't use em-dashes — we replace them with parentheses or commas in published work.
- Don't hedge ("perhaps," "might," "could") in client-facing recommendations. Be direct.
</guidelines_do_not>

<format>
[Tone, structure, length defaults. Keep this tight.]
Example: "Conversational but precise. Short paragraphs, max three sentences each. Lead with a one-line takeaway. Use markdown headers for any output longer than two paragraphs."
</format>

<when_unsure>
[Escalation rule. What should Claude do when context is missing?]
Examples:
- "Ask before assuming. Don't invent partner names, dates, or numbers — ask me to clarify."
- "If a request would require information that's not in the project files, say so explicitly rather than fabricating."
- "Surface uncertainty inline ('I'm not sure about X — please confirm') rather than producing a confident answer that's only 80% right."
</when_unsure>
```

If the project has reference materials worth quoting verbatim into the instructions (a brand-voice paragraph, a regulatory clause, a glossary), wrap them in their own descriptively-named tag (e.g., `<brand_voice_reference>`, `<glossary>`) so Claude can cite them by section. Don't dump long content inline — link to a knowledge file instead. Reserve inline tags for short, behavior-shaping references.

## High-leverage techniques

1. **Use XML tags to demarcate sections.** Anthropic's prompt-engineering best practice — XML tags reduce ambiguity, prevent rules in one section from leaking into another, and let Claude unambiguously reference the right block when guidelines conflict. Lowercase, snake_case, no unnecessary nesting. Don't substitute headers (`## ROLE`) or all-caps labels (`ROLE:`) for tags — they're softer signals and degrade in long contexts.

2. **Explain intent, not just rules.** "Use Oxford commas because…" beats "use Oxford commas." Intent helps Claude generalize at edge cases the user didn't anticipate.

3. **"Do NOT" lists move behavior more reliably than "Do" lists** for things like avoiding em-dashes, hedges, boilerplate caveats, or specific failure modes.

4. **Specify tone, structure, and requirements explicitly.** Vague: "be professional." Specific: "conversational but precise; short paragraphs, max three sentences each; one-line takeaway at the top."

5. **Separate profile preferences from project instructions.** Profile = your universal rules across all your work ("don't use em-dashes," "I prefer concise responses"). Project = the context for THIS work. Mixing them is the most common setup error.

6. **Place the most important rules first within each section.** In long instructions, earlier rules anchor more reliably than later ones. If a single guideline matters most ("never invent partner names"), make it the first item in `<guidelines_do_not>`.

## What NOT to put in instructions

- **Conditional or rare guidance.** Things that only apply sometimes belong in a Skill (loaded only when triggered), not in always-on instructions.
- **Things tools do better.** Spell-checking, code linting, mechanical rule enforcement — let purpose-built tools handle these.
- **Long lists of facts.** Facts go in knowledge files. Instructions should describe behavior.
- **Paragraphs of background.** Context belongs in a `project-overview.md` knowledge file. Instructions should reference the file, not duplicate its content.
