import requests
import csv
import yfinance as yf
from tabulate import tabulate

stocks = []
with open("stocks1.csv") as file:
    for line in csv.reader(file):
        stocks.append(line[0])
data = []
headers = ["rate", "Symbol"]
count = 0
print("Data loaded ...")
for stock in stocks:
    try:
        msft = yf.Ticker(stock)
        data.append([msft.info["recommendationMean"], msft.info["symbol"]])
        count = count + 1

    except (KeyError, requests.exceptions.HTTPError):
        continue


print(tabulate(sorted(data), headers, tablefmt="grid"))
print(f"{count} stocks founded")
