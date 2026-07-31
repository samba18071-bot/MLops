import pandas as pd
import streamlit as st
import yfinance as yf
import datetime

st.write(
    """
    # Stock Price Analyser
 
    Shown are the stock price data for the apple company.
    """
) 
tickerSymbol = st.text_input("Enter the stock ticker symbol", value="AAPL", key="placeholder")    

#tickerSymbol = 'AAPL'
#to divide into two columns
col1, col2 = st.columns(2)
with col1:
    start_date = st.date_input("Start date", value=datetime.date(2022, 1, 1))
with col2:  
    end_date = st.date_input("End date", value=datetime.date(2022, 12, 31))

tickerData = yf.Ticker(tickerSymbol)
tickerDf = tickerData.history(
                              start=start_date,
                              end=end_date)

st.write(
    f"""
    ## {tickerSymbol}'s EOD price data
    """
)
st.dataframe(tickerDf)

st.write(
    """
    ## Daily Closing Price
    """
)

st.line_chart(tickerDf.Close)


st.write(
    """
    ## Daily Volume
    """
)
st.line_chart(tickerDf.Volume)