"""Application entrypoint."""

from __future__ import annotations

import logging

from polymarket_bot.config.settings import load_settings
from polymarket_bot.utils.logger import configure_logging


def run() -> int:
    """Boot the app and confirm base components are wired."""
    settings, runtime_config = load_settings()
    configure_logging(settings.log_level)

    logger = logging.getLogger("polymarket_bot")
    logger.info("Starting %s in %s", settings.app_name, settings.environment)
    logger.info(
        "Runtime config loaded (strategy=%s, risk=%s, execution=%s, integrations=%s)",
        bool(runtime_config.strategy),
        bool(runtime_config.risk),
        bool(runtime_config.execution),
        bool(runtime_config.integrations),
    )
    return 0


def main() -> None:
    raise SystemExit(run())


if __name__ == "__main__":
    main()
