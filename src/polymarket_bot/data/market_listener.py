"""Websocket market data listener placeholder."""

from __future__ import annotations


class MarketListener:
    """Market listener stub."""

    def __init__(self, source: str = "polymarket") -> None:
        self.source = source

    async def start(self) -> None:
        """TODO: implement stream subscription and event dispatch."""
