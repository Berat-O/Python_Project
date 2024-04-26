import requests
import csv
import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
import os
from multiprocessing import Pool
import logging

# Assign Log message
logger = logging.getLogger(__name__)

# Create handler
stream_handler = logging.StreamHandler()                                                                # Stream handler
stream_handler.setLevel(logging.INFO)                                                                   # Set level

# Assign handler
stream_format = logging.Formatter('%(name)s - %(levelname)s - %(message)s')                             # Stream format
stream_handler.setFormatter(stream_format)                                                              # Assign format

# Add handler
logger.addHandler(stream_handler)

def load_stocks(filename):
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        logger.info('Files loaded')
        return [line[0] for line in reader]

def fetch_stock_data(stock):
    try:
        ticker = yf.Ticker(stock)
        return [ticker.info.get("recommendationMean"), ticker.info.get("symbol")]
    except (KeyError, requests.exceptions.HTTPError):
        logger.error(f"Failed to load data for {stock}", exc_info=True)
        return None

def display_data(data, sort=False):
    df = pd.DataFrame(data, columns=['Rate', 'Symbol'])
    if sort:
        df = df.dropna().sort_values(by=['Rate'])
    print(df.head())
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
        logger.info(f"Successful symbols saved to {new_filename}.")                                     # Info log for writing data
    except Exception as e:
        logger.error(f"An error occurred while saving successful symbols to {new_filename}: {e}")       # Error log for writing data

def main():
    logging.basicConfig(
        filename='myapp.log', 
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', 
        level=logging.INFO
        )
    logger.info('Session started')                                                                      # Session start info log
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
        logger.error(f"An error occurred: {e}", exc_info=True)                                          # Error log while running main
    finally:
        if successful_symbols:
            save_successful_symbols(filename, successful_symbols)

    logger.info('Session stopped')                                                                      # Session stop info log

if __name__ == "__main__":
    main()
