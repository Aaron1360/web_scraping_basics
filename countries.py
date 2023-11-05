"""This script shows how to retrieve the content of a web page using requests and Beautiful Soup.
The page we are going to work on is a sandbox of www.scrapethissite.com"""

import requests
from bs4 import BeautifulSoup as bs
# import openpyxl as xl

def scrape_data(countries):
    """This function organizes the desired data on a list of dictionaries.

    Args:
        countries (bs4.element.ResultSet): Object that holds all the HTML tags that match the specified criteria.

    Returns:
        list: List of dictionaries where each dictionary represents a country.
    """
    list_of_countries = []
    for country in countries:
        new_country = {}
        new_country["name"] = country.h3.text.strip()
        new_country["capital"]= country.find("span",class_="country-capital").text.strip()
        new_country["population"] = country.find("span",class_="country-population").text.strip()
        new_country["area"] = country.find("span",class_="country-area").text.strip()
        list_of_countries.append(new_country)
    return list_of_countries

def show_info(data):
    for country in data:
        for key,value in country.items():
            print(f"{key}: {value}")
        print()

def save_txt(data):
    """Stores the information on list_of_countries.txt

    Args:
        data (list): List of dictionaries with country information.
    """
    with open("list_of_countries.txt","w") as file:
        for i,country in enumerate(data):
            file.write(f"{i+1}.- ")
            for key,value in country.items():
                if key == "name":
                    file.write(f"{key}: {value}.\n")
                else:
                    file.write(f"\t{key}: {value}.\n")
            file.write("\n")
    print("**Info saved successfully**")
    
# Target
page = "https://www.scrapethissite.com/pages/simple/"

# Make request and parse content
response = requests.get(page)
response.encoding = "latin-1"
soup = bs(response.content,"html.parser",from_encoding="latin-1")    
countries = soup.find_all(name="div",class_="col-md-4 country")

data = scrape_data(countries)
# show_info(data)
save_txt(data)
