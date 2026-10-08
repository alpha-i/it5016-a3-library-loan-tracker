"""Concept example: keep a business rule in a small, testable function."""

from decimal import Decimal


def calculate_late_fee(
    days_overdue: int,
    daily_rate: Decimal = Decimal("0.50"),
) -> Decimal:
    """Calculate a hypothetical fee of 50 cents per overdue day."""
    if days_overdue < 0:
        raise ValueError("Days overdue cannot be negative.")
    if daily_rate < 0:
        raise ValueError("Daily rate cannot be negative.")

    # This function depends only on its arguments and does not print,
    # request input, or modify shared state.
    return daily_rate * days_overdue


if __name__ == '__main__':
    example_fee = calculate_late_fee(3)
    print(f"Hypothetical fee for 3 overdue days: ${example_fee:.2f}")
