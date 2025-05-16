import yfinance as yf

def fetch_stock_data(ticker, start_date, end_date):
    df = yf.download(ticker, start=start_date, end=end_date)
    df.reset_index(inplace=True)
    return df

if __name__ == "__main__":
    df = fetch_stock_data('AAPL', '2022-01-01', '2023-01-01')
    print(df.head())
