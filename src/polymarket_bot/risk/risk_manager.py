"""Risk management placeholders."""

from __future__ import annotations

from polymarket_bot.core.models import Position


class RiskManager:
    """Risk management interface."""

    def should_exit(self, position: Position, pnl_pct: float) -> bool:
        """TODO: implement exit decision using position state and pnl percentage."""
        _ = position, pnl_pct
        return False
