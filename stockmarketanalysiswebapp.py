import streamlit as st
import yfinance as yf
import datetime
import pandas as pd 
import numpy as np
import pandas_datareader as pdr
import datetime
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import base64 as base64

start_date = datetime.datetime(2010, 1, 1)
end_date = datetime.datetime(2019, 12, 31)


def image_local(image_file):
    with open(image_file, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())
    st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: url(data:image/{"jpg"};base64,{encoded_string.decode()});
        background-size: cover
    }}
    </style>
    """,
    unsafe_allow_html=True
    )
image_local('D:/code/Jupyter/stock-exchange-background-vector-27122797.jpg')


st.title("Stock Market Analysis")

selected_stock = st.sidebar.selectbox("Select dataset for analysis", ["INFY.NS", "TATASTEEL.NS","TATAMOTORS.NS", "TCS.NS", "MARUTI.NS", "HDFCBANK.NS", 
                                                              "BHARTIARTL.NS", "HINDALCO.NS", "WIPRO.NS","RELIANCE.NS", "ONGC.NS", "ADANIPORTS.NS",
                                                              "AXISBANK.NS", "NESTLEIND.NS", "HCLTECH.NS","SBIN.NS", "ICICIBANK.NS", "BRITANNIA.NS", 
                                                              "HINDUNILVR.NS","SUNPHARMA.NS"]) 

def get_dataset(selected_stock):
    if selected_stock == "INFY.NS":
        data = yf.download("INFY.NS", start=start_date, end=end_date)
    elif selected_stock == "TATASTEEL.NS":
        data = yf.download("TATASTEEL.NS", start=start_date, end=end_date)
    elif selected_stock == "TATAMOTORS.NS":
        data = yf.download("TATAMOTORS.NS", start=start_date, end=end_date)
    elif selected_stock == "TCS.NS":
        data = yf.download("TCS.NS", start=start_date, end=end_date)
    elif selected_stock == "MARUTI.NS":
        data = yf.download("MARUTI.NS", start=start_date, end=end_date)
    elif selected_stock == "HDFCBANK.NS":
        data = yf.download("HDFCBANK.NS", start=start_date, end=end_date)
    elif selected_stock == "BHARTIARTL.NS":
        data = yf.download("BHARTIARTL.NS", start=start_date, end=end_date)
    elif selected_stock == "HINDALCO.NS":
        data = yf.download("HINDALCO.NS", start=start_date, end=end_date)
    elif selected_stock == "WIPRO.NS":
        data = yf.download("WIPRO.NS", start=start_date, end=end_date)
    elif selected_stock == "RELIANCE.NS":
        data = yf.download("RELIANCE.NS", start=start_date, end=end_date)
    elif selected_stock == "ONGC.NS":
        data = yf.download("ONGC.NS", start=start_date, end=end_date)
    elif selected_stock == "ADANIPORTS.NS":
        data = yf.download("ADANIPORTS.NS", start=start_date, end=end_date)
    elif selected_stock == "AXISBANK.NS":
        data = yf.download("AXISBANK.NS", start=start_date, end=end_date)
    elif selected_stock == "NESTLEIND.NS":
        data = yf.download("NESTLEIND.NS", start=start_date, end=end_date)
    elif selected_stock == "HCLTECH.NS":
        data = yf.download("HCLTECH.NS", start=start_date, end=end_date)
    elif selected_stock == "SBIN.NS":
        data = yf.download("SBIN.NS", start=start_date, end=end_date)
    elif selected_stock == "ICICIBANK.NS":
        data = yf.download("ICICIBANK.NS", start=start_date, end=end_date)
    elif selected_stock == "BRITANNIA.NS":
        data = yf.download("BRITANNIA.NS", start=start_date, end=end_date)
    elif selected_stock == "HINDUNILVR.NS":
        data = yf.download("HINDUNILVR.NS", start=start_date, end=end_date)
    else:
        data = yf.download("SUNPHARMA.NS", start=start_date, end=end_date)
    return data

df = get_dataset(selected_stock)


if df is not None:
    col1, col2 = st.columns([0.3,0.7])
    
    with col1:
        st.markdown("Uploaded dataset")
        st.dataframe(df)
    
    with col2:
        st.markdown("Visualization")
        filter = st.sidebar.radio("Choose the plots:",["First Rows","Last Rows","Line Plot", "Histogram","Area"])
        if filter == "First Rows":
            st.dataframe(df.head())
        elif filter == "Last Rows":
            st.dataframe(df.tail())
        elif filter == "Line Plot":
            closing = st.sidebar.radio("Choose:",["Close","Adj Close"])
            if closing == "Close":
                stockdf = df['Close']
                st.line_chart(stockdf)
            else:
                stockdf = df['Adj Close']
                st.line_chart(stockdf)
        elif filter == "Histogram":
            closing = st.sidebar.radio("Choose:",["Close","Adj Close"])
            if closing == "Close":
                fig, ax = plt.subplots()
                stockdf = df['Close']
                ax.hist(stockdf, bins=20)
                st.pyplot(fig)
            else:
                fig, ax = plt.subplots()
                stockdf = df['Adj Close']
                ax.hist(stockdf, bins=20)
                st.pyplot(fig)
        else:
            st.area_chart(df)
            
            
            