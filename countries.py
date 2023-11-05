"""This script shows how to retrieve the content of a web page using requests and Beautiful Soup.
The page we are going to work on is a sandbox of www.scrapethissite.com"""

import requests
from bs4 import BeautifulSoup as bs
# import openpyxl as xl

# Target
page = "https://www.scrapethissite.com/pages/simple/"

# Make request and parse content
response = requests.get(page)
soup = bs(response.content,"html.parser",from_encoding="latin-1")    
countries = soup.find_all(name="div",class_="col-md-4 country")

for country in countries:
    name = country.h3.text.strip()
    capital = country.find("span",class_="country-capital").text.strip()
    population = country.find("span",class_="country-population").text.strip()
    area = country.find("span",class_="country-area").text.strip()
    print(f"Name: {name}\nCapital: {capital}\nPopulation: {population}\nArea(km^2): {area}\n") 