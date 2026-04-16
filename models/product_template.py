from __future__ import annotations

from dataclasses import dataclass, field
from datetime import date
from typing import Literal

DayCountConvention = Literal["30/360", "actual/360", "actual/365", "actual/actual"]
BusinessDayConvention = Literal["following", "modified_following", "preceding", "none"]

Frequency = Literal["annual", "semiannual", "quarterly", "monthly", "once"]


@dataclass(frozen=True)
class ProductTemplate:
    product_name: str
    product_type: str
    notional: float
    rate: float
    term_years: int
    start_date: date
    currency: str = "EUR"
    frequency: Frequency = "annual"
    day_count_convention: DayCountConvention = "30/360"
    business_day_convention: BusinessDayConvention = "modified_following"
    description: str = ""
    metadata: dict[str, str] = field(default_factory=dict)
