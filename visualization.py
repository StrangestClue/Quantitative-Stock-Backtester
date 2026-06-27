import matplotlib.pyplot as plt


def plot_results(data):

    # -------------------------
    # Strategy vs Buy & Hold
    # -------------------------
    portfolio = (data["Portfolio"] / data["Portfolio"].iloc[0])
    stock = (data["Close"] / data["Close"].iloc[0])
    plt.figure(figsize=(12,6))
    plt.plot(
        data.index,
        portfolio,
        label="Strategy"
    )
    plt.plot(
        data.index,
        stock,
        label="Buy & Hold"
    )
    plt.legend()
    plt.title("Strategy vs Buy & Hold")

    # -------------------------
    # Price + RSI
    # -------------------------
    fig, (ax1, ax2) = plt.subplots(
        2,
        1,
        figsize=(12,8),
        sharex=True
    )
    ax1.plot(data.index, data["Close"], label="Close")
    ax1.plot(data.index, data["MA20"], label="MA20")
    ax1.plot(data.index, data["MA50"], label="MA50")
    ax1.legend()
    ax1.set_title("Price")
    ax2.plot(data.index, data["RSI"])
    ax2.axhline(70, linestyle="--")
    ax2.axhline(30, linestyle="--")
    ax2.set_title("RSI")

    # -------------------------
    # Bollinger Bands
    # -------------------------
    plt.figure(figsize=(12,6))
    plt.plot(data.index, data["Close"])
    plt.plot(data.index, data["MA20"])
    plt.plot(data.index, data["Upper_Band"])
    plt.plot(data.index, data["Lower_Band"])

    plt.fill_between(
        data.index,
        data["Upper_Band"],
        data["Lower_Band"],
        alpha=0.2
    )
    plt.title("Bollinger Bands")

    plt.show()