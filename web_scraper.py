"""This script shows how to retrieve the content of a web page using requests and Beautiful Soup.
The page we are going to work on is a sandbox of www.scrapethissite.com"""

import requests
from bs4 import BeautifulSoup as bs
import openpyxl as xl

page = "https://www.scrapethissite.com/pages/simple/"

response = requests.get(page)
with open("content.txt","w") as content:
    content.write(str(response.content))