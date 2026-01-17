import streamlit as st
import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

# Page title
st.title("📊 NVIDIA Stock Dashboard")

# Load data
ticker = yf.Ticker("NVDA")
data = ticker.history(period="1y")

# Company Info
st.subheader("📌 Company Information")
st.write("**Company Name:** NVIDIA Corporation")
st.write("**Sector:**", ticker.info.get("sector"))
st.write("**Market Cap:**", ticker.info.get("marketCap"))

# Show raw data
st.subheader("📋 Stock Price Data")
st.dataframe(data.head())

# Plot stock price
st.subheader("📈 Closing Price Trend")

fig, ax = plt.subplots()
ax.plot(data.index, data["Close"])
ax.set_xlabel("Date")
ax.set_ylabel("Close Price")
st.pyplot(fig)

# Volume chart
st.subheader("📊 Trading Volume")
st.bar_chart(data["Volume"])
