"""Core, framework-agnostic models."""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime
from decimal import Decimal


@dataclass(slots=True)
class MarketTick:
    market_id: str
    best_bid: Decimal
    best_ask: Decimal
    timestamp: datetime


@dataclass(slots=True)
class OrderIntent:
    market_id: str
    side: str
    price: Decimal
    quantity: Decimal
    created_at: datetime
