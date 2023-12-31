"""Here we are gonna work with common website interface components by building a web scraper that can retrieve data through different pages."""

import requests
from bs4 import BeautifulSoup as bs
import pandas as pd
import time

# URLs
PAGE = "https://www.scrapethissite.com/pages/forms/?per_page=100"# here you can change the number of rows per page (25/50/100)
MAIN_WEBSITE = "https://www.scrapethissite.com"

def new_request(page):
    """Make a request with the correct encoding and return a BeautiflSoup object.

    Args:
        page (str): Target page.

    Returns:
        BeautifulSoup object: contain the parsed content of the webpage.
    """
    response = requests.get(page)
    # response.encoding="latin-1"
    soup = bs(response.content,"html.parser",from_encoding="latin-1")
    return soup

def scrape_table(current_table,dataframe):
    """Append the content of the table to the dataframe.

    Args:
        current_table (bs4.element.Tag): This object contain all the data of the current table
        dataframe (pandas.core.frame.DataFrame): Pandas object where the data is stored.
    """
    rows = current_table.find_all("tr")
    for row in rows[1:]:
        row_cells = row.find_all("td")
        row_data = [data.text.strip() for data in row_cells]
        length = len(dataframe)
        dataframe.loc[length] = row_data

def scrape_page(link,dataframe):
    """Makes a request to the current link and scrape its data.

    Args:
        link (str): New page to scrape.
        dataframe (pandas.core.frame.DataFrame): Pandas object where the data is stored.
    """
    soup = new_request(link)
    current_table = soup.find("table",class_="table")
    scrape_table(current_table,dataframe)
    
# Make first request 
soup = new_request(PAGE)

# Get list of links to the next pages
pagination_area = soup.find("ul",class_="pagination")
pages = pagination_area.find_all("a")
links = [MAIN_WEBSITE + link.get("href") for link in pages[1:-1]]

# Create dataframe
first_table = soup.find("table",class_="table")
column_titles = first_table.find_all("th")
titles = [title.text.strip() for title in column_titles]
hockey_df = pd.DataFrame(columns=titles)

# Fill dataframe
scrape_table(first_table,hockey_df)
for link in links:
    time.sleep(1)
    scrape_page(link,hockey_df)

# Save data on a excel file
hockey_df.to_excel("df_hockey_teams.xlsx",index=False)
print("**Data saved successfully**")
