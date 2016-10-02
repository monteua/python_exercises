import requests
from bs4 import BeautifulSoup

url = "http://www.vanityfair.com/style/society/2014/06/monica-lewinsky-humiliation-culture"

r = requests.get(url)

r_html = r.text

soup = BeautifulSoup(r_html, "html5lib")

article = soup.find_all(class_="content-section")

for item in article:
    if item.p or item.em:
        print item.text