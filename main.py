from config import *
from data_loader import download_data
from indicators import add_indicators
from strategies import moving_average_strategy
from backtester import run_backtest
from metrics import calculate_metrics
from visualization import plot_results

def main():
    data = download_data(
        TICKER,
        START_DATE,
        END_DATE
    )

    data = add_indicators(data)
    data = moving_average_strategy(data)
    data, trades = run_backtest(data)

    results = calculate_metrics(
        data,
        trades
    )

    print()
    print("=" * 50)
    print("RESULTS")
    print("=" * 50)

    for key, value in results.items():
        print(f"{key}: {value}")
    plot_results(data)


if __name__ == "__main__":
    main()