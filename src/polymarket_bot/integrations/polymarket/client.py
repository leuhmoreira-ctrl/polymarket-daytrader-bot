"""Polymarket API client placeholder."""

from __future__ import annotations


class PolymarketClient:
    """Polymarket integration stub."""

    def __init__(self, base_url: str, timeout_seconds: float = 10.0) -> None:
        self.base_url = base_url
        self.timeout_seconds = timeout_seconds

    async def get_market(self, market_id: str) -> dict[str, object]:
        """TODO: implement Polymarket API fetch for market details."""
        _ = market_id
        return {}

    async def close(self) -> None:
        """TODO: implement adapter cleanup if needed."""
