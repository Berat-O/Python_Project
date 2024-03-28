import requests
import csv
import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
import sys

def load_stocks(filename):
    with open(filename) as file:
        return [line[0] for line in csv.reader(file)]

def fetch_stock_data(stocks):
    data = []
    for stock in stocks:
        try:
            ticker = yf.Ticker(stock)
            data.append([ticker.info["recommendationMean"], ticker.info["symbol"]])
        except (KeyError, requests.exceptions.HTTPError):
            print(f"Failed to load data for {stock}")
    return data

def display_data(data, sort=False):
    df = pd.DataFrame(data, columns=['Rate', 'Symbol'])
    if sort:
        df = df.sort_values(by=['Rate'])
    print(df)
    return df

def plot_data(df):
    plt.bar(df['Symbol'], df['Rate'], color='skyblue')
    plt.xlabel('Symbol')
    plt.ylabel('Rate')
    plt.title('Stock Ratings')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.show()

def main():
    args = sys.argv
    stocks = load_stocks("stocks1.csv")
    data = fetch_stock_data(stocks)
    sorted_data = 'sort' in args
    df = display_data(data, sort=sorted_data)
    plot_data(df)

if __name__ == "__main__":
    main()
