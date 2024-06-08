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

        # Create handler
        stream_handler = logging.StreamHandler()  # Create a stream handler to output logs to console
        stream_handler.setLevel(logging.INFO)    # Set the log level to INFO

        # Assign handler
        stream_format = logging.Formatter('%(name)s - %(levelname)s - %(message)s')  # Define the format for log messages
        stream_handler.setFormatter(stream_format)  # Assign the format to the stream handler

        # Add handler
        self.logger.addHandler(stream_handler)  # Add the stream handler to the logger
        
        # Initialize instances of other classes
        self.stock_loader = StockLoader()
        self.stock_fetcher = StockFetcher()
        self.data_processor = DataProcessor()
        self.stock_plotter = StockPlotter()

    def main(self):
        """Main function to orchestrate the execution flow."""
        logging.basicConfig(
            filename='myapp.log',
            format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
            level=logging.INFO
        )
        self.logger.info('Session started')  # Log that the session has started
        filename = input("Enter the filename containing the list of stocks: ")
        path = "/workspaces/Python_Project/Stock-Analysis/data/"
        filename = path + filename
        
        if not filename.endswith('.csv'):
            filename += '.csv'
            
        sort_data = input("Sort data? (yes/no): ").lower() == 'yes'
        successful_symbols = []

        try:
            stocks = self.stock_loader.load_stocks(filename)
            # Use multiprocessing to fetch data for multiple stocks concurrently
            with Pool() as pool:
                data = pool.map(self.stock_fetcher.fetch_stock_data, stocks)
            for stock_info in data:
                if stock_info is not None and stock_info[0] is not None:
                    successful_symbols.append(stock_info[1])
            df = self.data_processor.display_data(data, sort=sort_data)
            self.stock_plotter.plot_data(df, save_figure=True, figure_filename="stock_ratings.png")

        except Exception as e:
            self.logger.error(f"An error occurred: {e}", exc_info=True)  # Log error if an exception occurs
        finally:
            save_successful = input("Do you want to save successful symbols? (yes/no): ").lower() == 'yes'
            if successful_symbols and save_successful:
                output_filename = input("Enter the filename to save successful symbols: ")
                if not output_filename.endswith('.csv'):
                    output_filename += '.csv'
                self.data_processor.save_successful_symbols(output_filename, successful_symbols)

        self.logger.info('Session stopped')  # Log that the session has stopped

if __name__ == '__main__':  # If the script is being run directly, call the main function
    app = Main()  # Create an instance of the class
    app.main()  # Call the main function to start the script

