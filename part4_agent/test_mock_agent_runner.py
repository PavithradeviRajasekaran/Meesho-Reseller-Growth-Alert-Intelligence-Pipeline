import os
import sys


PROJECT_ROOT = os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))
)

if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)


from part4_agent.mock_agent_runner import run


MONTHLY_FILE = os.path.join(
    PROJECT_ROOT,
    "part1_sql",
    "output",
    "monthly_category_revenue.csv"
)

CORRUPTED_FILE = os.path.join(
    PROJECT_ROOT,
    "part2_engine",
    "fixtures",
    "corrupted_feed.csv"
)


def test_may_run():

    result = run(
        "May",
        MONTHLY_FILE,
        MONTHLY_FILE
    )

    assert result["validation_status"] == "valid"

    assert result["validation_errors"] == []

    assert len(
        result["flagged_categories"]
    ) == 3

    categories = [
        item["category"]
        for item in result["flagged_categories"]
    ]

    assert categories == [
        "Ethnic Wear",
        "Western Wear",
        "Kids Wear"
    ]

    percentages = [
        item["mom_pct"]
        for item in result["flagged_categories"]
    ]

    assert percentages == [
        77.1,
        -23.6,
        -23.48
    ]

    for item in result["flagged_categories"]:
        assert item["drafted"] is True

        assert item["category"] in item["message"]

        assert str(
            item["mom_pct"]
        ) in item["message"]

    assert set(
        result["suppressed_categories"]
    ) == {
        "Beauty & Personal Care",
        "Home & Kitchen"
    }

    assert result["escalated_categories"] == []

    assert (
        result["action_taken"]
        == "drafted_and_held_for_approval"
    )


def test_june_run():

    result = run(
        "June",
        MONTHLY_FILE,
        MONTHLY_FILE
    )

    assert result["validation_status"] == "valid"

    assert len(
        result["flagged_categories"]
    ) == 3

    categories = [
        item["category"]
        for item in result["flagged_categories"]
    ]

    assert categories == [
        "Ethnic Wear",
        "Home & Kitchen",
        "Kids Wear"
    ]

    percentages = [
        item["mom_pct"]
        for item in result["flagged_categories"]
    ]

    assert percentages == [
        -58.74,
        42.59,
        23.9
    ]

    assert result[
        "suppressed_categories"
    ] == [
        "Western Wear"
    ]

    assert (
        "Beauty & Personal Care"
        not in result["suppressed_categories"]
    )

    assert result["escalated_categories"] == []


def test_corrupted_feed_hard_stop():

    result = run(
        "July",
        MONTHLY_FILE,
        CORRUPTED_FILE
    )

    assert result[
        "validation_status"
    ] == "invalid"

    assert result[
        "action_taken"
    ] == "hard_stop"

    expected_errors = [
        (
            "line 3: negative revenue (-4200.0) "
            "for category=Western Wear"
        ),
        "line 4: missing category (month=July)",
        (
            "line 6: missing revenue "
            "(category=Home & Kitchen)"
        )
    ]

    assert result[
        "validation_errors"
    ] == expected_errors

    assert result[
        "flagged_categories"
    ] == []

    assert result[
        "suppressed_categories"
    ] == []

    assert result[
        "escalated_categories"
    ] == []


if __name__ == "__main__":

    test_may_run()

    test_june_run()

    test_corrupted_feed_hard_stop()

    print(
        "\nAll Part 4 agent tests passed."
    )