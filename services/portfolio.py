from __future__ import annotations

from collections import defaultdict
from datetime import date
from typing import Iterable

from models.cash_flow import CashFlow


def merge_cash_flow_schedules(*schedules: Iterable[CashFlow]) -> list[CashFlow]:
    """Merge multiple cash flow schedules into a single sorted list."""
    merged = [cash_flow for schedule in schedules for cash_flow in schedule]
    return sorted(merged, key=lambda cash_flow: (cash_flow.date, cash_flow.product_name, cash_flow.type))


def aggregate_cash_flows_by_date_and_currency(
    schedule: Iterable[CashFlow],
) -> list[dict[str, object]]:
    """Aggregate cash flow amounts by date and currency."""
    aggregation: dict[tuple[date, str], float] = defaultdict(float)
    for cash_flow in schedule:
        aggregation[(cash_flow.date, cash_flow.currency)] += cash_flow.amount

    return [
        {
            "date": cash_flow_date,
            "currency": currency,
            "amount": round(amount, 2),
        }
        for (cash_flow_date, currency), amount in sorted(
            aggregation.items(), key=lambda item: (item[0][0], item[0][1])
        )
    ]


def summarize_cash_flows(schedule: Iterable[CashFlow]) -> dict[str, dict[str, float]]:
    """Calculate total inflows, outflows, and net amounts per currency."""
    summary: dict[str, dict[str, float]] = defaultdict(
        lambda: {"total_inflow": 0.0, "total_outflow": 0.0, "net": 0.0}
    )

    for cash_flow in schedule:
        amount = float(cash_flow.amount)
        if amount >= 0:
            summary[cash_flow.currency]["total_inflow"] += amount
        else:
            summary[cash_flow.currency]["total_outflow"] += amount
        summary[cash_flow.currency]["net"] += amount

    return {currency: values for currency, values in summary.items()}
