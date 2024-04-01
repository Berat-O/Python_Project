import requests
import csv
import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
import sys
from multiprocessing import Pool

def load_stocks(filename):
    with open(filename) as file:
        return [line[0] for line in csv.reader(file)]

def fetch_stock_data(stock):
    try:
        ticker = yf.Ticker(stock)
        return [ticker.info["recommendationMean"], ticker.info["symbol"]]
    except (KeyError, requests.exceptions.HTTPError):
        print(f"Failed to load data for {stock}")
        return None

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
    filename = input("Enter the filename containing the list of stocks: ")
    if not filename.endswith('.csv'):
        filename += '.csv'

    sort_data = input("Sort data? (yes/no): ").lower() == 'yes'

    try:
        stocks = load_stocks(filename)
        # Use multiprocessing to fetch data for multiple stocks concurrently
        with Pool() as pool:
            data = pool.map(fetch_stock_data, stocks)
        data = [d for d in data if d is not None]  # Remove None values (failed fetches)
        df = display_data(data, sort=sort_data)
        plot_data(df)
    except Exception as e:
        print(f"An error occurred: {e}")



if __name__ == "__main__":
    main()
