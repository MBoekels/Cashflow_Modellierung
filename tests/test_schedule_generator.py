from datetime import date

import pytest

from services.schedule_generator import generate_cash_flow_schedule


def test_generate_cash_flow_schedule_bullet_loan():
    schedule = generate_cash_flow_schedule(
        product_name="Test Loan",
        notional=100_000,
        rate=0.05,
        term_years=1,
        start_date=date(2026, 1, 15),
        frequency="quarterly",
        currency="EUR",
    )

    assert len(schedule) == 5
    assert schedule[0].type == "interest"
    assert schedule[-1].type == "principal"
    assert schedule[-1].amount == 100_000
    assert schedule[-1].date == date(2027, 1, 15)


def test_generate_cash_flow_schedule_once_frequency_maturity():
    schedule = generate_cash_flow_schedule(
        product_name="Single Payment",
        notional=50_000,
        rate=0.04,
        term_years=1,
        start_date=date(2026, 1, 15),
        frequency="once",
        currency="USD",
    )

    assert len(schedule) == 2
    assert schedule[0].type == "interest"
    assert schedule[1].type == "principal"
    assert schedule[0].date == schedule[1].date
    assert schedule[1].date == date(2027, 1, 15)


def test_generate_cash_flow_schedule_invalid_term_raises():
    with pytest.raises(ValueError, match="Term years must be greater than zero"):
        generate_cash_flow_schedule(
            product_name="Invalid Loan",
            notional=100_000,
            rate=0.05,
            term_years=0,
            start_date=date(2026, 1, 15),
            frequency="annual",
            currency="EUR",
        )


def test_generate_cash_flow_schedule_invalid_frequency_raises():
    with pytest.raises(ValueError, match="Unsupported frequency"):
        generate_cash_flow_schedule(
            product_name="Unsupported",
            notional=100_000,
            rate=0.05,
            term_years=1,
            start_date=date(2026, 1, 15),
            frequency="weekly",  # invalid value
            currency="EUR",
        )
