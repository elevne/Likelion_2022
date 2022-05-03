import requests
from bs4 import BeautifulSoup
from datetime import datetime

url = 'http://www.daum.net'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

results = soup.findAll('a', 'link_favorsch')

print(datetime.today().strftime('%Y년 %m월 %d일의 실시간 검색어 순위입니다. \n'))

for result in results:
    print(result.get_text(), '\n')