import os
import csv
import pandas as pd
import logging

class DataProcessor:

    @staticmethod
    def display_data(data, sort=False):
        """Display stock data in tabular format."""
        if not data:
            logging.getLogger(__name__).warning("No data to display.")
            return pd.DataFrame()
        #Filtering None values inside data
        data = [item for item in data if item is not None]

        df = pd.DataFrame(data, columns=['Rate', 'Symbol'])
        if sort:
            df = df.dropna().sort_values(by=['Rate'])
        print(df.head())
        return df
    
    @staticmethod
    def save_successful_symbols(filename, successful_symbols):
        """Save successfully fetched stock symbols to a CSV file."""
        if not successful_symbols:
            logging.getLoger(__name__).info("No successful symbols to save.")
            return

        try:
            directory = "data"
            if not os.path.exists(directory):
                os.makedirs(directory)
            #Constructing the file path
            path = os.path.join(directory, filename)
            with open(path, 'w', newline='') as file:
                writer = csv.writer(file)
                for symbol in successful_symbols:
                    writer.writerow([symbol])
            logging.getLogger(__name__).info(f"Successful symbols saved to {path}.")
        except PermissionError:
            logging.getLogger(__name__).error(f"Permission denied: Unable to save symbols to {path}. Please check file permissions")
        except IOError as e:
            logging.getLogger(__name__).error(f"IO error occurred while saving symbols: {e}")
        except Exception as e:
            logging.getLogger(__name__).error(f"An error occurred while saving successful symbols to {path}: {e}")
