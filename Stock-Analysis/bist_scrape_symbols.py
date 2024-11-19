import csv
import requests
from bs4 import BeautifulSoup

# Define the URL of the webpage to scrape
url = "https://www.kap.org.tr/tr/bist-sirketler"

# Send a GET request to the URL and get the response
response = requests.get(url)

# Parse the HTML content of the response using BeautifulSoup
soup = BeautifulSoup(response.text, "html.parser")

# Find all 'a' tags with class 'vcell' and extract their href and text
links = soup.find_all('a', class_='vcell')

# Open a CSV file in write mode to store the extracted data
with open('symbols.csv', 'w', newline='', encoding='utf-8') as csvfile:
    # Create a CSV writer object
    csvwriter = csv.writer(csvfile)
    
    # Write the header row
    csvwriter.writerow(['Symbol'])
    
    # Iterate through each link found on the webpage
    # Extract the text from the link and remove any leading/trailing whitespace
    # Check if the extracted text contains unwanted phrases
    # Split the text by commas
    # Append '.IS' to each symbol and write it to the CSV file
    [csvwriter.writerow([symbol.strip() + ".IS"]) 
     for link in links 
     for text in [link.get_text(strip=True)]
     if "PwC BAĞIMSIZ DENETİM VE SERBEST MUHASEBECİ MALİ MÜŞAVİRLİK A.Ş" not in text and "A.Ş." not in text
     for symbol in text.split(",")]

