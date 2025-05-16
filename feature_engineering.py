def add_features(df):
    df['MA7'] = df['Close'].rolling(window=7).mean()
    df['MA14'] = df['Close'].rolling(window=14).mean()
    df['Price_Change'] = df['Close'].pct_change()
    df['Volatility'] = df['Close'].rolling(window=7).std()
    df['Close_lag_1'] = df['Close'].shift(1)
    df['Close_lag_2'] = df['Close'].shift(2)
    df.dropna(inplace=True)
    return df

if __name__ == "__main__":
    import yfinance as yf
    df = yf.download('AAPL', start='2022-01-01', end='2023-01-01')
    df.reset_index(inplace=True)
    df = add_features(df)
    print(df.head())
