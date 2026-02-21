"""Strategy abstraction."""

from __future__ import annotations

from abc import ABC, abstractmethod

from polymarket_bot.core.models import MarketTick, OrderIntent


class BaseStrategy(ABC):
    """Base contract for strategy implementations."""

    @abstractmethod
    def on_tick(self, tick: MarketTick) -> OrderIntent | None:
        """Translate market data into an optional order intent."""
