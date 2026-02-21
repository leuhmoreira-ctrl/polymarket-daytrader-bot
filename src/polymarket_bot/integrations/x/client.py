"""X API client placeholder."""

from __future__ import annotations

import httpx


class XClient:
    def __init__(self, base_url: str, timeout_seconds: float = 10.0) -> None:
        self._client = httpx.AsyncClient(base_url=base_url, timeout=timeout_seconds)

    async def healthcheck(self) -> bool:
        response = await self._client.get("/2/users/me")
        return response.status_code in {200, 401}

    async def close(self) -> None:
        await self._client.aclose()
