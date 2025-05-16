import pandas as pd
from sklearn.preprocessing import MinMaxScaler

def preprocess_data(df):
    # Fill missing values
    df.fillna(method='ffill', inplace=True)
    
    # Remove duplicates
    df.drop_duplicates(inplace=True)
    
    # Scale features
    scaler = MinMaxScaler()
    scaled_features = scaler.fit_transform(df[['Open', 'High', 'Low', 'Close', 'Volume']])
    df_scaled = pd.DataFrame(scaled_features, columns=['Open', 'High', 'Low', 'Close', 'Volume'])
    
    return df_scaled, scaler

if __name__ == "__main__":
    import yfinance as yf
    df = yf.download('AAPL', start='2022-01-01', end='2023-01-01')
    df.reset_index(inplace=True)
    df_scaled, scaler = preprocess_data(df)
    print(df_scaled.head())
