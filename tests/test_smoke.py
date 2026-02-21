from polymarket_bot.main import run


def test_smoke_run_returns_zero() -> None:
    assert run() == 0
