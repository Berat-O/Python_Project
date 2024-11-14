import requests
import yfinance as yf
import logging


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
            return [ticker.info.get("recommendationMean"), ticker.info.get("symbol")]
        except (KeyError, requests.exceptions.HTTPError):
            logging.getLogger(__name__).error(f"Failed to load data for {stock}", exc_info=True)  # Log error if data couldn't be fetched
            return None