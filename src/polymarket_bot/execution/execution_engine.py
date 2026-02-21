"""Execution engine placeholders."""

from __future__ import annotations

from polymarket_bot.core.models import OrderIntent


class ExecutionEngine:
    """Order submission abstraction."""

    async def submit(self, intent: OrderIntent) -> dict[str, str]:
        # In phase 01 we only expose an interface contract.
        return {"status": "stub", "market_id": intent.market_id}
