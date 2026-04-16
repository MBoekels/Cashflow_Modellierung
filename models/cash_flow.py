from __future__ import annotations

from dataclasses import dataclass
from datetime import date
from typing import Literal

CashFlowType = Literal["payment", "principal", "interest", "fee", "income", "other"]


@dataclass(frozen=True)
class CashFlow:
    product_name: str
    type: CashFlowType
    date: date
    amount: float
    currency: str
    description: str
