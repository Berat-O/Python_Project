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
    def save_successful_symbols(filename, results):
        """Save successfully fetched stock symbols to a CSV file."""
        if not results:
            logging.getLogger(__name__).info("No successful symbols to save.")
            return
        
        directory = "data"
        #Constructing the file path
        # Eliminate the possibility of unbound in exception handling
        path = os.path.join(directory, filename)
        
        try:
            if not os.path.exists(directory):
                os.makedirs(directory)
            with open(path, 'w', newline='', encoding='utf-8') as file:
                # DictWriter allows you to neatly divide dictionary data into columns
                fieldnames = ['Rate', 'Symbol']
                writer = csv.DictWriter(file, fieldnames=fieldnames)
                
                # Write header (column name)
                writer.writeheader()
                # write all lines of data
                for row in results:
                    writer.writerow(row)
            logging.getLogger(__name__).info(f"Successful symbols saved to {path}.")
        except PermissionError:
            logging.getLogger(__name__).error(f"Permission denied: Unable to save symbols to {path}. Please check file permissions")
        except IOError as e:
            logging.getLogger(__name__).error(f"IO error occurred while saving symbols: {e}")
        except Exception as e:
            logging.getLogger(__name__).error(f"An error occurred while saving successful symbols to {path}: {e}")
