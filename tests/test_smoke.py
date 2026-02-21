import polymarket_bot
from polymarket_bot.main import run


def test_smoke_run_returns_zero() -> None:
    assert polymarket_bot.__version__
    assert run() == 0
