# app/robo_advisor.py

import csv
import json
import os


from dotenv import load_dotenv
import requests

load_dotenv()


# utility function to convert float or integer to usd-formatted string (for printing)
def to_usd(my_price):
    return "${0:,.2f}".format(my_price)



#INFO INPUTS

api_key = os.environ.get("ALPHAVANTAGE_API_KEY")
#[print](api_key)

symbol = "IBM"  #accept user input

request_url = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol={symbol}&apikey={api_key}"

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
    low_price = tsd[date]["3. low"]
    high_prices.append(float(high_price))
    low_prices.append(float(low_price))



recent_high = max(high_prices)
recent_low = min(low_prices)


cutoff_one = (float(recent_low)) * 0.20         #20 percent of the recent low value
cutoff_two = cutoff_one + (float(recent_low))   #recent low value plus 20 percent of the recent low value



#
#INFO OUTPUTS
#


#csv_file_path = "data/prices.csv"

csv_file_path = os.path.join(os.path.dirname(__file__), "..", "data", "prices.csv")

csv_headers = ["timestamp", "open", "high", "low", "close", "volume"]

with open(csv_file_path, "w") as csv_file:
    writer = csv.DictWriter(csv_file, fieldnames=csv_headers)
    writer.writeheader()
    for date in dates:
        daily_prices = tsd[date]
        writer.writerow({
        "timestamp": date,
        "open": daily_prices["1. open"],
        "high": daily_prices["2. high"],
        "low": daily_prices["3. low"],
        "close": daily_prices["4. close"],
        "volume": daily_prices["6. volume"]
    })






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
if float(latest_close) < cutoff_two:
    print("RECOMMENDATION: BUY!")
else:
    print("RECOMMENDATION: DON'T BUY!")

if float(latest_close) < cutoff_two:
    print("BECAUSE THE STOCK'S LATEST CLOSING PRICE IS LESS THAN 20% ABOVE IT'S RECENT LOW.")
else:
    print("BECAUSE THE STOCK'S LATEST CLOSING PRICE IS GREATER THAN 20% ABOVE IT'S RECENT LOW.")

print("-------------------------")
print(f"WRITING DATA TO CSV: {csv_file_path}...")
print("-------------------------")
print("HAPPY INVESTING!")
print("-------------------------")
