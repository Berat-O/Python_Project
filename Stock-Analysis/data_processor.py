import os
import csv
import pandas as pd
import logging

# Configure logging at the module level
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s')

class DataProcessor:

    @staticmethod
    def display_data(data, sort=False, top_n=10):
        """Display stock data in tabular format.
        
        Args:
            data (list): List of stock data.
            sort (bool): Whether to sort the data by rating.
            top_n (int): Number of rows to display. Default is 10.
            
        Returns:
            DataFrame: Pandas DataFrame containing stock data.
        """
        df = pd.DataFrame(data, columns=['Rate', 'Symbol'])
        
        if sort:
            df = df.dropna().sort_values(by=['Rate'], ascending=False)
        
        # Display top_n rows, useful when data is large
        print(df.head(top_n))
        return df
    
    @staticmethod
    def save_successful_symbols(filename, successful_symbols):
        """Save successfully fetched stock symbols to a CSV file.
        
        Args:
            filename (str): Filename to save the symbols.
            successful_symbols (list): List of successfully fetched stock symbols.
        """
        try:
            # Construct the full path for saving the file
            path = os.path.join(os.getcwd(), "data")  # Use current working directory
            os.makedirs(path, exist_ok=True)  # Ensure directory exists
            
            # Construct the new filename with CSV extension
            new_filename = os.path.splitext(filename)[0] + ".csv"
            new_filename = os.path.join(path, new_filename)
            
            with open(new_filename, 'w', newline='', encoding='utf-8') as file:
                writer = csv.writer(file)
                writer.writerow(['Symbol'])  # Optional header for CSV file
                for symbol in successful_symbols:
                    writer.writerow([symbol])
            
            logging.getLogger(__name__).info(f"Successful symbols saved to {new_filename}.")
        except Exception as e:
            logging.getLogger(__name__).error(f"An error occurred while saving successful symbols to {new_filename}: {e}")
