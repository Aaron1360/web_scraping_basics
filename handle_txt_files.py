"""This script shows how to retrieve the content of a web page using requests and Beautiful Soup.
The page we are going to work on is a sandbox of www.scrapethissite.com"""

import requests
from bs4 import BeautifulSoup as bs
# import openpyxl as xl

def save_html(soup):
    """This function saves the content of the HTML in a text file.
    It helps to locate the desired information."""
    with open("HTML_file.txt","w") as html_file:
        # # Solution 1
        # for _ in soup.contents:
        #     html_file.write(str(_))
        # Solution 2
        html_file.write(soup.prettify())
        print("***HTML content saved***")

def list_countries(tags):
    """This function retrieves all the countries from the page and saves them on a txt file."""
    with open("countries.txt","w") as file:
        for h3 in tags:
            file.write(h3.text.strip() + "\n")
        print("***Text saved***")

# Target
page = "https://www.scrapethissite.com/pages/simple/"

# Make request and parse content
response = requests.get(page)
soup = bs(response.content,"html.parser",from_encoding="latin-1")    

# save_html(soup=soup)# This file is used as a tool

# h3_tags = soup.find_all("h3")# Get tags and store info
# list_countries(tags=h3_tags)

# Show all the countries and related info
content = soup.find_all(name="div",attrs={"class","col-md-4 country"})
for country in content:
    print(country.text.strip())