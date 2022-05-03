import requests
from bs4 import BeautifulSoup
from datetime import datetime

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'}
url = 'http://https://datalab.naver.com/'
response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, 'html.parser')
rank = 1

results = soup.findAll('span', 'item_title')

search_rank_file = open('rankresult.txt', 'w')


print(datetime.today().strftime('%Y년 %m월 %d일의 실시간 검색어 순위입니다. \n'))

for result in results:
    search_rank_file.write(str(rank)+'위: '+result.get_text()+'\n')
    print(result.get_text(), '\n')
    rank += 1