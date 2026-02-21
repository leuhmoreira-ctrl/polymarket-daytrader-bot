"""Websocket market data listener placeholder."""

from __future__ import annotations

import websockets


class MarketListener:
    def __init__(self, websocket_url: str) -> None:
        self.websocket_url = websocket_url

    async def ping(self) -> bool:
        async with websockets.connect(self.websocket_url) as conn:
            await conn.ping()
        return True
