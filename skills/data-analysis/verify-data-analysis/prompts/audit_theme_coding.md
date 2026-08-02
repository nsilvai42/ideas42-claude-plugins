# Prompt — Audit open-text theme coding

**Use in:** a chat where a human reviewer can independently code a sample of responses without seeing the AI's tags.

**Inputs:**
- Raw open-text responses (the field that was coded)
- The theme dictionary or coding rule
- The AI-applied tags

**Output:** an inter-rater reliability report per theme, mapping to permitted downstream language per the template.

---

## Prompt

```
You are auditing open-text theme coding. The downstream analysis reports theme counts or percentages. Without an audit, those counts must remain directional.

INPUTS:
- raw text column: <name>
- AI tags: <comma-separated tag strings per row, or one indicator column per theme>
- theme dictionary or coding rule: <verbatim>
- themes used in downstream claims: <list of theme names>

TASK:

1. For each theme on the list:

   a. Pull all responses tagged with this theme. If > 20, sample 20.

   b. Pull 30 random responses NOT tagged with this theme.

   c. Output a worksheet with:
      | response_id | theme_being_audited | ai_tag | response_text | (human fills) human_tag | (human fills) disagreement_type | (human fills) reviewer_note |

   d. The human reviewer should code blind — they should not see the ai_tag column when coding. Suggest the operator hide that column in the workbook until coding is complete.

2. After human coding, compute per theme:
   - % agreement (matching tags / total)
   - Cohen's κ (if appropriate; pandas-cohen-kappa or scikit-learn)
   - false positive rate (ai_tag=1, human_tag=0)
   - false negative rate (ai_tag=0, human_tag=1)

3. Map results to permitted downstream language:
   - ≥ 90% agreement, κ ≥ 0.75 → precise percentage allowed
   - 80–90% agreement, κ 0.6–0.75 → approximate percentage with caveat
   - < 80% agreement or κ < 0.6 → directional only
   - No audit run → directional only

4. For each theme that fails, recommend either:
   - re-coding with a revised dictionary (and propose the revision)
   - keeping the downstream claim directional
   - excluding the theme from downstream claims

CONSTRAINTS:
- Do not let the human reviewer see the AI tag during coding. Blind comparison is the whole point.
- Do not "correct" the AI tags by editing them. The audit measures agreement, not the AI's tags' truth.
- A passing audit per theme is per-theme. Other themes in the same project may still be Directional only.

Return the audit worksheet, the agreement statistics, and the language-permission table.
```

## Notes for the operator

- This is the most expensive audit in the skill. Run only when a theme count is load-bearing in a downstream decision.
- The default disposition (no audit) keeps language directional. That is usually the right answer.
