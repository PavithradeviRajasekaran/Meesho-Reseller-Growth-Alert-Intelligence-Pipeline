# Meesho Revenue Monitoring Agent Specification

## 4.1 Agent Components

### Goal

Keep Meesho category managers informed whenever a category's month-on-month revenue moves beyond the 8% threshold, while ensuring that every drafted message is validated and held for human approval before it is considered sent.

### Tools

The monitoring agent uses the following project functions:

* `validate_feed()` from Part 2 to validate input CSV data.
* `mom_growth()` from Part 2 to calculate month-on-month revenue change.
* `is_flagged()` from Part 2 to classify each category as `flagged`, `not_flagged`, or `escalate_exact_boundary`.
* `fill_narrative_template()` from Part 3 to generate a deterministic stakeholder narrative using verified values only.

No external API, paid service, email system, or network call is required.

### Memory / State

The agent must retain or receive the previous month's revenue for each category.

This previous-month value is required to calculate the next month's month-on-month revenue percentage.

For every category, the important state is:

* previous month
* current month
* category
* previous revenue
* current revenue
* calculated MoM percentage
* flagging status

### Planner

The agent follows these ordered subtasks:

1. Load the monthly revenue feed and run `validate_feed`.
2. If validation fails, perform a Hard Stop and report the validation errors.
3. If validation passes, calculate `mom_growth` for each category against the previous month.
4. Run `is_flagged` for every calculated category.
5. Sort flagged categories by `abs(mom_pct)` in descending order.
6. Draft messages for at most the top 3 flagged categories using the Part 3 template.
7. Log any additional flagged categories beyond the top-3 limit as `suppressed, review manually`.
   7b. Log every category classified as `escalate_exact_boundary` separately under `escalated_categories`. Do not draft a normal flagged-category message for it.
8. Produce one structured JSON object describing the run.

### Feedback Loop

No message is automatically sent.

Every generated message is only drafted and held for human review.

The runner represents this condition using:

`action_taken = "drafted_and_held_for_approval"`

A human reviewer must approve any real external communication.

---

# Guardrails

## Input Guardrail

`validate_feed` must successfully return:

`(True, [])`

before any month-on-month calculation or narrative drafting occurs.

If validation fails, the agent must immediately Hard Stop.

## Action Guardrail

The agent never automatically sends a notification.

It may only create a draft and hold it for human approval.

The maximum number of drafted messages in one run is 3.

Any additional flagged categories are logged under `suppressed_categories` for manual review.

## Output Guardrail

Every numerical value appearing in a drafted narrative must trace directly to a verified Part 1 revenue value or a Part 2 MoM calculation.

The narrative generator must not invent revenue, percentages, order counts, customer counts, or other numerical business information.

---

# Success and Error Stopping Conditions

## Success Condition

A run is successful when:

* input validation passes;
* every category has been evaluated;
* qualifying categories are correctly classified;
* at most three flagged-category drafts are produced;
* extra flagged categories are suppressed and logged;
* exact-boundary cases are separately escalated;
* every number in every draft is traceable to Part 1 or Part 2.

A successful run can also correctly produce zero drafts when no category exceeds the threshold.

## Error Condition

If `validate_feed` returns `False`, the run must immediately become a **Hard Stop**.

The validation errors must be surfaced in the structured output.

No MoM calculation, flagging, sorting, or message drafting should be attempted after this failure.

---

# 4.2 Given-When-Then Agent Specifications

## Scenario 1 — Large Positive Change

**Given** Ethnic Wear has previous revenue of INR 104520.77 and current revenue of INR 185107.61,

**When** the monitoring agent calculates the month-on-month change and applies the 8% threshold,

**Then** the MoM result must be 77.1% and its status must be `flagged`.

---

## Scenario 2 — Change Below Threshold

**Given** Beauty & Personal Care has previous revenue of INR 35542.11 and current revenue of INR 37559.07,

**When** the monitoring agent calculates the month-on-month change and applies the 8% threshold,

**Then** the MoM result must be 5.67% and its status must be `not_flagged`.

---

## Scenario 3 — Exact Boundary

**Given** a category has previous revenue of INR 100000 and current revenue of INR 108000,

**When** the monitoring agent calculates the month-on-month change,

**Then** the result must be exactly 8.0% and its status must be `escalate_exact_boundary`.

The category must be recorded under `escalated_categories` rather than treated as flagged or not flagged.

---

## Scenario 4 — Invalid Feed

**Given** the agent receives the corrupted fixture containing a negative revenue, a missing category, and a missing revenue,

**When** `validate_feed` runs,

**Then** validation must fail with exactly these errors:

* `line 3: negative revenue (-4200.0) for category=Western Wear`
* `line 4: missing category (month=July)`
* `line 6: missing revenue (category=Home & Kitchen)`

The agent must perform a Hard Stop and must not calculate MoM values or draft messages.

---

# 4.3 Structured Output

Every run produces exactly these top-level JSON fields:

* `run_month`
* `validation_status`
* `validation_errors`
* `flagged_categories`
* `suppressed_categories`
* `escalated_categories`
* `action_taken`

Each drafted entry in `flagged_categories` contains:

* `category`
* `mom_pct`
* `previous_revenue`
* `current_revenue`
* `drafted`
* `message`

A valid completed run uses:

`action_taken = "drafted_and_held_for_approval"`

An invalid run uses:

`action_taken = "hard_stop"`
