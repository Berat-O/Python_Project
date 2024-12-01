import sys
import os
from multiprocessing import Pool
import logging
from load_stocks import StockLoader
from fetch_stocks import StockFetcher
from data_processor import DataProcessor
from plot_stocks import StockPlotter

class Main:

    def __init__(self):
        # Assign Log message
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(logging.INFO)  # Set the logger level to INFO

        # Create handler
        stream_handler = logging.StreamHandler(sys.stderr)  # Output logs to stderr
        stream_handler.setLevel(logging.INFO)    # Set the log level to INFO

        stream_format = logging.Formatter('%(name)s - %(levelname)s - %(message)s')  # Define the format for log messages
        stream_handler.setFormatter(stream_format)  # Assign the format to the stream handler

        self.logger.addHandler(stream_handler)  # Add the stream handler to the logger

        self.stock_loader = StockLoader()
        self.stock_fetcher = StockFetcher()
        self.data_processor = DataProcessor()
        self.stock_plotter = StockPlotter()

    def main(self):
        """Main function to orchestrate the execution flow."""
        self.logger.info('Session started')
        sys.stderr.flush()  # Force output of stderr buffer

        filename = input("Enter the filename containing the list of stocks: ")
        if not filename.endswith('.csv'):
            filename += '.csv'
        path = os.path.join("data", filename)

        sort_data = input("Sort data? (yes/no): ").lower() == 'yes'
        successful_symbols = []

        try:
            stocks = self.stock_loader.load_stocks(path)
            if not stocks:
                self.logger.info('No stocks loaded')
                return
            # Use multiprocessing to fetch data for multiple stocks concurrently
            with Pool() as pool:
                data = pool.map(self.stock_fetcher.fetch_stock_data, stocks)
            # Filter None values from data
            data = [stock_info for stock_info in data if stock_info is not None]
            if not data:
                self.logger.warning("No valid stock data was fetched.")
                return
            # Fill in the list of successful symbols
            successful_symbols = [stock_info[1] for stock_info in data]

            df = self.data_processor.display_data(data, sort=sort_data)
            self.stock_plotter.plot_data(df, save_figure=True, figure_filename="stock_ratings.png")
        except FileNotFoundError:
            # Handle missing file error
            self.logger.error(f"File {filename} not found. Please check the filename and try again.")
        except ValueError as e:
            # Handle invalid data format errors
            self.logger.error(f"Invalid data format encountered: {e}")
        except Exception as e:
            # Handle unexpected errors
            self.logger.error(f"An error occurred: {e}", exc_info=True)
        finally:
            save_successful = input("Do you want to save successful symbols? (yes/no): ").lower() == 'yes'
            if successful_symbols and save_successful:
                output_filename = input("Enter the filename to save successful symbols: ")
                if not output_filename.endswith('.csv'):
                    output_filename += '.csv'
                self.data_processor.save_successful_symbols(output_filename, successful_symbols)

        self.logger.info('Session stopped')  # Log that the session has stopped

if __name__ == '__main__':
    app = Main()
    app.main()