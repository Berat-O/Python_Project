import csv
import logging
import os

# Set up logging for the module
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s')

class StockLoader:

    @staticmethod
    def load_stocks(filename):
        """Load stock symbols from a CSV file.
        
        Args:
            filename (str): The name of the CSV file containing stock symbols.
            
        Returns:
            list: A list of stock symbols.
        """
        if not os.path.isfile(filename):  # Check if the file exists
            logging.error(f"File {filename} does not exist.")
            return []  # Return an empty list if the file does not exist

        try:
            with open(filename, 'r') as file:
                reader = csv.reader(file)
                stock_symbols = [line[0] for line in reader if line]  # Ensures non-empty lines are read
                logging.info(f"Successfully loaded {len(stock_symbols)} stock symbols from {filename}.")
                return stock_symbols
        except Exception as e:
            logging.error(f"Error reading the file {filename}: {e}")
            return []

