"""This script is designed to scrape data from a webpage that dynamically loads content using AJAX requests.
"""
from numpy import NaN
import requests
from bs4 import BeautifulSoup as bs
import pandas as pd
import time
import json

# main website
PAGE = "https://www.scrapethissite.com/pages/ajax-javascript/"

# first request
response = requests.get(PAGE)
# response.encoding="latin-1"
soup = bs(response.content,"html.parser",from_encoding="latin-1")
col_titles = soup.find_all("th")
titles = [title.text.strip() for title in col_titles]

# get all the links 
links = soup.find_all("a",class_="year-link")
years = [link.text.strip() for link in links]

# Scrape data in json format
data = []
for year in years:
    time.sleep(1)
    payload = {
    "ajax":"true",
    "year":year
    }
    # emulate AJAX requests
    response = requests.get(PAGE,params=payload)
    # response.encoding="latin-1"
    soup = bs(response.content,"html.parser",from_encoding="latin-1")
    json_string = soup.text
    # convert parsed response to json format and store it
    current_data = json.loads(json_string)
    for film in current_data:
        data.append(film)
    
# Create dataframe and excel file
df = pd.json_normalize(data)
df = df.replace(NaN,"-")
df.to_excel("films.xlsx",index=False)
print("**Data saved successfully**")
