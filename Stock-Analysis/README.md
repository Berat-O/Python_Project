<!-- Improved Docs -->

# Stock Analysis Made Easy: Analyze and Visualize Stock Ratings


<!-- Improved Docs -->
## Overview
This Python script empowers you to effortlessly analyze and visualize stock ratings, making informed investment decisions a breeze!



<!-- Improved Docs -->
## Powerful Features at Your Fingertips:
- **Effortless Data Fetching**: Tap into the power of Yahoo Finance to retrieve stock ratings for your chosen symbols.
- **Clear Data Presentation**: View the fetched data in a clean and easy-to-read table format.
- **Organized Sorting**: Gain deeper insights by sorting the data based on stock ratings, allowing you to prioritize high-potential stocks.
- **Visual Insights**:Uncover trends and patterns with a captivating bar chart that brings stock ratings to life!
- **Robust Error Handling**: Rest assured, the script gracefully handles errors, logging them for troubleshooting purposes. ️
- **Multiprocessing Power**:  Experience lightning-fast performance as the script leverages multiprocessing to fetch data for multiple stocks simultaneously. ⚡️
- **Detailed Logging**:Stay informed with comprehensive logs that track the script's execution flow and any encountered errors.

## Getting Started:

## Prerequisites
- Python 3.x
- Required Python packages: `requests`, `csv`, `yfinance`, `pandas`, `matplotlib`,`xlrd`,`openpyxl`
- Internet connection to fetch stock data from Yahoo Finance

## Usage
1. **Install Dependencies**: Ensure that all required Python packages are installed. You can install them via pip:
   ```
   pip install requests yfinance pandas matplotlib xlrd openpyxl
   ```
or 
   ```
   pip install -r requirements.txt
   ```
2. **Prepare Stock List**: Create a CSV file containing a list of stock symbols, with one symbol per line.
3. **Run the Script**: Execute the script `app.py`. You'll be prompted to enter the filename of the CSV containing stock symbols and whether to sort the data. The recommended file name is "topix_core30".
4. **View Data**: After execution, the script will display the fetched stock data. If opted, it will also generate a bar plot for visualization.
5. **Save Successful Symbols**: Optionally, you can choose to save the symbols for which data was successfully fetched into another CSV file.

<!-- Improved Docs -->
## Behind the Scenes:


-Logs are meticulously recorded in a file named myapp.log within the script's directory. These logs provide timestamps, log levels, and detailed messages for efficient troubleshooting.


<!-- Improved Docs -->
## Additional Notes:

-Double-check that your CSV file includes valid stock symbols.

-In case of any errors, the log file will provide valuable details for resolving the issue.

-For further assistance or questions, feel free to reach out to the script's maintainer.




