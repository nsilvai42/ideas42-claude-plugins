---
name: right-size-setup
description: Recommends the right Claude surface (Chat / Cowork / Code / Claude Design), model (Haiku / Sonnet / Opus), and effort level for a given task. Use this skill whenever someone asks which model to use, which effort to pick, where to do a task (Chat vs. Cowork vs. Code vs. Claude Design), whether to use Haiku vs. Sonnet vs. Opus, whether Opus or max effort is overkill for something, or how to get the best results for a task. Also trigger when someone seems to be defaulting to the biggest model or highest effort out of habit — over-provisioning is the most common mistake. Trigger even for vague questions like "am I using Claude right?" or "is this the right setup for me?"
---

# Right-size your setup (surface · model · effort)

Give a confident, specific recommendation — not a hedged survey of all options. The person is asking because they want a verdict, not a menu.

## Three independent axes

A good setup is a triple: **surface · model · effort**. They answer different questions, so route them separately:

- **Surface** — *where* the work lives. Driven by what the task touches (files, apps, a repo), not by how hard it is.
- **Model** — matched to *task complexity* (Haiku → Sonnet → Opus).
- **Effort** — the *dial within a model*.

One principle ties it together: **raise effort before reaching for a heavier model, and switch surfaces only when the work genuinely needs files, apps, repo changes, or visual review.** Most people over-jump on all three axes — bigger model, higher effort, heavier surface — when a smaller setup would do the job faster.

## The failure modes you're correcting

1. **Always-Opus** — using the heaviest model for everything, which costs 4–12× more with no quality gain on bounded tasks
2. **Max-effort by default** — turning effort up "to be safe" when the default is sufficient (on structured tasks, higher effort can actually regress output quality)
3. **Haiku blindspot** — nobody reaches for Haiku, even when it's clearly the right tool. Surface it confidently
4. **Wrong surface** — copy-pasting endlessly in plain Chat for file- or repo-heavy work, spinning up Cowork/Code for something that's just a question, or describing a visual in words when Claude Design would build it

## Surface — where the work lives

Pick the surface from what the task *touches*, not its difficulty:

| The work… | Surface |
|---|---|
| Is a question, a draft, or a one-off — nothing on disk | **Chat** |
| Involves files/folders on the computer, documents, connected apps, or a multi-artifact project | **Cowork** |
| Touches a code repository, the terminal, or a software project | **Code** |
| Produces a visual or design artifact — mockup, slide deck, diagram, UI, or brand piece | **Claude Design** |

If they're already in a surface that fits, don't make them move. Only recommend switching when the work needs something the current surface can't do.

**Claude Design is browser-only and exposes the same model + effort controls as the other surfaces.** It's a distinct surface on the web (claude.ai in a browser) — not in the Cowork desktop app or Code. Recommend its model and effort as normal. If the person is working in the desktop app or Code, flag that they'll need to open it in a browser.

## Model — the three tiers

| Task signals | Model |
|---|---|
| Quick lookup, single Q&A, formatting tweak, short plain-language edit, simple translation | **Haiku 4.5** |
| Drafting, editing, summarizing, research synthesis, brainstorming, most project work | **Sonnet 4.6** |
| Open-ended strategy, genuinely complex multi-step analysis, ambiguous framing, high-stakes long-form | **Opus 4.8** |

**When a task sits between two tiers, start lower.** It's fast to re-run at higher if the first pass isn't enough. Starting at the top wastes time and limits.

## Effort settings (real UI labels — use these exactly)

Effort is per-model. Don't use generic "low/medium/high" without the model qualifier.

### Haiku 4.5
No effort grade — just an **Extended** toggle:
- **Off** (default): fast, standard output
- **On**: deeper reasoning, slower — only for questions that genuinely need it

### Sonnet 4.6
**Low · Medium · High · Max** + a separate **Thinking** toggle (off by default).

| Setting | When |
|---|---|
| Low | Quick tasks, routine drafts, anything single-pass. Default in Chat. |
| Medium | Longer drafts, nuanced edits, moderate synthesis. Default in Cowork. |
| High | Complex deliverables, multi-angle analysis, important external comms |
| Max | Reserve for the hardest synthesis tasks |
| Thinking | Structured multi-step reasoning — rare, use deliberately |

### Opus 4.8
**Low · Medium · High (default) · Extra · Max** + a separate **Thinking** toggle.

| Setting | When |
|---|---|
| Low / Medium | If you chose Opus for a bounded task — actively dial down from its default |
| High | The right starting point for most Opus work |
| Extra | Deep multi-step synthesis, long research or strategy passes |
| Max + Thinking | Maximum reasoning — expensive and slow; reserve for rare, high-stakes moments |

Opus defaults to High. On structured or bounded tasks, dial it down — High is often overkill.

## How to give the recommendation

Lead with the full setup as a triple, then one line of why, then how to set it.

**If you can render a visual widget or Artifact, show a settings card** (this is the preferred output — see `references/settings-card.md` for the template). The card has a "Recommended setup" header reading **Surface · Model · Effort**, three rows (Surface, Model, Effort) with the recommended option highlighted in each, and a one-line guidance footer. Always keep a one-line text verdict above the card so it still lands for anyone who can't see it. If you can't render visuals, use the text shape below.

Text shape:

```
Use **[Surface] · [Model] · [Effort]**.

[One sentence on why this fits — and, if relevant, why you're not recommending the heavier setup they'd reach for by default.]

How to set it:
• Surface: [Chat / Cowork / Code] — [one clause on why this surface].
• Model + effort: pick [Model] in the picker; set effort to [Setting]. [Mention Opus's Ultracode in Code only if relevant.]
```

**Stay tight — aim for ~120 words, and don't exceed ~150.** The value here is a fast, confident verdict, not an essay. Two failure modes to avoid:

- **Stay in your lane.** You're answering *which surface, model, and effort* — not *how to do the task*. Resist adding tips on phrasing the prompt, breaking the work into phases, or structuring the deliverable. That's a different question; if they want it, they'll ask.
- **At most one caveat, and only if it changes the call.** A single short note (e.g. "don't crank effort to Max for this") is fine when it corrects a likely mistake. Don't stack "one note" paragraphs — each extra caveat dilutes the verdict.

## When the request is too vague to route

If you can't tell what surface, model, or effort fits — e.g. "what should I use for my project?" with no sense of the task — ask first, don't guess. Gather the three routing signals: **what kind of task** it is, **what the output** should be, and **whether it touches files, apps, or a repo** (which decides the surface). If you can render an interactive form, collect them in one short widget; otherwise ask in a single plain-text question. Then produce the recommendation.

## Worked examples

**"Help me shorten a one-pager before sending to my director."**
→ **Chat · Sonnet 4.6 · Low.** Bounded editing with clear source material — paste it into Chat. (If the memo is a file on your computer you want edited in place, it's **Cowork · Sonnet · Medium** instead — same model, the surface follows the file.)

**"I'm designing a program theory for a new multi-site initiative."**
→ **Chat · Opus 4.8 · High** — or **Cowork** if you're pulling together several project files. Open-ended and strategic; Opus earns its cost here.

**"Translate this paragraph to plain language."**
→ **Chat · Haiku 4.5 · Extended off.** Fast, bounded, one-pass.

**"Refactor the data-cleaning script in my repo."**
→ **Code · Sonnet 4.6 · Smarter end of the slider.** It touches a repository, so the surface is Code; a routine refactor is well within Sonnet.

**"I need to mock up a one-page layout for our program flyer."**
→ **Claude Design · Sonnet 4.6 · Medium.** The output is a visual artifact, so it belongs on the design surface. Open it in a browser (Design isn't in the desktop app or Code); Sonnet handles a bounded layout well.

**"Should I crank the effort to max?"**
→ Rarely. Higher effort costs more time and uses your limits faster. On structured tasks — editing, formatting, summaries — it can regress quality versus the model's default. Start at the default; raise effort before you reach for a heavier model.
