import numpy as np
from config import *

def calculate_metrics(data, trades):
    buy_signals = (
        data["Position"] == 1
    ).sum()
    sell_signals = (
        data["Position"] == -1
    ).sum()

    wins = sum(
        1
        for trade in trades
        if trade["Return"] > 0
    )

    win_rate = wins / len(trades)
    rolling_max = data["Portfolio"].cummax()
    drawdown = (data["Portfolio"] - rolling_max) / rolling_max
    max_drawdown = drawdown.min()
    data["Daily_Return"] = (data["Portfolio"].pct_change())
    sharpe = (data["Daily_Return"].mean() / data["Daily_Return"].std()) * np.sqrt(252)
    buy_hold = (data["Close"] / data["Close"].iloc[0]) * INITIAL_CAPITAL

    return {
        "Buy Signals": buy_signals,
        "Sell Signals": sell_signals,
        "Win Rate": win_rate,
        "Sharpe": sharpe,
        "Drawdown": max_drawdown,
        "Final Portfolio":
        data["Portfolio"].iloc[-1],
        "Buy Hold":
        buy_hold.iloc[-1]

    }