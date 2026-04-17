from __future__ import annotations

from datetime import date
from typing import Iterable

from dateutil.relativedelta import relativedelta

from models.cash_flow import CashFlow
from models.product_template import BusinessDayConvention, DayCountConvention, Frequency
from services.date_utils import (
    adjust_business_day,
    day_count_fraction,
    generate_schedule_dates,
    frequency_to_months,
)


def validate_schedule_parameters(
    product_name: str,
    notional: float,
    rate: float,
    term_years: int,
    start_date: date,
    currency: str,
    frequency: Frequency,
) -> None:
    if not product_name or not product_name.strip():
        raise ValueError("Product name must not be empty.")
    if not isinstance(notional, (int, float)) or notional == 0:
        raise ValueError("Notional must be a non-zero numeric value.")
    if not isinstance(rate, (int, float)) or rate < 0:
        raise ValueError("Rate must be a non-negative numeric value.")
    if not isinstance(term_years, int) or term_years <= 0:
        raise ValueError("Term years must be greater than zero.")
    if not isinstance(start_date, date):
        raise ValueError("Start date must be a valid date.")
    if not currency or not currency.strip():
        raise ValueError("Currency code must not be empty.")

    months_per_period = frequency_to_months(frequency)
    if frequency != "once" and months_per_period <= 0:
        raise ValueError(f"Unsupported frequency: {frequency}")
    if frequency != "once" and (term_years * 12) % months_per_period != 0:
        raise ValueError(
            "Term years must be an exact multiple of the payment frequency interval."
        )


def generate_cash_flow_schedule(
    product_name: str,
    notional: float,
    rate: float,
    term_years: int,
    start_date: date,
    currency: str = "EUR",
    frequency: Frequency = "annual",
    day_count_convention: DayCountConvention = "30/360",
    business_day_convention: BusinessDayConvention = "modified_following",
    description: str = "",
    holidays: Iterable[date] | None = None,
) -> list[CashFlow]:
    validate_schedule_parameters(
        product_name,
        notional,
        rate,
        term_years,
        start_date,
        currency,
        frequency,
    )

    if frequency == "once":
        maturity_date = start_date + relativedelta(years=term_years)
        payment_dates = [
            adjust_business_day(maturity_date, business_day_convention, holidays)
        ]
    else:
        payment_dates = generate_schedule_dates(
            start_date,
            term_years,
            frequency,
            business_day_convention,
            holidays,
        )

    cash_flows: list[CashFlow] = []
    previous_date = start_date
    last_index = len(payment_dates) - 1
    for index, payment_date in enumerate(payment_dates):
        if payment_date < previous_date:
            raise ValueError("Cash flow dates must be in ascending order.")

        accrual_fraction = day_count_fraction(
            previous_date, payment_date, day_count_convention
        )
        interest_amount = notional * rate * accrual_fraction

        if interest_amount != 0:
            cash_flows.append(
                CashFlow(
                    product_name=product_name,
                    type="interest",
                    date=payment_date,
                    amount=interest_amount,
                    currency=currency,
                    description=description or "Interest payment",
                )
            )

        if index == last_index:
            cash_flows.append(
                CashFlow(
                    product_name=product_name,
                    type="principal",
                    date=payment_date,
                    amount=notional,
                    currency=currency,
                    description=description or "Principal repayment",
                )
            )
        previous_date = payment_date

    return sorted(cash_flows, key=lambda cash_flow: cash_flow.date)
