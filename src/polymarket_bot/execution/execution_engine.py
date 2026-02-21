"""Execution engine placeholders."""

from __future__ import annotations

from polymarket_bot.core.models import Order


class ExecutionEngine:
    """Order submission abstraction."""

    async def place_order(self, order: Order) -> str:
        """TODO: implement order placement in exchange adapter."""
        _ = order
        return "stub-order-id"
