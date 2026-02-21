"""Settings and runtime config loaders."""

from __future__ import annotations

from pathlib import Path

import yaml
from pydantic import BaseModel, Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Environment-backed settings loaded from `.env` and process env vars."""

    polymarket_api_key: str = ""
    news_api_key: str = ""
    x_api_key: str = ""
    log_level: str = "INFO"
    config_path: Path = Path("config/default.yaml")

    model_config = SettingsConfigDict(
        env_file=".env",
        extra="ignore",
    )


class RiskConfig(BaseModel):
    """Risk controls for day-trade operation."""

    stop_loss_pct: float = 0.001
    take_profit_pct: float = 0.0015
    max_position_usd: float = 100.0
    max_open_positions: int = 3


class ExecutionConfig(BaseModel):
    """Execution runtime controls."""

    poll_interval_ms: int = 250


class IntegrationConfig(BaseModel):
    """Single integration placeholder config."""

    base_url: str = ""
    api_key_env: str = ""


class IntegrationsConfig(BaseModel):
    """Group all integration placeholder configs."""

    polymarket: IntegrationConfig = Field(default_factory=IntegrationConfig)
    news: IntegrationConfig = Field(default_factory=IntegrationConfig)
    x: IntegrationConfig = Field(default_factory=IntegrationConfig)


class RuntimeConfig(BaseModel):
    """YAML runtime config grouped by domain."""

    risk: RiskConfig = Field(default_factory=RiskConfig)
    execution: ExecutionConfig = Field(default_factory=ExecutionConfig)
    integrations: IntegrationsConfig = Field(default_factory=IntegrationsConfig)


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
    """Load env settings and YAML runtime config."""
    settings = Settings()
    runtime_config = load_runtime_config(settings.config_path)
    return settings, runtime_config
