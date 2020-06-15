# app/robo_advisor.py

import csv
import json
import os
import requests

# utility function to convert float or integer to usd-formatted string (for printing)

def to_usd(my_price):
    return "${0:,.2f}".format(my_price)



#INFO INPUTS

request_url = "https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol=IBM&apikey=demo"

response = requests.get(request_url)

parsed_response = json.loads(response.text)

last_refreshed = parsed_response["Meta Data"]["3. Last Refreshed"]

tsd = parsed_response["Time Series (Daily)"]

dates = list(tsd.keys())

latest_day = dates[0]

latest_close = tsd[latest_day]["4. close"]


high_prices = []
low_prices = []


for date in dates:
    high_price = tsd[date]["2. high"]
    high_prices.append(float(high_price))
    low_price = tsd[date]["3. low"]
    low_prices.append(float(low_price))


recent_high = max(high_prices)
recent_low = min(low_prices)


#
#INFO OUTPUTS
#


#csv_file_path = "data/prices.csv"

csv_file_path = os.path.join(os.path.dirname(__file__), "..", "data", "prices.csv")

csv_headers = 
with open(csv_file_path, "w") as csv_file:
    writer = csv.DictWriter(csv_file, fieldnames=["city", "name"])
    writer.writeheader()

    # looping

    writer.writerow({"city": "New York", "name": "Yankees"})





print("-------------------------")
print("SELECTED SYMBOL: IBM")
print("-------------------------")
print("REQUESTING STOCK MARKET DATA...")
print("REQUEST AT: 2018-02-20 02:00pm")
print("-------------------------")
print(f"LATEST DAY: {last_refreshed}")
print(f"LATEST CLOSE: {to_usd(float(latest_close))}")
print(f"RECENT HIGH: {to_usd(float(recent_high))}")
print(f"RECENT LOW: {to_usd(float(recent_low))}")
print("-------------------------")
print("RECOMMENDATION: BUY!")
print("BECAUSE: TODO")
print("-------------------------")
print(f"WRITING DATA TO CSV: {csv_file_path}...")
print("-------------------------")
print("HAPPY INVESTING!")
print("-------------------------")


