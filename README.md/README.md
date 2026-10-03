#Meesho Reseller Growth & Alert Intelligence Pipeline

##Project Overview

The **Meesho Reseller Growth & Alert Intelligence Pipeline** is an end-to-end analytics and monitoring project designed to analyze reseller and category-level revenue performance.

The pipeline takes raw reseller order data, performs SQL-based analysis, calculates month-over-month (MoM) revenue growth, validates data quality, generates business narratives, and produces guarded monitoring alerts through a mock agent workflow.

The project is divided into four integrated parts:

1. **Part 1 — SQL Analytics**
2. **Part 2 — Growth Engine**
3. **Part 3 — Narrative Intelligence**
4. **Part 4 — Agentic Monitoring Workflow**

---

##Project Objectives

* Generate a reproducible reseller/order dataset.
* Store and analyze data using SQLite.
* Calculate category-level monthly revenue.
* Calculate month-over-month revenue growth.
* Identify significant revenue changes using configurable thresholds.
* Validate incoming CSV feeds before processing.
* Generate concise business narratives from validated results.
* Mask reseller identifiers when required.
* Implement a guarded monitoring agent workflow.
* Escalate exact-threshold cases separately.
* Prevent invalid data from reaching downstream processing.
* Require human approval before alerts are considered actionable.

---

#Project Structure

```text
CapstoneProject/
│
├── data/
│   ├── generate_dataset.py
│   ├── resellers.csv
│   ├── orders.csv
│   └── meesho_reseller.db
│
├── part1_sql/
│   ├── queries.sql
│   ├── run_queries.py
│   └── output/
│       └── *.csv
│
├── part2_engine/
│   ├── growth_engine.py
│   ├── test_growth_engine.py
│   └── fixtures/
│       ├── corrupted_feed.csv
│       └── monthly_category_revenue.csv
│
├── part3_narrative/
│   ├── prompt_pack.md
│   ├── narrative_report.md
│   ├── masking.py
│   └── test_masking.py
│
├── part4_agent/
│   ├── agent_spec.md
│   ├── mock_agent_runner.py
│   └── test_mock_agent_runner.py
│
└── README.md
```

---

#Pipeline Flow

```text
                 Raw Dataset
                     │
                     ▼
          ┌─────────────────────┐
          │ Part 1: SQL         │
          │ Analytics           │
          └─────────────────────┘
                     │
                     ▼
      monthly_category_revenue.csv
                     │
                     ▼
          ┌─────────────────────┐
          │ Part 2: Growth      │
          │ Engine              │
          └─────────────────────┘
                     │
                     ▼
             MoM Growth + Flags
                     │
                     ▼
          ┌─────────────────────┐
          │ Part 3: Narrative   │
          │ Intelligence        │
          └─────────────────────┘
                     │
                     ▼
              Business Insights
                     │
                     ▼
          ┌─────────────────────┐
          │ Part 4: Monitoring  │
          │ Agent               │
          └─────────────────────┘
                     │
                     ▼
          Alerts / Escalations
                     │
                     ▼
             Human Approval
```

---

#Part 1 — SQL Analytics

Part 1 generates a reproducible dataset containing:

* 24 resellers
* 900 orders
* Multiple product categories
* Monthly order and revenue information

The generated data is stored in:

```text
data/resellers.csv
data/orders.csv
data/meesho_reseller.db
```

SQL queries are used to calculate category-level monthly revenue and order counts.

The main downstream output is:

```text
part1_sql/output/monthly_category_revenue.csv
```

with the required columns:

```text
month
category
revenue
n_orders
```

---

#Part 2 — Growth Engine

Part 2 processes the monthly category revenue feed.

###Month-over-Month Formula

```text
MoM Growth (%) =
((Current Revenue - Previous Revenue) / Previous Revenue) × 100
```

The result is rounded to two decimal places.

###Flagging Logic

The default threshold is:

```text
8.0%
```

The engine uses three outcomes:

```text
abs(MoM) > 8.0
        ↓
flagged

abs(MoM) < 8.0
        ↓
not_flagged

abs(MoM) == 8.0
        ↓
escalate_exact_boundary
```

The engine also validates incoming CSV feeds and prevents corrupted data from entering downstream processing.

---

#Part 3 — Narrative Intelligence

Part 3 converts validated analytical results into concise business narratives.

It includes:

* Prompt design
* Narrative templates
* Worked examples
* Chart-selection guidance
* Reseller identifier masking

Example masking:

```text
RS019 → ALIAS-19
```

The masking tests ensure that raw reseller identifiers do not leak into generated narratives.

---

#Part 4 — Agentic Monitoring Workflow

Part 4 integrates the previous components into a guarded monitoring workflow.

The mock agent:

1. Validates the incoming feed.
2. Stops processing if validation fails.
3. Calculates MoM growth.
4. Identifies flagged categories.
5. Separates exact-threshold cases.
6. Sorts flagged categories by absolute growth.
7. Drafts messages for the top 3 flagged categories.
8. Suppresses remaining flagged categories.
9. Generates structured output.
10. Requires human approval before action.

###Safety/Guardrail Principle

```text
Invalid Feed
     ↓
HARD STOP
     ↓
No alerts
No narratives
No downstream processing
```

This prevents corrupted data from generating misleading alerts.

---

#Testing

The project includes tests for Parts 2–4.

##Run Part 2 Tests

```bash
python part2_engine/test_growth_engine.py
```

##Run Part 3 Tests

```bash
python part3_narrative/test_masking.py
```

##Run Part 4 Tests

```bash
python part4_agent/test_mock_agent_runner.py
```

##Run the Complete Test Suite

Install pytest if required:

```bash
python -m pip install pytest
```

Then run:

```bash
python -m pytest
```

All tests should pass before submitting the project.

---

#How to Run the Project

##1. Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/meesho-reseller-growth-alert-intelligence.git
```

Move into the project:

```bash
cd meesho-reseller-growth-alert-intelligence
```

---

##2. Generate the Dataset

```bash
python data/generate_dataset.py
```

This generates the required CSV files and SQLite database.

---

##3. Run Part 1

```bash
python part1_sql/run_queries.py
```

This executes the SQL analysis and generates the CSV outputs in:

```text
part1_sql/output/
```

---

##4. Run Part 2

```bash
python part2_engine/test_growth_engine.py
```

---

##5. Run Part 3

```bash
python part3_narrative/test_masking.py
```

---

##6. Run Part 4

```bash
python part4_agent/test_mock_agent_runner.py
```

---

##7. Run All Tests

```bash
python -m pytest
```

---

#Expected Acceptance Results

The project validates the following important scenarios.

###April → May: Ethnic Wear

```text
MoM Growth: 77.1%
Status: flagged
```

###May → June: Beauty & Personal Care

```text
MoM Growth: 5.67%
Status: not_flagged
```

###Exact Boundary

```text
Previous Revenue: 100000
Current Revenue: 108000
MoM Growth: 8.0%
Status: escalate_exact_boundary
```

###Corrupted Feed

The corrupted feed must be rejected with validation errors.

```text
line 3: negative revenue (-4200.0) for category=Western Wear
line 4: missing category (month=July)
line 6: missing revenue (category=Home & Kitchen)
```

No downstream alerts should be generated from the corrupted feed.

---

#Guardrails

The pipeline includes several controls:

* Input feed validation
* Negative revenue detection
* Missing category detection
* Missing revenue detection
* Exact-threshold escalation
* Top-3 alert drafting
* Suppression of lower-priority flagged categories
* Reseller identifier masking
* No downstream processing after hard-stop validation failure
* Human approval requirement

---

#Technologies Used

* **Python**
* **SQLite**
* **SQL**
* **CSV**
* **Pytest**
* **Markdown**
* **Git & GitHub**

---

#Key Output

The primary Part 1 → Part 2 interface is:

```text
part1_sql/output/monthly_category_revenue.csv
```

This file connects the SQL analytics stage with the growth engine and subsequent monitoring workflow.

