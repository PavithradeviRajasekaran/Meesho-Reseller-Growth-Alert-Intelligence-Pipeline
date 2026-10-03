from masking import alias_for, assert_no_raw_names_leak


def test_alias_for():
    assert alias_for("RS019") == "ALIAS-19"
    assert alias_for("RS006") == "ALIAS-06"


def test_no_raw_names_leak():
    reseller_names = [
        "Mumbai Reseller 1",
        "Mumbai Reseller 4",
        "Hyderabad Reseller 6",
        "Lucknow Reseller 6",
        "Jaipur Reseller 5"
    ]

    safe_text = """
    West — ALIAS-19
    West — ALIAS-22
    South — ALIAS-12
    North — ALIAS-06
    North — ALIAS-05
    """

    assert assert_no_raw_names_leak(
        safe_text,
        reseller_names
    ) is True


def test_raw_name_is_detected():
    reseller_names = [
        "Mumbai Reseller 1",
        "Mumbai Reseller 4",
        "Hyderabad Reseller 6",
        "Lucknow Reseller 6",
        "Jaipur Reseller 5"
    ]

    unsafe_text = """
    West — Mumbai Reseller 1
    """

    assert assert_no_raw_names_leak(
        unsafe_text,
        reseller_names
    ) is False


if __name__ == "__main__":
    test_alias_for()
    test_no_raw_names_leak()
    test_raw_name_is_detected()

    print("All masking tests passed.")