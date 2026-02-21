# polymarket-daytrader-bot

Base repository for a Polymarket day trader bot.

## Scope (Phase 01)
- Project skeleton for strategy, risk, execution, and integrations.
- Environment-based settings via `.env`.
- Runtime config via `config/default.yaml`.
- Baseline logging.
- Smoke test + lint/format tooling.

## Prerequisites
- Python 3.11+
- [uv](https://docs.astral.sh/uv/) (recommended)

## Quickstart
```bash
cp .env.example .env
UV_CACHE_DIR=/tmp/uv-cache uv sync --python 3.11 --extra dev
UV_CACHE_DIR=/tmp/uv-cache uv run pytest
UV_CACHE_DIR=/tmp/uv-cache uv run ruff check .
UV_CACHE_DIR=/tmp/uv-cache uv run ruff format --check .
```

## Tooling commands
```bash
uv run pytest
uv run ruff format .
uv run ruff check .
```

## Local run
```bash
UV_CACHE_DIR=/tmp/uv-cache uv run python -m polymarket_bot.main
```

## Project layout
```
src/polymarket_bot/
  config/
  core/
  strategies/
  risk/
  execution/
  integrations/
  data/
  utils/
config/default.yaml
tests/test_smoke.py
```
