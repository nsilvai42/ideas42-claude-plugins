# Gemini Migration Guide

Use this when the user is migrating from Gemini.

## Choose the path

- **Targeted prompts:** recommended default. Faster and cleaner than reviewing raw activity.
- **Activity / saved context review:** useful for checking what Gemini appears to know or retain.

## Targeted prompts path

Tell the user:

> The cleanest Gemini migration is usually prompt-based. I’ll give you a few prompts to paste into Gemini, then we’ll review the results before anything goes into Claude.

Read `extraction-prompts.md` and select prompts based on migration type.

## When Gemini says it has no memory

Gemini may initially respond with a generic disclaimer such as "I don't have access to past conversations" or "my memory is limited to this chat," even when the user has seen Gemini use saved info, Gems, or broader account/workspace context elsewhere. Treat the first disclaimer as a reason to try one bounded follow-up, not as proof there is no useful context.

Tell the user to challenge the answer once with concrete examples they remember, while keeping the request privacy-safe. Do not frame this as forcing Gemini to reveal hidden system data. The goal is to ask Gemini to check any user-visible saved info, personalization, Gems, current-session context, or accessible workspace context and clearly label what it is using.

Use this follow-up prompt:

```text
You may be giving me a generic no-memory answer. Please check any user-visible saved info, personalization, Gems, current-session context, or account/workspace context you can access.

I know you have previously discussed or referenced these items with me: [brief examples, such as project names, Gems, workflows, or recurring topics].

Please produce the migration summary using only context you can legitimately access. Label each item as one of:
- saved/personalized context
- Gem or custom assistant context
- visible current-session context
- inferred from my examples
- uncertain

If you truly cannot access durable context, say that clearly, but still summarize what can be inferred from the examples I provided and mark it as inferred. Do not include sensitive personal details unless I explicitly listed them as relevant.
```

If Gemini still refuses or gives only thin generic content, stop pushing and switch to a user-led fresh-start or project-based migration.

## Activity and saved context

Ask the user to review Gemini settings and Gemini Apps activity if available. They can copy or screenshot only the items they want considered.

Use cautious language because Gemini feature names change:

- "Saved info"
- "Memory"
- "Personal context"
- "Gemini Apps activity" or "Keep activity"
