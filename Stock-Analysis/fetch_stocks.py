import yfinance as yf
import logging
from urllib.error import URLError

class StockFetcher:

    @staticmethod
    def fetch_stock_data(stock):
        """Fetch stock data from Yahoo Finance with improved error handling."""
        try:
            ticker = yf.Ticker(stock)
            info = ticker.info

            # Check if info returned anything
            if not info:
                raise ValueError("Empty response received from Yahoo Finance API")

            # Check if recommendation data exists
            if 'recommendationMean' not in info:
                # log and return None instead of throwing an error
                logging.getLogger(__name__).warning(f"No recommendation data for {stock}. Skipping.")
                return None 

            # First find the analyst recommendation value (recommendationMean) 
            # If not available, substitute current stock price (currentPrice)
            rate = info.get("recommendationMean")
            if rate is None:
                # Obtain prices for Japanese stocks etc.
                rate = info.get("currentPrice") or info.get("regularMarketPrice") or 0
                logging.getLogger(__name__).debug(f"{stock}: Using price as fallback.")

            # Unify the return value into a dictionary (for consistency with app.py)
            return {"Rate": rate, "Symbol": stock}

        except ValueError as e:
            logging.getLogger(__name__).error(
                f"[ValueError] Unable to fetch data for '{stock}': {e}. "
                f"Possible causes: Invalid stock symbol or empty API response."
            )

        except KeyError as e:
            logging.getLogger(__name__).error(
                f"[KeyError] Missing expected data for '{stock}': {e}. "
                f"The API might have changed or the stock does not provide recommendation data.",
                exc_info=True
            )

        except URLError as e:
            logging.getLogger(__name__).error(
                f"[URLError] Network issue while fetching '{stock}': {e}. "
                f"Please check your internet connection or try again later."
            )

        except Exception as e:
            logging.getLogger(__name__).error(
                f"[Unexpected Error] Failed to fetch '{stock}': ({type(e).__name__}) {e}",
                exc_info=True
            )

        return None

