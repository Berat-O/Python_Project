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
                raise KeyError("recommendationMean field missing in API response")

            rate = info["recommendationMean"]
            return (rate, stock)

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

