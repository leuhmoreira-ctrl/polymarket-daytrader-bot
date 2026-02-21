"""Settings and runtime config loaders."""

from __future__ import annotations

from pathlib import Path
from typing import Any

import yaml
from pydantic import BaseModel, Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Environment-backed settings loaded from `.env` and process env vars."""

    app_name: str = "polymarket-daytrader-bot"
    environment: str = "dev"
    log_level: str = "INFO"
    config_path: Path = Path("config/default.yaml")

    model_config = SettingsConfigDict(
        env_file=".env",
        env_prefix="BOT_",
        extra="ignore",
    )


class RuntimeConfig(BaseModel):
    """YAML runtime config grouped by domain."""

    strategy: dict[str, Any] = Field(default_factory=dict)
    risk: dict[str, Any] = Field(default_factory=dict)
    execution: dict[str, Any] = Field(default_factory=dict)
    integrations: dict[str, Any] = Field(default_factory=dict)


def load_runtime_config(path: Path) -> RuntimeConfig:
    """Load `config/*.yaml` into a validated runtime config model."""
    if not path.exists():
        return RuntimeConfig()

    with path.open("r", encoding="utf-8") as handle:
        payload = yaml.safe_load(handle) or {}

    if not isinstance(payload, dict):
        raise ValueError("Runtime config file must contain a top-level mapping.")

    return RuntimeConfig.model_validate(payload)


def load_settings() -> tuple[Settings, RuntimeConfig]:
    settings = Settings()
    runtime_config = load_runtime_config(settings.config_path)
    return settings, runtime_config
