from bs4 import BeautifulSoup as bs
from PIL import Image
from pathlib import Path
import requests
import io
import hashlib
import time

PAGE = "https://www.scrapethissite.com/pages/frames/"
MAIN_WEBSITE = "https://www.scrapethissite.com"
PATH = "/home/remote/Documents/python_dev/github_repos/web_scraping_basics/turtles_img"

def new_request(page):
    response = requests.get(page)
    soup = bs(response.content,"html.parser",from_encoding="latin-1")
    return soup

def scrape_text(turtle_soup,file):
    name = turtle_soup.find("h3").text.strip()
    text = turtle_soup.find("p").text.strip()
    if "\u2014" in text:
        text = text.replace("\u2014","-")
    file.write(name+"\n")
    file.write(text+"\n\n")
    
# TODO: fix response 403 and downlad all the images on PATH 

# def scrape_images(turtle_soup):
#     img_src = turtle_soup.find("img",class_="turtle-image center-block").get("src")
#     if ".JPG" in img_src:
#         img_part = img_src.split(".JPG")[0]
#     else:
#         img_part = img_src.split(".jpg")[0]
#     cleaned = img_part.replace("thumb/","")
#     url = f"{cleaned}.jpg"
#     filename = url.split("/")[-1]
#     img = requests.get(url,headers={"Content-Type": "image/jpeg"})
#     print(img.status_code)
#     # if img.status_code != 200:
#     #     print("Error getting {filename}")
#     # else:
#     #     with open(PATH+filename,"wb") as f:
#     #         f.write(img.content)
#     #         print("Save {filename}")
            
soup = new_request(PAGE)
real_page = MAIN_WEBSITE + soup.find("iframe")["src"]

real_soup = new_request(real_page)

turtles_div = real_soup.find_all("div",class_="col-md-4 turtle-family-card")

turtles_pages = [MAIN_WEBSITE + page.find("a")["href"] for page in turtles_div]

with open("turtles_data.txt","w") as file:
    for page in turtles_pages:
        time.sleep(1)
        turtle_soup = new_request(page)
        scrape_text(turtle_soup,file)
        # scrape_images(turtle_soup)

print("TURTLES DATA SAVED SUCCESSFULLY")
