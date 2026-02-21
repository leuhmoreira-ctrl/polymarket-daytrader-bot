"""Application entrypoint."""

from __future__ import annotations

import logging

from polymarket_bot.config.settings import load_settings
from polymarket_bot.utils.logger import configure_logging


def bootstrap() -> None:
    """Initialize base runtime dependencies."""
    settings, _ = load_settings()
    configure_logging(settings.log_level)


def run() -> int:
    """Run the application entrypoint."""
    bootstrap()
    logger = logging.getLogger("polymarket_bot")
    logger.info("started")
    return 0


def main() -> None:
    raise SystemExit(run())


if __name__ == "__main__":
    main()
