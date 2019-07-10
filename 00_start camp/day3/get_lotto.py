import requests
import json


url = 'https://www.dhlottery.co.kr/common.do?method=getLottoNumber&drwNo=866'   #딕셔너리가 아니라 스트링이었다. 

response = requests.get(url).text   

data = json.loads(response)  #스트링을 딕셔너리로 만드는 방법


real_numbers = []

for key, value in data.items():
    if 'drwtNo' in key:
        real_numbers.append(value)  

print(real_numbers)





