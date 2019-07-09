import bs4
import requests
import csv

url = 'https://www.melon.com/chart/index.htm'

headers = {'User-Agent': ':)'} 
#사용자의 요원이다. 우리 대신해서 요청을 보내는 사람을 쓰라는 것. 
#약간의 변형이 필요한 경우도 있다. 

response = requests.get(url, headers=headers).text
text = bs4.BeautifulSoup(response, 'html.parser')
rows = text.select('.lst50')

writer = csv.writer(open('melon50.csv', 'w', encoding='utf-8', newline=''))
writer.writerow(['순위', '제목', '가수'])

for row in rows:
    rank = row.select_one('td:nth-child(2) > div > span.rank').text
    title = row.select_one('td:nth-child(6) > div > div > div.ellipsis.rank01 > span > a').text
    artist = row.select_one('td:nth-child(6) > div > div > div.ellipsis.rank02 > a').text
    writer.writerow([rank, title, artist])


