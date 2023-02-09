import yfinance as yf
import streamlit as st
import pandas as pd

st.write("""
# Stock Price App

Shows the Closing and Volume Stock price 
""")

#define the ticker symbol
ticker_symbol = 'GOOGL'

#Get data on this ticker
ticker_data = yf.Ticker(ticker_symbol)

#Get the historical prices for this ticker
ticker_df = ticker_data.history(period='1d', start='2023-01-01', end='2023-01-31')
st.write("""
## Closing Price

""")
st.line_chart(ticker_df.Close)

st.write("""
## Volume Price

""")
st.line_chart(ticker_df.Volume)