import os

from growth_engine import (
    mom_growth,
    is_flagged,
    validate_feed
)


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
FIXTURES_DIR = os.path.join(BASE_DIR, "fixtures")


def test_ethnic_wear_april_to_may():
    # GIVEN April -> May Ethnic Wear revenue
    previous = 104520.77
    current = 185107.61

    # WHEN
    mom_pct = mom_growth(previous, current)
    result = is_flagged(mom_pct)

    # THEN
    assert mom_pct == 77.1
    assert result == "flagged"


def test_beauty_personal_care_may_to_june():
    # GIVEN May -> June Beauty & Personal Care revenue
    previous = 35542.11
    current = 37559.07

    # WHEN
    mom_pct = mom_growth(previous, current)
    result = is_flagged(mom_pct)

    # THEN
    assert mom_pct == 5.67
    assert result == "not_flagged"


def test_exact_threshold_boundary():
    # GIVEN exactly 8% growth
    previous = 100000
    current = 108000

    # WHEN
    mom_pct = mom_growth(previous, current)
    result = is_flagged(mom_pct)

    # THEN
    assert mom_pct == 8.0
    assert result == "escalate_exact_boundary"


def test_corrupted_feed():
    # GIVEN corrupted CSV fixture
    csv_path = os.path.join(
        FIXTURES_DIR,
        "corrupted_feed.csv"
    )

    # WHEN
    valid, errors = validate_feed(csv_path)

    # THEN
    assert valid is False

    expected_errors = [
        "line 3: negative revenue (-4200.0) for category=Western Wear",
        "line 4: missing category (month=July)",
        "line 6: missing revenue (category=Home & Kitchen)"
    ]

    assert errors == expected_errors


def test_valid_monthly_category_feed():
    # GIVEN validated Part 1 CSV
    csv_path = os.path.join(
        FIXTURES_DIR,
        "monthly_category_revenue.csv"
    )

    # WHEN
    valid, errors = validate_feed(csv_path)

    # THEN
    assert valid is True
    assert errors == []


if __name__ == "__main__":
    test_ethnic_wear_april_to_may()
    test_beauty_personal_care_may_to_june()
    test_exact_threshold_boundary()
    test_corrupted_feed()
    test_valid_monthly_category_feed()

    print("All Part 2 tests passed.")
    