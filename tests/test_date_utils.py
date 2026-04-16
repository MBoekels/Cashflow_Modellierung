from datetime import date

from services.date_utils import (
    adjust_business_day,
    day_count_fraction,
    generate_schedule_dates,
)


def test_adjust_business_day_modified_following_weekend():
    friday = date(2026, 4, 17)
    adjusted = adjust_business_day(friday, "modified_following")
    assert adjusted == friday


def test_adjust_business_day_modified_following_month_end():
    sunday = date(2026, 8, 30)  # Sunday, but modified following should move to preceding because next business day is in next month
    adjusted = adjust_business_day(sunday, "modified_following")
    assert adjusted.weekday() < 5
    assert adjusted.month == sunday.month


def test_day_count_fraction_30_360():
    start = date(2026, 1, 15)
    end = date(2026, 4, 15)
    fraction = day_count_fraction(start, end, "30/360")
    assert fraction == 0.25


def test_generate_schedule_dates_quarterly():
    schedule = generate_schedule_dates(date(2026, 1, 15), term_years=1, frequency="quarterly")
    assert len(schedule) == 4
    assert schedule[0].month == 4
    assert schedule[-1].month == 1
    assert schedule[-1].year == 2027
