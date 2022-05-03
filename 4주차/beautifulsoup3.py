import requests
from bs4 import BeautifulSoup

url = 'http://www.daum.net'
response = requests.get(url)

soup = BeautifulSoup(response.text, 'html.parser')

print(soup.title)