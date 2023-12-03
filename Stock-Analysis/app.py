import requests
import csv
import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
import sys

args = sys.argv

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


#printing the data using pandas
df= pd.DataFrame(data, columns=['Rate', 'Symbol'])
if len(args) > 1 and args[1] == 'sort':
    sort_df=df.sort_values(by=['Rate'])
    print(sort_df)
else:
    print(df)

#plotting a bar-graph using matplotlib
if len(args) > 1 and args[1] == 'sort':
    plt.bar(sort_df['Symbol'], sort_df['Rate'], color='skyblue')
else:
    plt.bar(df['Symbol'], df['Rate'], color='skyblue')
plt.xlabel('Symbol')
plt.ylabel('Rate')
plt.title('Stock Ratings')

plt.xticks(rotation=45, ha='right')
plt.tight_layout()

plt.show()
