# Extracting Stock Data Using a Python Library

import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

nvidia = yf.Ticker("NVDA")
#nvidia historical stock prices
print(nvidia.history(period= "1mo"))
#information about data types of nvidia
print(nvidia.info)
#about income statement
print(nvidia.financials.T)
print(nvidia.dividends)
print(nvidia.info['sector'])
print(nvidia.info['industry'])

nvidia_share_price_data = nvidia.history(period="max")
print(nvidia_share_price_data)
print(nvidia_share_price_data.head())
print(nvidia_share_price_data.reset_index(inplace=True))
print(nvidia_share_price_data.plot(x="Date", y="Open"))