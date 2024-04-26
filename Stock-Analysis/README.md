# Stock Analysis Script

## Overview
This script is designed to analyze stock data fetched from Yahoo Finance using the `yfinance` library. It allows users to input a list of stock symbols via a CSV file, fetch relevant data such as stock ratings, and display the data in a tabular format. Additionally, it provides an option to sort the data based on stock ratings and generate a bar plot for visualization.

## Features
- **Fetching Stock Data**: The script utilizes Yahoo Finance API to fetch stock data including stock ratings.
- **Data Display**: It displays the fetched data in a tabular format.
- **Sorting**: Users have the option to sort the displayed data based on stock ratings.
- **Data Visualization**: The script can generate a bar plot to visualize the stock ratings.
- **Error Handling**: It handles errors gracefully, logging them for debugging purposes.
- **Multiprocessing**: To improve efficiency, the script employs multiprocessing for fetching data for multiple stocks concurrently.
- **Logging**: Detailed logging is implemented to track the execution flow and any encountered errors.

## Prerequisites
- Python 3.x
- Required Python packages: `requests`, `csv`, `yfinance`, `pandas`, `matplotlib`
- Internet connection to fetch stock data from Yahoo Finance

## Usage
1. **Install Dependencies**: Ensure that all required Python packages are installed. You can install them via pip:
   ```
   pip install requests yfinance pandas matplotlib
   ```
2. **Prepare Stock List**: Create a CSV file containing a list of stock symbols, with one symbol per line.
3. **Run the Script**: Execute the script `main.py`. You'll be prompted to enter the filename of the CSV containing stock symbols and whether to sort the data.
4. **View Data**: After execution, the script will display the fetched stock data. If opted, it will also generate a bar plot for visualization.
5. **Save Successful Symbols**: Optionally, you can choose to save the symbols for which data was successfully fetched into another CSV file.

## Logging
- Logs are stored in a file named `myapp.log` in the same directory as the script.
- Log entries include timestamps, log levels, and detailed messages for better debugging.

## Additional Notes
- Ensure that the provided CSV file contains valid stock symbols.
- If any errors occur during execution, refer to the log file for detailed information.
- For further assistance or inquiries, feel free to contact the script maintainer.


   



