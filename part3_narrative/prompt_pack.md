# Reusable Prompt Pack — Flagged Category Narrative

## Trigger

This prompt is triggered when a category's `is_flagged` result is `"flagged"`.

## Input list

The prompt requires the following placeholder variables:

- `{category}` — product category
- `{previous_revenue}` — revenue in the previous month
- `{current_revenue}` — revenue in the current month
- `{mom_pct}` — calculated Month-on-Month percentage
- `{month}` — current month
- `{prev_month}` — previous month

## Prompt

Write a concise stakeholder update for a regional manager using the
Context → Insight → Implication structure.

Use only the supplied input values.

Context:
Explain what category is being measured and compare `{month}` with
`{prev_month}`.

Insight:
State `{category}` revenue for `{prev_month}` as `{previous_revenue}`,
revenue for `{month}` as `{current_revenue}`, and the MoM change as
`{mom_pct}%`. Label the numerical observation explicitly as a fact.

Implication:
Provide one specific and actionable next step for the regional manager.
If a possible cause is suggested, label it explicitly as a hypothesis.
Do not present an unproven cause as a fact.

Never state a number that is not one of the supplied placeholders.
Do not invent sales, orders, customers, causes, or other business facts.

## Checklist

Before using the narrative, verify:

1. Every number in the draft matches one of the supplied placeholder
   values exactly.
2. The category and both months are explicitly named.
3. The numerical observation is labeled as a fact.
4. Any proposed cause is labeled as a hypothesis rather than a fact.
5. The recommendation is specific and actionable.
6. No unsupported business claim has been introduced.
7. The narrative follows the Context → Insight → Implication structure.
8. No raw reseller name or other internal identifier is exposed.