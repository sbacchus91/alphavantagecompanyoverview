import requests
import json
import csv
import sys
import pandas as pd


stocks=["CRM","AAPL","MSFT"]

companies = []
for x in stocks:
    API_URL = "https://www.alphavantage.co/query?function=OVERVIEW&symbol={}&apikey=E63WUCB1N4X4AX10".format(x)
    response = requests.get(API_URL)
    if(response.status_code != 200):
        sys.exit(0) #do not continue if failed to fetch folders
    else:
        response_json = response.json()
        companies.append(response_json)

df = pd.DataFrame(companies)
df.to_csv('output.csv', index=False)