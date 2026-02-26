import csv
import logging

class StockLoader:

    @staticmethod
    def load_stocks(filename):
        """Load stock symbols from CSV, trying multiple character codes."""
        stocks = []
        try:
            #List of encodings to try. 
            #utf-8-sig can preferentially process UTF-8 with BOM (for Excel)
            encodings = ['utf-8-sig', 'utf-8', 'cp932', 'shift_jis', 'euc-jp']
            
            selected_enc = None
            
            for enc in encodings:
                try:
                    with open(filename, 'r', encoding=enc) as file:
                        # Try loading it once and check if there are any errors
                        reader = csv.reader(file)
                        # Keep data temporarily
                        temp_stocks = []
                        for line in reader:
                            if line and len(line) >= 1:
                                symbol = line[0].strip()
                                if symbol:
                                    temp_stocks.append(symbol)
                        
                        # If you get to this point, loading is successful
                        stocks = temp_stocks
                        selected_enc = enc
                        break 
                except (UnicodeDecodeError, csv.Error):
                    # If decoding fails, try the next character code
                    continue
                except FileNotFoundError:
                    logging.getLogger(__name__).error(f"File {filename} not found.")
                    return []

            if selected_enc:
                logging.getLogger(__name__).info(f"Successfully loaded {filename} using {selected_enc}.")
            else:
                logging.getLogger(__name__).error(f"Failed to decode {filename} with available encodings.")
                return []

            if not stocks:
                logging.getLogger(__name__).warning(f"No valid stock symbols found in file {filename}.")
                
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