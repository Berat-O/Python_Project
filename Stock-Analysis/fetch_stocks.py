import requests
import yfinance as yf
import logging

# Configure logging at the module level
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s')

class StockFetcher:

    @staticmethod
    def fetch_stock_data(stock):
        """Fetch stock data from Yahoo Finance.
        
        Args:
            stock (str): Stock symbol.
            
        Returns:
            list or None: A list containing stock rating and symbol, or None if data couldn't be fetched.
        """
        try:
            ticker = yf.Ticker(stock)
            info = ticker.info
            
            # Extract necessary data, ensuring they exist
            recommendation_mean = info.get("recommendationMean")
            symbol = info.get("symbol")
            
            # Check if the expected data is available
            if recommendation_mean is None or symbol is None:
                logging.error(f"Missing data for stock {stock}. Recommendation or symbol is None.")
                return None

            return [recommendation_mean, symbol]
        
        except (requests.exceptions.RequestException, yfinance.YahooFinanceError) as e:
            logging.error(f"Error fetching data for {stock}: {e}", exc_info=True)  # Log specific error
            return None
        except Exception as e:
            logging.error(f"Unexpected error fetching data for {stock}: {e}", exc_info=True)
            return None
