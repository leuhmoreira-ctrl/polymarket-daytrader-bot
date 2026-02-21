"""Strategy abstraction."""

from __future__ import annotations

from abc import ABC, abstractmethod

from polymarket_bot.core.models import Market, Signal


class Strategy(ABC):
    """Base contract for strategy implementations."""

    @abstractmethod
    def generate_signal(self, market_state: Market) -> Signal | None:
        """TODO: implement signal generation based on market state."""
