"""Polymarket API client placeholder."""

from __future__ import annotations

from collections.abc import Mapping
from typing import Any

import httpx


class PolymarketClient:
    def __init__(self, base_url: str, timeout_seconds: float = 10.0) -> None:
        self._client = httpx.AsyncClient(base_url=base_url, timeout=timeout_seconds)

    async def get_market(self, market_id: str) -> Mapping[str, Any]:
        response = await self._client.get(f"/markets/{market_id}")
        response.raise_for_status()
        payload = response.json()
        if not isinstance(payload, Mapping):
            return {}
        return payload

    async def close(self) -> None:
        await self._client.aclose()
