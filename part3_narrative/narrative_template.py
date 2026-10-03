def fill_narrative_template(
    category: str,
    previous_revenue: float,
    current_revenue: float,
    mom_pct: float,
    month: str,
    prev_month: str
) -> str:
    """
    Deterministic offline narrative generator.

    It uses only values supplied by Part 1 / Part 2.
    No API, LLM, or network connection is required.
    """

    message = (
        f"Context: {category} revenue is being compared for "
        f"{month} vs {prev_month}. "
        f"Insight — Fact: revenue moved from INR {previous_revenue} "
        f"to INR {current_revenue}, a {mom_pct}% MoM change. "
        f"Implication — Hypothesis: review product-level and "
        f"channel-level activity for {category} before taking action."
    )

    return message