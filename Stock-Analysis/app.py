import requests
import csv
import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
import os
from multiprocessing import Pool

def load_stocks(filename):
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        return [line[0] for line in reader]

def fetch_stock_data(stock):
    try:
        ticker = yf.Ticker(stock)
        return [ticker.info.get("recommendationMean"), ticker.info.get("symbol")]
    except (KeyError, requests.exceptions.HTTPError):
        print(f"Failed to load data for {stock}")
        return None

def display_data(data, sort=False):
    df = pd.DataFrame(data, columns=['Rate', 'Symbol'])
    if sort:
        df = df.dropna().sort_values(by=['Rate'])
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

def save_successful_symbols(filename, successful_symbols):
    try:
        new_filename = os.path.splitext(filename)[0] + "_successful.csv"
        with open(new_filename, 'w') as file:
            writer = csv.writer(file)
            for symbol in successful_symbols:
                writer.writerow([symbol])
        print(f"Successful symbols saved to {new_filename}.")
    except Exception as e:
        print(f"An error occurred while saving successful symbols to {new_filename}: {e}")

def main():
    filename = input("Enter the filename containing the list of stocks: ")
    if not filename.endswith('.csv'):
        filename += '.csv'

    sort_data = input("Sort data? (yes/no): ").lower() == 'yes'
    successful_symbols = []

    try:
        stocks = load_stocks(filename)
        # Use multiprocessing to fetch data for multiple stocks concurrently
        with Pool() as pool:
            data = pool.map(fetch_stock_data, stocks)
        for stock_info in data:
            if stock_info is not None and stock_info[0] is not None:
                successful_symbols.append(stock_info[1])
        df = display_data(data, sort=sort_data)
        plot_data(df)
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        if successful_symbols:
            save_successful_symbols(filename, successful_symbols)

if __name__ == "__main__":
    main()
