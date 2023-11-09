import requests
from bs4 import BeautifulSoup as bs
import time

PAGE = "https://www.scrapethissite.com/pages/frames/"
MAIN_WEBSITE = "https://www.scrapethissite.com"

def new_request(page):
    response = requests.get(page)
    # response.encoding="latin-1"
    soup = bs(response.content,"html.parser",from_encoding="latin-1")
    return soup

soup = new_request(PAGE)
real_page = MAIN_WEBSITE + soup.find("iframe")["src"]

real_soup = new_request(real_page)

turtles_div = real_soup.find_all("div",class_="col-md-4 turtle-family-card")

# names = [name.find("h3").text for name in turtles_div]

turtles_pages = [MAIN_WEBSITE + page.find("a")["href"] for page in turtles_div]

with open("turtles_data.txt","w") as file:
    for page in turtles_pages:
        time.sleep(1)
        turtle_soup = new_request(page)
        name = turtle_soup.find("h3").text.strip()
        text = turtle_soup.find("p").text.strip()

        if "\u2014" in text:
            text = text.replace("\u2014","-")
        file.write(name+"\n")
        file.write(text+"\n\n")

print("TURTLES DATA SAVED SUCCESSFULLY")
        
        