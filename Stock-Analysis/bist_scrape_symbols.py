import csv
import requests
from bs4 import BeautifulSoup
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s')

# Define the URL of the webpage to scrape
url = "https://www.kap.org.tr/tr/bist-sirketler"

# Set up the headers to mimic a real browser request
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}

# Send a GET request to the URL and get the response
try:
    response = requests.get(url, headers=headers)
    response.raise_for_status()  # Raise an exception if the request was unsuccessful (status code 4xx or 5xx)
    logging.info("Successfully fetched the webpage.")
except requests.exceptions.RequestException as e:
    logging.error(f"Failed to fetch webpage: {e}")
    exit(1)  # Exit the program if the request fails

# Parse the HTML content of the response using BeautifulSoup
soup = BeautifulSoup(response.text, "html.parser")

# Find all 'a' tags with class 'vcell' and extract their href and text
links = soup.find_all('a', class_='vcell')

# Open a CSV file in write mode to store the extracted data
csv_filename = 'symbols.csv'
try:
    with open(csv_filename, 'w', newline='', encoding='utf-8') as csvfile:
        # Create a CSV writer object
        csvwriter = csv.writer(csvfile)
        
        # Write the header row
        csvwriter.writerow(['Symbol'])
        
        # Iterate through each link found on the webpage
        for link in links:
            # Extract the text from the link and remove any leading/trailing whitespace
            text = link.get_text(strip=True)
            
            # Check if the extracted text contains unwanted phrases
            if "PwC BAĞIMSIZ DENETİM VE SERBEST MUHASEBECİ MALİ MÜŞAVİRLİK A.Ş" not in text and "A.Ş." not in text:
                # Split the text by commas
                for symbol in text.split(","):
                    # Append '.IS' to each symbol and write it to the CSV file
                    cleaned_symbol = symbol.strip() + ".IS"
                    csvwriter.writerow([cleaned_symbol])
                    logging.info(f"Symbol '{cleaned_symbol}' written to CSV.")
    logging.info(f"Symbols successfully saved to {csv_filename}.")
except Exception as e:
    logging.error(f"An error occurred while writing to CSV: {e}")
