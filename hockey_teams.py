"""Here we are gonna work with common website interface components by building a web scraper that can conduct searches and paginate through the results."""

import requests
from bs4 import BeautifulSoup as bs
import pandas as pd

# Target
page = "https://www.scrapethissite.com/pages/forms/?per_page=100"# here you can change the number of rows per page (25/50/100)

# Make request and parse content
response = requests.get(page)
response.encoding = "latin-1"
soup = bs(response.content,"html.parser",from_encoding="latin-1")

# Create dataframe
table = soup.find("table")
columns = table.find_all("th")
column_titles = [col.text.strip() for col in columns]
df = pd.DataFrame(columns = column_titles)

# Fill dataframe 
column_data = table.find_all("tr")
for row in column_data[1:]:
    row_data = row.find_all("td")
    individual_row_data = [data.text.strip() for data in row_data]
    length = len(df)
    df.loc[length] = individual_row_data

# Create excel file
df.to_excel("dataframe.xlsx",index=False)