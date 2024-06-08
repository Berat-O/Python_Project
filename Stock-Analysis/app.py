import requests
import csv
import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
import os
from multiprocessing import Pool
import logging
import datetime


# Assign Log message
logger = logging.getLogger(__name__)

# Create handler
stream_handler = logging.StreamHandler()  # Create a stream handler to output logs to console
stream_handler.setLevel(logging.INFO)    # Set the log level to INFO

# Assign handler
stream_format = logging.Formatter('%(name)s - %(levelname)s - %(message)s')  # Define the format for log messages
stream_handler.setFormatter(stream_format)  # Assign the format to the stream handler

# Add handler
logger.addHandler(stream_handler)  # Add the stream handler to the logger

def load_stocks(filename):
    """Load stock symbols from a CSV file.
    
    Args:
        filename (str): The name of the CSV file containing stock symbols.
        
    Returns:
        list: A list of stock symbols.
    """
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        logger.info('Files loaded')  # Log that the file has been loaded
        return [line[0] for line in reader]
    
# updated the exception handling
def fetch_stock_data(stock):
    """Fetch stock data from Yahoo Finance.
    
    Args:
        stock (str): Stock symbol.
        
    Returns:
        list or None: A list containing stock rating and symbol, or None if data couldn't be fetched.
    """
    try:
        ticker = yf.Ticker(stock)
        return [ticker.info.get("recommendationMean"), ticker.info.get("symbol")]
    except KeyError as e:
        logger.error(f"Failed to load data for {stock}. Missing key: {e}") # Improved the error exception added the data catch and also catch the key error

def display_data(data, sort=False):
    """Display stock data in tabular format.
    
    Args:
        data (list): List of stock data.
        sort (bool): Whether to sort the data by rating.
        
    Returns:
        DataFrame: Pandas DataFrame containing stock data.
    """
    df = pd.DataFrame(data, columns=['Rate', 'Symbol'])
    if sort:
        df = df.dropna().sort_values(by=['Rate'])
    print(df.head())
    return df

def plot_data(df, save_figure=False, figure_filename="plot.png", bar_width=0.6, font_size=3, dpi=700):
    """Plot stock ratings.
    
    Args:
        df (DataFrame): Pandas DataFrame containing stock data.
        save_figure (bool): Whether to save the plot as an image file.
        figure_filename (str): Filename to save the plot.
        bar_width (float): Width of the bars in the bar plot.
        font_size (int): Font size for plot labels.
        dpi (int): Dots per inch for the saved image.
    """
    plt.bar(df['Symbol'], df['Rate'], color='skyblue', width=bar_width)
    plt.xlabel('Symbol', fontsize=font_size)
    plt.ylabel('Rate', fontsize=font_size)
    plt.title('Stock Ratings', fontsize=font_size)
    plt.xticks(rotation=45, ha='right', fontsize=font_size)
    plt.tight_layout()
    if save_figure:
        current_time = datetime.datetime.now().strftime("%d-%m-%Y")
        figure_filename = f"/workspaces/Python_Project/Stock-Analysis/results/plot_{current_time}.png"
        plt.savefig(figure_filename, dpi=dpi)  # Save the figure to a file with higher resolution
        logger.info(f"Figure saved as {figure_filename}.")  # Log that the figure has been saved
    else:
        plt.show()

# updated the error handling mechanism in the code
def save_successful_symbols(filename, successful_symbols):
  """Save successfully fetched stock symbols to a CSV file.

  Args:
      filename (str): Filename to save the symbols.
      successful_symbols (list): List of successfully fetched stock symbols.
  """
  try:
      path = "/workspaces/Python_Project/Stock-Analysis/data/"
      new_filename = os.path.splitext(filename)[0] + ".csv"
      new_filename = path + new_filename
      with open(new_filename, 'w') as file:
          writer = csv.writer(file)
          for symbol in successful_symbols:
              writer.writerow([symbol])
      logger.info(f"Successful symbols saved to {new_filename}.")  # Log that symbols have been saved for further coders to work on
  except OSError as e:
      logger.error(f"An error occurred while saving successful symbols to {new_filename}: {e}")  # Log specific OSError details
  except Exception as e:  # Fallback for other exceptions
      logger.error(f"An unexpected error occurred: {e}")  # Log a generic message for other exceptions .

def main():
    """Main function to orchestrate the execution flow."""
    logging.basicConfig(
        filename='myapp.log',
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        level=logging.INFO
    )
    logger.info('Session started')  # Log that the session has started
    filename = input("Enter the filename containing the list of stocks: ")
    path = "/workspaces/Python_Project/Stock-Analysis/data/"
    filename = path + filename
    
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
        plot_data(df, save_figure=True, figure_filename="stock_ratings.png")

    except Exception as e:
        logger.error(f"An error occurred: {e}", exc_info=True)  # Log error if an exception occurs
    finally:
        save_successful = input("Do you want to save successful symbols? (yes/no): ").lower() == 'yes'
        if successful_symbols and save_successful:
            output_filename = input("Enter the filename to save successful symbols: ")
            if not output_filename.endswith('.csv'):
                output_filename += '.csv'
            save_successful_symbols(output_filename, successful_symbols)

    logger.info('Session stopped')  # Log that the session has stopped

main()  # Call the main function to start the script
