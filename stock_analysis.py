# Stock Analysis Script

import yfinance as yf

ticker = input("Enter stock symbol (e.g., AAPL): ")

stock = yf.Ticker(ticker)
data = stock.history(period="5d")

print("\nStock Data:\n")
print(data)