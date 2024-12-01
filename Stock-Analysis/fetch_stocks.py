import yfinance as yf
import logging
from urllib.error import URLError

class StockFetcher:

    @staticmethod
    def fetch_stock_data(stock):
        """Fetch stock data from Yahoo Finance."""
        try:
            ticker = yf.Ticker(stock)
            info = ticker.info
            if not info or 'recommendationMean' not in info:
                raise ValueError("Recommendation data is missing")
            rate = info["recommendationMean"]
            return (rate, stock)
        except ValueError as e:
            logging.getLogger(__name__).error(f"Value error for stock {stock}: {e}")
        except KeyError as e:
            logging.getLogger(__name__).error(f"Key error for stock {stock}: {e}", exc_info=True)
        except URLError as e:
            logging.getLogger(__name__).error(f"Network error while fetching data for {stock}: {e}")
        except Exception as e:
            logging.getLogger(__name__).error(f"Unexpected error while fetching data for {stock}: {e}", exc_info=True)
        return None