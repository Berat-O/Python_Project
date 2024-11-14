import csv
import logging

class StockLoader:

    @staticmethod
    def load_stocks(filename):
        """Load stock symbols from a CSV file.
        
        Args:
            filename (str): The name of the CSV file containing stock symbols.
            
        Returns:
            list: A list of stock symbols.
        """
        with open(filename, 'r') as file:
            reader = csv.reader(file)
            logging.getLogger(__name__).info('Files loaded')  # Log that the file has been loaded
            return [line[0] for line in reader]