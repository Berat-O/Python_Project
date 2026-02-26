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
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(logging.INFO)

        stream_handler = logging.StreamHandler(sys.stderr)
        stream_handler.setLevel(logging.INFO)

        stream_format = logging.Formatter('%(name)s - %(levelname)s - %(message)s')
        stream_handler.setFormatter(stream_format)

        if not self.logger.handlers:
            self.logger.addHandler(stream_handler)

        self.stock_loader = StockLoader()
        self.stock_fetcher = StockFetcher()
        self.data_processor = DataProcessor()
        self.stock_plotter = StockPlotter()

    def main(self):
        """Main function to orchestrate the execution flow."""
        self.logger.info("Session started")
        sys.stderr.flush()

        # ---- Filename input ----
        filename = input("Enter the filename containing the list of stocks: ").strip()

        if not filename:
            print("Error: Filename cannot be empty.")
            self.logger.error("Empty filename provided.")
            return

        if "." in filename and not filename.endswith(".csv"):
            print("Error: Please provide a .csv file.")
            self.logger.error(f"Invalid file extension: {filename}")
            return

        if not filename.endswith(".csv"):
            filename += ".csv"

        path = os.path.join("data", filename)

        # ---- Sorting preference ----
        sort_data = input("Sort data? (yes/no): ").strip().lower() == "yes"
        successful_symbols = []

        try:
            stocks = self.stock_loader.load_stocks(path)

            if not stocks:
                print("No stocks found in the provided file.")
                self.logger.info("No stocks loaded.")
                return

            # Limit the number of Pool() to reduce memory consumption.
            # This is to avoid running out of PC memory (or virtual memory) when executing parallel processing.
            with Pool(processes=2) as pool:
                data = pool.map(self.stock_fetcher.fetch_stock_data, stocks)

            data = [stock_info for stock_info in data if stock_info is not None]

            if not data:
                print("No valid stock data was fetched.")
                self.logger.warning("No valid stock data was fetched.")
                return

            successful_symbols = data  # Keep all data
            
            df = self.data_processor.display_data(data, sort=sort_data)
            
            self.stock_plotter.plot_data(
                df,
                save_figure=True,
                figure_filename="stock_ratings.png"
            )

        except FileNotFoundError:
            print(f"Error: File '{filename}' not found.")
            self.logger.error(f"File not found: {filename}")

        except ValueError as e:
            print(f"Error: Invalid data format - {e}")
            self.logger.error(f"Invalid data format: {e}")

        except Exception as e:
            print(f"Unexpected error occurred: {e}")
            self.logger.error("Unexpected error", exc_info=True)

        finally:
            save_successful = input("Do you want to save successful symbols? (yes/no): ").strip().lower() == "yes"

            if successful_symbols and save_successful:
                output_filename = input("Enter the filename to save successful symbols: ").strip()

                if not output_filename.endswith(".csv"):
                    output_filename += ".csv"

                self.data_processor.save_successful_symbols(
                    output_filename,
                    successful_symbols
                )

        self.logger.info("Session stopped")


if __name__ == "__main__":
    app = Main()
    app.main()
