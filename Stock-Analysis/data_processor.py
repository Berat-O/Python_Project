import os
import csv
import pandas as pd
import logging

class DataProcessor:

    @staticmethod
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
    
    @staticmethod
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
            logging.getLogger(__name__).info(f"Successful symbols saved to {new_filename}.")  # Log that symbols have been saved
        except Exception as e:
            logging.getLogger(__name__).error(f"An error occurred while saving successful symbols to {new_filename}: {e}")  # Log error if saving fails
