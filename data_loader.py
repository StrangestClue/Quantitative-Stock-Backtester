import yfinance as yf

def download_data(ticker, start, end):

    data = yf.download(
        ticker,
        start=start,
        end=end
    )

    data.columns = data.columns.droplevel(1)

    return data