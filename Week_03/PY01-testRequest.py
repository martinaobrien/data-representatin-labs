import requests
from bs4 import BeautifulSoup

with open("../week02/carviewer2.html") as fp:
    soup - BeautifulSoup(fp,'html.parser')
page = requests.get("http://dataquestio.github.ie/web-scraping-pages/simple.html")
print (page)
print ("-------------")
print (page.content)
soup1 = BeautifulSoup(page.content, 'html.parser')
print ("-------------")
print (soup1.prettify())

