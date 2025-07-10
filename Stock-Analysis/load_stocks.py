import csv
import logging

class StockLoader:

    @staticmethod
    def load_stocks(filename):
        """Load stock symbols from a CSV file."""
        stocks = []
        try:
            with open(filename, 'r') as file:
                reader = csv.reader(file)
                for line in reader:
                    if line and len(line) >= 1:
                        symbol = line[0].strip()
                        if symbol:
                            stocks.append(symbol)
            if not stocks:
                logging.getLogger(__name__).warning(f"No valid stock symbols found in file {filename}.")
            else:
                logging.getLogger(__name__).info('File loaded successfully.')
            return stocks
        except FileNotFoundError:
            logging.getLogger(__name__).error(f"File {filename} not found. Please provide a valid file path.")
            return []
        except csv.Error as e:
            logging.getLogger(__name__).error(f"CSV format error in file {filename}: {e}")
            return []
        except Exception as e:
            logging.getLogger(__name__).error(f"An unexpected error occurred while loading stocks: {e}")
            return []