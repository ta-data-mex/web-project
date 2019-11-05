import requests
from bs4 import BeautifulSoup

url = 'https://www.ign.com/reviews/games'
html = requests.get(url).content
print(html)
#soup = BeautifulSoup(html, "lxml")
