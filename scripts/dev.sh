#!/usr/bin/env bash
set -euo pipefail

UV_CACHE_DIR="${UV_CACHE_DIR:-/tmp/uv-cache}"

uv sync --python 3.11 --extra dev
uv run ruff check .
uv run ruff format --check .
uv run pytest
