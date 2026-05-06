import yfinance as yf
import logging
from urllib.error import URLError

class StockFetcher:

    @staticmethod
    def fetch_stock_data(stock):
        """Fetch stock data with improved validation and user-friendly error handling."""
        try:
            # ✅ Input validation
            if not stock or not isinstance(stock, str):
                raise ValueError("Stock symbol must be a non-empty string")

            stock = stock.strip().upper()

            ticker = yf.Ticker(stock)
            info = ticker.info

            # ✅ Check empty response
            if not info:
                raise ValueError("No data received. Please check the stock symbol.")

            # ✅ Check required field
            if 'recommendationMean' not in info:
                raise KeyError("Recommendation data not available for this stock.")

            rate = info["recommendationMean"]
            return (rate, stock)

        except ValueError as e:
            print(f"❌ Input Error: {e}")
            logging.error(f"[ValueError] {e}")

        except KeyError as e:
            print(f"❌ Data Error: {e}")
            logging.error(f"[KeyError] {e}", exc_info=True)

        except URLError:
            print("❌ Network Error: Please check your internet connection.")
            logging.error("[URLError] Network issue", exc_info=True)

        except Exception as e:
            print(f"❌ Unexpected Error: {type(e).__name__} - {e}")
            logging.error(f"[Unexpected Error] {e}", exc_info=True)

        # ✅ Always return None on failure
        return None
