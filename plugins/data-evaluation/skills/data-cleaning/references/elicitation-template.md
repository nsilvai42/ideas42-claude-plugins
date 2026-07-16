# Elicitation form patterns

How to ask the user a question during a cleaning run. Default to `interactive elicitation tool` with the elicitation module loaded. Fall back to `structured-question interface` only if visualize is unavailable.

## First: load the elicitation module

Before the first form, silently call:

```
tool schema reader with modules=["elicitation"]
```

Don't narrate this. Then proceed directly to your first form.

## Form structure

Every form uses the `<form class="elicit">` shell with header / body / footer. The header subject should reflect the operation being asked about — keep it under 4 words.

Header subjects to use:
- Discovery: `"Dataset details"`
- Per-pattern: `"{Operation} options"` (e.g., `"Cost-guess parsing"`, `"Multi-select setup"`)
- End-of-run: `"Wrap-up"`

## The `(recommended)` convention

When one option is clearly best practice for the user's situation, mark it with `(recommended)` after the label, like so:

```html
<button type="button" class="elicit-pill" data-value="flag-only-recommended"
  style="...">
  <span>
    <span style="font-size:13px; font-weight:500">Flag only (recommended)</span><br>
    <span style="font-size:11px; color:var(--color-text-tertiary)">Report null rates + patterns, don't impute</span>
  </span>
</button>
```

Use `(recommended)` when:
- The option matches established best practice in the literature or standard tooling
- The option is the safer default (preserves info, flags rather than drops)
- Other options are valid but require justification

Do NOT use `(recommended)` when:
- The choice is genuinely a matter of preference
- Multiple options are equally defensible
- The "right" answer depends on the user's analytic intent (in which case ask follow-up questions first)

## Choice format guide

Use the format that fits the question:

| Question shape | Format |
|---|---|
| Short labels, ≤4 words, no subtitle needed | Plain pills |
| Options with icons + one-line subtitle | Cards |
| Output format / file-type pickers | Preview tiles |
| Quantity, scale, threshold | `<input type="range">` |
| Date | `<input type="date">` |
| Free-form text | `.elicit-textarea` |

Don't render every group as plain pills — flat forms read undifferentiated. Vary visual format across the form.

## Standard groups for cleaning workflows

### Discovery — multi-question form

```html
<div class="elicit-group">
  <label class="elicit-question">What is this data about?</label>
  <textarea class="elicit-textarea" data-name="data_topic"
    placeholder="e.g. customer feedback from Q4 product survey"></textarea>
</div>

<div class="elicit-group">
  <label class="elicit-question">Which column is the primary key?</label>
  <div class="elicit-pills" data-name="primary_key" data-multi="false">
    <!-- One pill per high-cardinality candidate column detected -->
    <button type="button" class="elicit-pill" data-value="ResponseId">ResponseId</button>
    <button type="button" class="elicit-pill" data-value="email">email</button>
    <button type="button" class="elicit-pill" data-value="Other" data-other>Other</button>
  </div>
  <input type="text" class="elicit-other" data-for="primary_key" placeholder="Type the column name" hidden>
</div>

<div class="elicit-group">
  <label class="elicit-question">Output language for the reproducible script?</label>
  <div class="elicit-pills" data-name="script_language" data-multi="false">
    <button type="button" class="elicit-pill" data-value="python-recommended">Python (recommended)</button>
    <button type="button" class="elicit-pill" data-value="r">R</button>
  </div>
</div>
```

### Per-pattern — single decision form

```html
<div class="elicit-group">
  <label class="elicit-question">This column looks like a 5-point Likert scale. Recode to 1–5 ordinal?</label>
  <!-- Show 3-5 example values -->
  <div style="font-size:12px; color:var(--color-text-tertiary); margin-bottom:8px">
    Sample values: "Very likely", "Somewhat likely", "Neutral", "Somewhat unlikely", "Very unlikely"
  </div>
  <div class="elicit-pills" data-name="likert_action" data-multi="false">
    <button type="button" class="elicit-pill" data-value="recode-recommended">Recode to ordinal (recommended)</button>
    <button type="button" class="elicit-pill" data-value="leave">Leave as text</button>
    <button type="button" class="elicit-pill" data-value="skip">Skip this column</button>
  </div>
</div>
```

### Threshold pickers — use range slider

```html
<div class="elicit-group">
  <label class="elicit-question">Bot-score threshold? Values below get dropped.</label>
  <input type="range" class="elicit-slider" data-name="bot_threshold"
    min="0" max="1" step="0.05" value="0.5">
  <div style="display:flex; justify-content:space-between; font-size:11px; color:var(--color-text-tertiary); margin-top:4px">
    <span>0.0 (keep all)</span>
    <span>0.5 (Google + Qualtrics default — recommended)</span>
    <span>1.0 (only the most human-like)</span>
  </div>
</div>
```

### Ledger approval

For approving a sampled ledger preview, render the sample in chat as a clean markdown table BEFORE the form, then ask:

```html
<div class="elicit-group">
  <label class="elicit-question">Does the sample above look right?</label>
  <div class="elicit-pills" data-name="ledger_approval" data-multi="false">
    <button type="button" class="elicit-pill" data-value="approve">Looks good — finalize</button>
    <button type="button" class="elicit-pill" data-value="show-more">Show me 10 more examples</button>
    <button type="button" class="elicit-pill" data-value="adjust">Some changes needed</button>
  </div>
</div>
<div class="elicit-group">
  <label class="elicit-question">If changes needed, what to revisit?</label>
  <textarea class="elicit-textarea" data-name="adjustments"
    placeholder="e.g. don't code 'free' as $0; treat ranges as upper bound instead of midpoint"></textarea>
</div>
```

## Fallback to structured-question interface

If `interactive elicitation tool` is unavailable, fall back to `structured-question interface`. The same content principles apply:
- Mark the recommended option in the label
- Provide a clear `description` for each option explaining the implication
- Group related questions in a single structured-question interface call (up to 4 questions)
- Use multiSelect=true only for genuine multi-select cases

## When NOT to ask

Skip the form and proceed directly when:
- The user has already provided the answer in a previous chat message
- The answer is unambiguously inferable from the data (e.g., only one candidate primary key)
- The operation is deterministic and non-subjective (binary flag, ISO date conversion)
- The user explicitly said to "just do it" or selected fully-automated workflow style

When in doubt, ask. One extra question is cheap; an unwelcome surprise transformation is expensive.
