from __future__ import annotations

from datetime import date, timedelta
from typing import Iterable, Literal

from dateutil.relativedelta import relativedelta

DayCountConvention = Literal["30/360", "actual/360", "actual/365", "actual/actual"]
BusinessDayConvention = Literal["following", "modified_following", "preceding", "none"]
Frequency = Literal["annual", "semiannual", "quarterly", "monthly", "once"]

DEFAULT_HOLIDAYS: frozenset[date] = frozenset()


def is_business_day(check_date: date, holidays: Iterable[date] | None = None) -> bool:
    if holidays is None:
        holidays = DEFAULT_HOLIDAYS
    return check_date.weekday() < 5 and check_date not in set(holidays)


def get_following_business_day(check_date: date, holidays: Iterable[date] | None = None) -> date:
    holidays = set(holidays or DEFAULT_HOLIDAYS)
    result = check_date
    while not is_business_day(result, holidays):
        result += timedelta(days=1)
    return result


def get_preceding_business_day(check_date: date, holidays: Iterable[date] | None = None) -> date:
    holidays = set(holidays or DEFAULT_HOLIDAYS)
    result = check_date
    while not is_business_day(result, holidays):
        result -= timedelta(days=1)
    return result


def adjust_business_day(check_date: date, convention: BusinessDayConvention, holidays: Iterable[date] | None = None) -> date:
    if convention == "none":
        return check_date
    if convention == "following":
        return get_following_business_day(check_date, holidays)
    if convention == "preceding":
        return get_preceding_business_day(check_date, holidays)
    if convention == "modified_following":
        adjusted = get_following_business_day(check_date, holidays)
        if adjusted.month != check_date.month:
            return get_preceding_business_day(check_date, holidays)
        return adjusted
    raise ValueError(f"Unsupported business day convention: {convention}")


def day_count_fraction(start: date, end: date, convention: DayCountConvention = "30/360") -> float:
    if end < start:
        raise ValueError("End date must be on or after start date.")
    if convention == "30/360":
        d1 = min(start.day, 30)
        d2 = min(end.day, 30) if d1 == 30 else end.day
        return (
            360 * (end.year - start.year)
            + 30 * (end.month - start.month)
            + (d2 - d1)
        ) / 360.0
    if convention == "actual/360":
        return (end - start).days / 360.0
    if convention == "actual/365":
        return (end - start).days / 365.0
    if convention == "actual/actual":
        return (end - start).days / 365.25
    raise ValueError(f"Unsupported day count convention: {convention}")


def frequency_to_months(frequency: Frequency) -> int:
    mapping: dict[Frequency, int] = {
        "annual": 12,
        "semiannual": 6,
        "quarterly": 3,
        "monthly": 1,
        "once": 0,
    }
    if frequency not in mapping:
        raise ValueError(f"Unsupported frequency: {frequency}")
    return mapping[frequency]


def generate_schedule_dates(
    start_date: date,
    term_years: int,
    frequency: Frequency = "annual",
    business_day_convention: BusinessDayConvention = "modified_following",
    holidays: Iterable[date] | None = None,
) -> list[date]:
    if term_years <= 0:
        raise ValueError("Term years must be greater than zero.")
    if frequency == "once":
        return [adjust_business_day(start_date, business_day_convention, holidays)]

    months_per_period = frequency_to_months(frequency)
    if months_per_period <= 0:
        raise ValueError("Frequency must specify a positive interval.")

    total_periods = int(term_years * 12 / months_per_period)
    if total_periods <= 0:
        raise ValueError("Total periods must be greater than zero for the given term and frequency.")

    schedule: list[date] = []
    for period_index in range(1, total_periods + 1):
        payment_date = start_date + relativedelta(months=months_per_period * period_index)
        payment_date = adjust_business_day(payment_date, business_day_convention, holidays)
        schedule.append(payment_date)
    return schedule
