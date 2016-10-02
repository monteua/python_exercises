import requests
from bs4 import BeautifulSoup

url = "http://www.nytimes.com/"

r = requests.get(url)

r_html = r.text

soup = BeautifulSoup(r_html, "html5lib")
title = soup.findAll(class_='story-heading')

for item in title:
    if item.a:

        item = item.a.text.replace("\n", " ").strip()
        print item
    else:
        item = item.contents[0].strip()