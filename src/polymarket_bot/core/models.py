"""Core, framework-agnostic models."""

from __future__ import annotations

from dataclasses import dataclass
from decimal import Decimal


@dataclass(slots=True)
class Market:
    """Market snapshot model."""

    market_id: str
    question: str
    best_bid: Decimal
    best_ask: Decimal


@dataclass(slots=True)
class Position:
    """Open position model."""

    market_id: str
    side: str
    size: Decimal
    average_price: Decimal


@dataclass(slots=True)
class Signal:
    """Strategy signal model."""

    market_id: str
    action: str
    confidence: float | None = None


@dataclass(slots=True)
class Order:
    """Order intent model."""

    market_id: str
    side: str
    price: Decimal
    size: Decimal
