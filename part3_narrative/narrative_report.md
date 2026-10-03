# Part 3 — Reliable AI Narrative & Prompt-Pack Report

## 3.2 Worked Narrative Reports

### May — Ethnic Wear

**Context:**  
This measures the Month-on-Month revenue change for the Ethnic Wear
category from April to May.

**Insight — Fact:**  
Ethnic Wear revenue increased from INR 104520.77 in April to
INR 185107.61 in May. The verified MoM growth is **77.1%**, and the
Part 2 engine classifies this result as **flagged**.

**Implication — Hypothesis:**  
The regional manager should check the May Ethnic Wear sales activity
and identify which products or sales channels contributed to the
increase before deciding whether the increase should be sustained.
Any specific cause of the increase is a hypothesis unless supported
by additional data.

### June — Ethnic Wear

**Context:**  
This measures the Month-on-Month revenue change for the Ethnic Wear
category from May to June.

**Insight — Fact:**  
Ethnic Wear revenue decreased from INR 185107.61 in May to
INR 76371.53 in June. The verified MoM growth is **-58.74%**, and the
Part 2 engine classifies this result as **flagged**.

**Implication — Hypothesis:**  
The regional manager should check June Ethnic Wear product-level
performance and compare the affected sales activity with May before
taking corrective action. A specific cause for the decline is a
hypothesis unless additional data confirms it.

---

## Narrative Self-Score

### Specificity

**Pass:** The narratives identify the Ethnic Wear category, the exact
months, and the verified revenue and MoM percentages.

### Audience Fit

**Pass:** The narratives focus on what a regional manager should
understand and do next rather than describing implementation details.

### Completeness

**Pass:** Both narratives contain Context, Insight, and Implication
sections.

### Actionability

**Pass:** Each implication gives a concrete next step: examine
product-level performance and sales activity before taking action.

---

# 3.3 Chart-Choice Justification

## Question 1 — Which month had the highest total revenue?

**Recommended chart: Column chart.**

This is a univariate comparison of total revenue across three months.
A column chart makes the comparison clear within 10 seconds. The
y-axis should start at zero so that the differences in revenue are not
visually exaggerated. No legend is necessary because there is only
one series, and 3D effects should be avoided.

The values are:

- April: INR 419417.43
- May: INR 444594.25
- June: INR 398055.24

---

## Question 2 — What percentage share does Ethnic Wear represent of
April's total revenue?

**Recommended chart: Donut chart.**

This is a composition question involving Ethnic Wear's share of
April's total revenue. A simple donut chart can communicate the
single percentage share quickly. The Ethnic Wear share is **24.92%**
of April's total revenue, based on INR 104520.77 out of
INR 419417.43.

Because this is a composition question rather than a trend or
comparison across multiple dimensions, a composition chart is
appropriate. The chart should remain simple and avoid 3D effects.

---

## Question 3 — How do the four regions compare on total revenue?

**Recommended chart: Horizontal bar chart.**

This is a univariate comparison of total revenue across four regions.
A horizontal bar chart makes the regional values easy to compare and
keeps the category labels readable. The x-axis should start at zero
so the magnitude comparison is not distorted. Only one measure is
being displayed, so a legend is unnecessary, and 3D effects should
be avoided.

The regional revenue values are:

- North: INR 337125.46
- South: INR 316736.68
- East: INR 275098.45
- West: INR 333106.33

---

# 3.4 Top-Reseller Narrative and Masking

The following narrative intentionally uses reseller aliases instead
of raw reseller names.

**Top-reseller narrative:**

The top-reseller results identify five resellers whose total spend
exceeded INR 50000. The relevant resellers are referenced using their
region and coded aliases only:

- North — ALIAS-06
- Jaipur/region information — ALIAS-05
- Hyderabad/South — ALIAS-12
- Mumbai/West — ALIAS-19
- Mumbai/West — ALIAS-22

The regional manager can use these coded aliases to identify the
relevant internal records without exposing raw reseller names in an
external-facing narrative.

The narrative should never contain raw names such as
"Mumbai Reseller 1".