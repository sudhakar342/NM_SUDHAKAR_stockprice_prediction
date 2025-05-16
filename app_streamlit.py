import streamlit as st
import yfinance as yf
import pandas as pd

st.title("Stock Price Prediction")

ticker = st.text_input("Enter Stock Ticker", "AAPL")
start_date = st.date_input("Start Date", pd.to_datetime('2022-01-01'))
end_date = st.date_input("End Date", pd.to_datetime('2023-01-01'))

if st.button("Predict"):
    df = yf.download(ticker, start=start_date, end=end_date)
    st.line_chart(df['Close'])
    st.write("Prediction feature coming soon!")
