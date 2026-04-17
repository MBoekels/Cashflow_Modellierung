from datetime import date

from models.cash_flow import CashFlow
from services.portfolio import (
    aggregate_cash_flows_by_date_and_currency,
    merge_cash_flow_schedules,
    summarize_cash_flows,
)


def test_merge_cash_flow_schedules_combines_and_sorts():
    schedule_a = [
        CashFlow(
            product_name="Loan A",
            type="interest",
            date=date(2026, 1, 15),
            amount=250.0,
            currency="EUR",
            description="Interest payment",
        )
    ]
    schedule_b = [
        CashFlow(
            product_name="Loan B",
            type="principal",
            date=date(2026, 1, 1),
            amount=1000.0,
            currency="EUR",
            description="Principal repayment",
        )
    ]

    merged = merge_cash_flow_schedules(schedule_a, schedule_b)

    assert len(merged) == 2
    assert merged[0].date == date(2026, 1, 1)
    assert merged[0].product_name == "Loan B"
    assert merged[1].product_name == "Loan A"


def test_aggregate_cash_flows_by_date_and_currency_groups_amounts():
    schedule = [
        CashFlow(
            product_name="Loan A",
            type="interest",
            date=date(2026, 1, 15),
            amount=100.0,
            currency="EUR",
            description="Interest",
        ),
        CashFlow(
            product_name="Loan A",
            type="principal",
            date=date(2026, 1, 15),
            amount=-50.0,
            currency="EUR",
            description="Principal",
        ),
        CashFlow(
            product_name="Deposit",
            type="income",
            date=date(2026, 1, 15),
            amount=200.0,
            currency="USD",
            description="Deposit inflow",
        ),
    ]

    aggregated = aggregate_cash_flows_by_date_and_currency(schedule)

    assert aggregated == [
        {"date": date(2026, 1, 15), "currency": "EUR", "amount": 50.0},
        {"date": date(2026, 1, 15), "currency": "USD", "amount": 200.0},
    ]


def test_summarize_cash_flows_returns_totals_by_currency():
    schedule = [
        CashFlow(
            product_name="Loan A",
            type="interest",
            date=date(2026, 1, 15),
            amount=100.0,
            currency="EUR",
            description="Interest",
        ),
        CashFlow(
            product_name="Loan A",
            type="principal",
            date=date(2026, 1, 15),
            amount=-25.0,
            currency="EUR",
            description="Principal",
        ),
        CashFlow(
            product_name="Deposit",
            type="income",
            date=date(2026, 1, 15),
            amount=50.0,
            currency="USD",
            description="Deposit inflow",
        ),
    ]

    summary = summarize_cash_flows(schedule)

    assert summary == {
        "EUR": {"total_inflow": 100.0, "total_outflow": -25.0, "net": 75.0},
        "USD": {"total_inflow": 50.0, "total_outflow": 0.0, "net": 50.0},
    }
