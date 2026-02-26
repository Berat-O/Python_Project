import pandas as pd
import os
import logging

'''
This is an example.
This pulls data from the Tokyo Stock Exchange to obtain a CSV of stocks for which data is available.
Please try to acquire other stocks as well.
'''
def fetch_and_save_core30():
    # URL of list of listed stocks (Excel) from JPX official website
    # Japanese listed stocks
    # This file contains market segmentation and size segmentation for all listed stocks
    jpx_url = "https://www.jpx.co.jp/markets/statistics-equities/misc/tvdivq0000001vg2-att/data_j.xls"
    
    print("Obtaining the latest stock list from JPX...")
    try:
        # Read the Excel file (using pandas read_excel) 
        # Extract stocks with 'TOPIX Core30' listed in '規模区分（Size category）' column
        df = pd.read_excel(jpx_url)
        
        # Filter only those with size category TOPIX Core30
        core30_df = df[df['規模区分'] == 'TOPIX Core30']
        
        if core30_df.empty:
            print("TOPIX Core30 stocks were not found. Please check the URL and file format.")
            return

        # Convert the stock code to a format that can be used by yfinance (e.g. 7203.T) 
        # Convert the number in the 'code' column to a string and add '.T' to the end
        symbols = core30_df['コード'].astype(str).apply(lambda x: x + ".T").tolist()

        # Save as CSV
        directory = "data"
        if not os.path.exists(directory):
            os.makedirs(directory)
            
        output_path = os.path.join(directory, "topix_core30.csv")
        
        # Save without index and header (to match existing load_stocks.py specifications)
        pd.Series(symbols).to_csv(output_path, index=False, header=False)
        
        print(f"Success: {len(symbols)} stocks are saved on {output_path}")
        print("stocks sample:", symbols[:5])

    except Exception as e:
        print(f"Error!!: {e}")

if __name__ == "__main__":
    fetch_and_save_core30()