# _*_ coding:utf-8 _*_
import requests
from bs4 import BeautifulSoup

file_name = raw_input("enter the file name: ")
file_name = file_name + ".txt"
fhand = open(file_name, 'w')



url = "http://www.vanityfair.com/style/society/2014/06/monica-lewinsky-humiliation-culture"

r = requests.get(url)

r_html = r.text

soup = BeautifulSoup(r_html, "html5lib")

article = soup.find_all(class_="content-section")

for item in article:
    if item.p or item.em:
        print item.text
        text = item.text
        fhand.write(text.encode("utf-8"))
fhand.close()