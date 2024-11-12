import os
import logging
from multiprocessing import Pool
from load_stocks import StockLoader
from fetch_stocks import StockFetcher
from data_processor import DataProcessor
from plot_stocks import StockPlotter


class Main:
    def __init__(self):
        """Initialize the Main class with the necessary components and configure logging."""
        # Create a logger instance
        self.logger = logging.getLogger(__name__)

        # Set up logging configuration
        logging.basicConfig(
            level=logging.INFO,  # Set the logging level to INFO
            format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',  # Define the log format
            handlers=[logging.StreamHandler()]  # Log to console
        )

        # Initialize instances of other classes
        self.stock_loader = StockLoader()
        self.stock_fetcher = StockFetcher()
        self.data_processor = DataProcessor()
        self.stock_plotter = StockPlotter()

    def main(self):
        """Main function to orchestrate the execution flow."""
        self.logger.info('Session started')  # Log the start of the session
        
        # Get the input filename and handle paths
        filename = input("Enter the filename containing the list of stocks: ")
        path = "/workspaces/Python_Project/Stock-Analysis/data/"
        filename = os.path.join(path, filename)

        # Ensure the file has a '.csv' extension
        if not filename.endswith('.csv'):
            filename += '.csv'

        # Ask the user if they want to sort the data
        sort_data = input("Sort data? (yes/no): ").lower() == 'yes'

        # Initialize a list to store successful stock symbols
        successful_symbols = []

        # Load and process stock data
        try:
            if not os.path.exists(filename):
                raise FileNotFoundError(f"The file {filename} does not exist.")
            
            # Load stock symbols from the file
            stocks = self.stock_loader.load_stocks(filename)

            # Use multiprocessing to fetch stock data concurrently
            with Pool() as pool:
                data = pool.map(self.stock_fetcher.fetch_stock_data, stocks)

            # Process the fetched data and filter out unsuccessful fetches
            for stock_info in data:
                if stock_info is not None and stock_info[0] is not None:
                    successful_symbols.append(stock_info[1])

            # Display the data and plot
            df = self.data_processor.display_data(data, sort=sort_data)
            self.stock_plotter.plot_data(df, save_figure=True, figure_filename="stock_ratings.png")

        except Exception as e:
            self.logger.error(f"An error occurred: {e}", exc_info=True)
        finally:
            # Optionally save successful symbols
            save_successful = input("Do you want to save successful symbols? (yes/no): ").lower() == 'yes'
            if successful_symbols and save_successful:
                output_filename = input("Enter the filename to save successful symbols: ")
                if not output_filename.endswith('.csv'):
                    output_filename += '.csv'
                self.data_processor.save_successful_symbols(output_filename, successful_symbols)

        # Log the end of the session
        self.logger.info('Session stopped')  # Log the stop of the session


# If the script is being run directly, instantiate and call the main function
if __name__ == '__main__':
    app = Main()  # Create an instance of the Main class
    app.main()  # Start the execution
