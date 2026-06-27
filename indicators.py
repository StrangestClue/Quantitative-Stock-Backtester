from config import *


def add_indicators(data):
    # Moving Averages

    data["MA20"] = data["Close"].rolling(FAST_MA).mean()
    data["MA50"] = data["Close"].rolling(SLOW_MA).mean()

    # MA Features
    data["Spread"] = data["MA20"] - data["MA50"]
    data["Scale20"] = data["MA20"].diff().fillna(0)
    data["Scale50"] = data["MA50"].diff().fillna(0)

    # RSI
    delta = data["Close"].diff()
    gain = delta.clip(lower=0)
    loss = -delta.clip(upper=0)
    avg_gain = gain.rolling(RSI_PERIOD).mean()
    avg_loss = loss.rolling(RSI_PERIOD).mean()
    rs = avg_gain / avg_loss
    data["RSI"] = 100 - (100 / (1 + rs))

    # Bollinger Bands
    sd = data["Close"].rolling(FAST_MA).std()
    data["Upper_Band"] = data["MA20"] + 2 * sd
    data["Lower_Band"] = data["MA20"] - 2 * sd
    return data