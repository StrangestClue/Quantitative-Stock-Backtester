from config import *

def run_backtest(data):
    capital = INITIAL_CAPITAL
    shares = 0
    portfolio_values = []
    trades = []
    buy_price = None

    for _, row in data.iterrows():
        close_price = row["Close"]

        if row["Position"] == 1:
            shares = (
                capital *
                (1 - TRANSACTION_COST)
            ) / close_price
            capital = 0
            buy_price = close_price

        elif row["Position"] == -1:
            capital = (
                shares *
                close_price *
                (1 - TRANSACTION_COST)
            )

            shares = 0
            trades.append({
                "Buy": buy_price,
                "Sell": close_price,
                "Return":
                (
                    close_price -
                    buy_price
                ) / buy_price
            })
        
        portfolio_value = capital + shares * close_price
        portfolio_values.append(portfolio_value)

    data["Portfolio"] = portfolio_values

    return data, trades