import yfinance as yf
import logging
from urllib.error import URLError


class StockFetcher:

    @staticmethod
    def fetch_stock_data(stock):
        """
        Fetch stock data safely with proper validation
        and improved error handling.

        Returns:
            tuple: (recommendationMean, stock symbol)
            None: if any error occurs
        """

        try:
            # Validate stock symbol input
            if not stock or not isinstance(stock, str):
                raise ValueError("Stock symbol must be a non-empty string.")

            # Remove extra spaces and convert to uppercase
            stock = stock.strip().upper()

            # Fetch stock information from Yahoo Finance
            ticker = yf.Ticker(stock)
            info = ticker.info

            # Check if API returned data
            if not info:
                raise ValueError(
                    "No data received. Please check the stock symbol."
                )

            # Check if recommendation data exists
            if "recommendationMean" not in info:
                raise KeyError(
                    "Recommendation data not available for this stock."
                )

            # Extract recommendation value
            recommendation_rate = info["recommendationMean"]

            return (recommendation_rate, stock)

        except ValueError as error:
            print(f"❌ Input Error: {error}")
            logging.error(f"[ValueError] {error}")

        except KeyError as error:
            print(f"❌ Data Error: {error}")
            logging.error(f"[KeyError] {error}", exc_info=True)

        except URLError:
            print("❌ Network Error: Please check your internet connection.")
            logging.error(
                "[URLError] Network issue occurred.",
                exc_info=True
            )

        except Exception as error:
            print(
                f"❌ Unexpected Error: "
                f"{type(error).__name__} - {error}"
            )
            logging.error(
                f"[Unexpected Error] {error}",
                exc_info=True
            )

        # Return None if any error occurs
        return None
