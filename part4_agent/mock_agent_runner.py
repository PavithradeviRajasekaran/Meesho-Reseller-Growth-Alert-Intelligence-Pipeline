import csv
import json
import os
import sys


# Make the project root importable
PROJECT_ROOT = os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))
)

if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)


# Import Part 2 functions - do NOT reimplement them
from part2_engine.growth_engine import (
    validate_feed,
    mom_growth,
    is_flagged
)

# Import Part 3 deterministic narrative function
from part3_narrative.narrative_template import (
    fill_narrative_template
)


PREVIOUS_MONTH = {
    "May": "April",
    "June": "May",
    "July": "June"
}


def load_month_data(csv_path: str, wanted_month: str) -> dict:
    """
    Load revenue values for one requested month.

    Returns:
        {
            "Ethnic Wear": 104520.77,
            ...
        }
    """

    data = {}

    with open(csv_path, "r", newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)

        for row in reader:
            if row["month"] == wanted_month:
                category = row["category"]
                revenue = float(row["revenue"])

                data[category] = revenue

    return data


def hard_stop_result(month: str, errors: list[str]) -> dict:
    """
    Build the required JSON structure for an invalid run.
    """

    return {
        "run_month": month,
        "validation_status": "invalid",
        "validation_errors": errors,
        "flagged_categories": [],
        "suppressed_categories": [],
        "escalated_categories": [],
        "action_taken": "hard_stop"
    }


def run(
    month: str,
    previous_month_csv: str,
    current_month_csv: str
) -> dict:

    # --------------------------------------------------
    # Step 1: Validate input feeds
    # --------------------------------------------------

    previous_valid, previous_errors = validate_feed(
        previous_month_csv
    )

    current_valid, current_errors = validate_feed(
        current_month_csv
    )

    validation_errors = (
        previous_errors + current_errors
    )

    # --------------------------------------------------
    # Step 2: Hard Stop if invalid
    # --------------------------------------------------

    if not previous_valid or not current_valid:
        result = hard_stop_result(
            month,
            validation_errors
        )

        print(json.dumps(result, indent=4))

        return result

    # Determine previous month
    if month not in PREVIOUS_MONTH:
        raise ValueError(
            f"Unsupported run month: {month}"
        )

    prev_month = PREVIOUS_MONTH[month]

    # --------------------------------------------------
    # Step 3: Load monthly data
    # --------------------------------------------------

    previous_data = load_month_data(
        previous_month_csv,
        prev_month
    )

    current_data = load_month_data(
        current_month_csv,
        month
    )

    flagged = []
    escalated_categories = []

    # --------------------------------------------------
    # Steps 3 and 4:
    # calculate MoM and classify
    # --------------------------------------------------

    for category, current_revenue in current_data.items():

        if category not in previous_data:
            continue

        previous_revenue = previous_data[category]

        mom_pct = mom_growth(
            previous_revenue,
            current_revenue
        )

        status = is_flagged(mom_pct)

        if status == "flagged":
            flagged.append(
                {
                    "category": category,
                    "mom_pct": mom_pct,
                    "previous_revenue": previous_revenue,
                    "current_revenue": current_revenue
                }
            )

        elif status == "escalate_exact_boundary":
            escalated_categories.append(category)

    # --------------------------------------------------
    # Step 5:
    # Sort largest absolute movement first
    # --------------------------------------------------

    flagged.sort(
        key=lambda item: abs(item["mom_pct"]),
        reverse=True
    )

    # Top 3 get drafted
    top_three = flagged[:3]

    # Remaining flagged categories are suppressed
    remaining = flagged[3:]

    flagged_categories = []

    # --------------------------------------------------
    # Step 6:
    # Draft at most three messages
    # --------------------------------------------------

    for item in top_three:

        message = fill_narrative_template(
            category=item["category"],
            previous_revenue=item["previous_revenue"],
            current_revenue=item["current_revenue"],
            mom_pct=item["mom_pct"],
            month=month,
            prev_month=prev_month
        )

        flagged_categories.append(
            {
                "category": item["category"],
                "mom_pct": item["mom_pct"],
                "previous_revenue": item[
                    "previous_revenue"
                ],
                "current_revenue": item[
                    "current_revenue"
                ],
                "drafted": True,
                "message": message
            }
        )

    # --------------------------------------------------
    # Step 7:
    # Suppress remaining flagged categories
    # --------------------------------------------------

    suppressed_categories = [
        item["category"]
        for item in remaining
    ]

    # --------------------------------------------------
    # Step 8:
    # Structured JSON result
    # --------------------------------------------------

    result = {
        "run_month": month,
        "validation_status": "valid",
        "validation_errors": [],
        "flagged_categories": flagged_categories,
        "suppressed_categories": suppressed_categories,
        "escalated_categories": escalated_categories,
        "action_taken":
            "drafted_and_held_for_approval"
    }

    print(json.dumps(result, indent=4))

    return result


if __name__ == "__main__":

    monthly_file = os.path.join(
        PROJECT_ROOT,
        "part1_sql",
        "output",
        "monthly_category_revenue.csv"
    )

    print("\nMAY RUN")
    print("-------")

    run(
        "May",
        monthly_file,
        monthly_file
    )

    print("\nJUNE RUN")
    print("--------")

    run(
        "June",
        monthly_file,
        monthly_file
    )