"""Risk management placeholders."""

from __future__ import annotations

from decimal import Decimal

from polymarket_bot.config.settings import RuntimeConfig
from polymarket_bot.core.models import OrderIntent


class RiskManager:
    """Apply simple risk gates before execution."""

    def __init__(self, runtime_config: RuntimeConfig) -> None:
        self._runtime_config = runtime_config

    def allow_order(self, intent: OrderIntent) -> bool:
        max_notional = Decimal(str(self._runtime_config.risk.get("max_notional_usd", 100.0)))
        notional = intent.price * intent.quantity
        return notional <= max_notional
