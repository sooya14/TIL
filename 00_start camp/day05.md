# 1907012 start camp - day05



### Lotto_day3

#### 방법1 (python 같지 않은)

```python
my = [1, 2, 3, 4, 5, 6]

real = [1, 2, 3, 4, 5, 7]
bonus = 6

# my 와 real 의 숫자가 모두 같으면 1등
# my 와 real 이 5개가 같고 나머지 하나가 bonus 면 2등
# my 와 real 이 5개가 같으면 3등
# '' 4개가 같으면 4등
# '' 3개가 같으면 5등
# 나머지는 꽝

match_count = 0
is_bonus = False        
#설정을 해놓지 않으면 기본값이 Trus로 설정되어 있기 때문에 중간에 오류가 발생한다. 

for i in my:    #이중 for문 
    if i == bonus:
        is_bonus = True
    for j in real:  # 위의 1은 고정, 이후 j 가 끝나야 i 가 다음으로 바뀐다. 
        if i == j:
            match_count += 1    # match_count = match_count + 1 같은 것


if match_count == 6:
    result = '1등'      
elif match_count == 5:
    if is_bonus:
        result = '2등'
    else:
        result = '3등'
elif match_count == 4:
    result = '4등'
elif match_count == 3:
    result = '5등'
else:
    result = '꽝'
```

* 모든 코드에서 사용가능한 코드 (문법을 알고 있으면)
* 이중 `for` 문 : 전체비교를 하는 방법
* print` : 코딩의 종결이 아니다. print로 끝날 수 없다. 터미널에서 확인용



#### 방법2

```python
match_count = 0

# is_bonus = False    
# if bonus in my:
#     is_bonus = True	#아래에 my 에 bonus 가 있을 때만 비교를 해놓았기 때문에 필요가 없다. 

for i in my:    
    for j in real:  
        if i == j:
            match_count += 1    


if match_count == 6:
    result = '1등'      
elif match_count == 5:
    if bonus in my:
        result = '2등'
    else:
        result = '3등'
elif match_count == 4:
    result = '4등'
elif match_count == 3:
    result = '5등'
else:
    result = '꽝'
```

* 방법1 보다 python 스러운 방법



#### 방법3

```python
match = set(my).intersection(set(real))   #집합 / 교집합              
match_count = len(match)    

if match_count == 6:
    result = '1등'      
elif match_count == 5:
    if bonus in my:
        result = '2등'
    else:
        result = '3등'
elif match_count == 4:
    result = '4등'
elif match_count == 3:
    result = '5등'
else:
    result = '꽝'
```

* `set()` : 집합으로 만드는 것 / 집합은 순서가 없다. 
  * [1, 2, 3] => list / {1, 2, 3,} => set / (1, 2, 3) => tuple / {'a' : 'A'} => dictionary
* `intersection()`,  `&` : 교집합 = `&`
* `len()`: 갯수



## CHAT BOT QUEST



* venv : 독립환경, 가상환경 / 프로젝트 별로 따로 pip list 를 관리하게 된다.

  => 새로운 프로젝트를 진해할 때, 새로 세팅하는 것이 좋다. 



```python

```



* `request`
* localhost ~ : 나만 접속가능하다. 
* http://127.0.0.1:5000/ => port : 기본값이 5000 (5000번째 문) / 임의적으로 조정이 가능하다. 

#### app.py

``` python
from flask import Flask, render_template, request
import requests 
from decouple import config

app = Flask(__name__)


api_url = 'https://api.telegram.org'
token = config('TOKEN')
chat_id = config('CHAT_ID')
secret_url = config('SECRET_URL')

@app.route(f'/{secret_url}', methods=["POST"])
def telegram():
    req = request.get_json()
    user = req['message']['from']['id']
    message = req['message']['text']

    if message == 'admin':
        res = '안녕하세요 관리자님 :)'
    else:
        res = '안녕하세요 손님 :)' 


    URL = f'{api_url}/bot{token}/sendMessage?chat_id={user}&text={res}'
    requests.get(URL)
    return ('success', 200)     # 200을 안하면 계속 보낸다. 


@app.route('/write')
def write():
    return render_template('write.html')


@app.route('/send')
def send():
    message = request.args.get('message')   # message 에는 사용자 input 저장
    URL = f'{api_url}/bot{token}/sendMessage?chat_id={chat_id}&text={message}' #주문서

    requests.get(URL)   #최종적인 주문을 하는 것
    return render_template('send.html')

if __name__ == '__main__':
    app.run(debug=True, port=80)
```



### 네이버 파파고 

```python
import requests

keyword = '띵작'

headers = {
    'X-Naver-Client-Id': 'hd64Y0JHk__fgKZcJ3wD',
    'X-Naver-Client-Secret': 'ktZ0ruu1s7',
}

data = {
    'source': 'ko',
    'target': 'en',
    'text': keyword,   # 마지막에도 쉼표를 적는 것이 바람직하다. 
}

res = requests.post(
    'https://openapi.naver.com/v1/papago/n2mt', 
    data=data, 
    headers=headers
)

result = res.json()['message']['result']['translatedText']
print(result)
```



```python
from flask import Flask, render_template, request
import requests 
from decouple import config

app = Flask(__name__)


api_url = 'https://api.telegram.org'
token = config('TOKEN')
admin_id = config('ADMIN_ID')
secret_url = config('SECRET_URL')
naver_client_id = config('NAVER_CLIENT_ID')
naver_client_secret = config('NAVER_CLIENT_SECRET')

@app.route(f'/{secret_url}', methods=["POST"])
def telegram():
    req = request.get_json()
    user = req['message']['from']['id'] # user 의 chat id
    message = req['message']['text']    # user의 입력 메세지

    ####
    headers = {
        'X-Naver-Client-Id': naver_client_id,
        'X-Naver-Client-Secret': naver_client_secret,
    }

    data = {
        'source': 'ko',
        'target': 'en',
        'text': message,   # 마지막에도 쉼표를 적는 것이 바람직 
    }

    res = requests.post(
        'https://openapi.naver.com/v1/papago/n2mt', 
        data=data, 
        headers=headers
    )

    result = res.json()['message']['result']['translatedText']
    ####

    URL = f'{api_url}/bot{token}/sendMessage?chat_id={user}&text={result}'
    requests.get(URL)
    return ('success', 200)     # 200을 안하면 계속 보낸다. 
```



```python
from flask import Flask, render_template, request
import requests
from decouple import config

app = Flask(__name__)

api_url = 'https://api.telegram.org'
token = config('TOKEN')
admin_id = config('ADMIN_ID')
secret_url = config('SECRET_URL')
naver_client_id = config('NAVER_CLIENT_ID')
naver_client_secret = config('NAVER_CLIENT_SECRET')

commands = [
    '/번역 <키워드>',
    '/미세먼지',
]


@app.route(f'/{secret_url}', methods=['POST'])
def telegram():
    req = request.get_json()
    user = req['message']['from']['id']  # user 의 chat id
    message = req['message']['text']  # user 의 입력 메시지
    no_error = '존재하지 않는 명령어 입니다.'

    if message[0] == '/':
        if ' ' in message:  # 띄어쓰기 후에 추가 input 있음
            words = message.split(' ')  # ['/번역', '띵작']
            							#split : ' '를 통해서 분리
            if words[0] == '/번역':
                headers = {
                    'X-Naver-Client-Id': naver_client_id,
                    'X-Naver-Client-Secret': naver_client_secret,
                }

                data = {
                    'source': 'ko',
                    'target': 'en',
                    'text': words[1],
                }

                res = requests.post('https://openapi.naver.com/v1/papago/n2mt', data=data, headers=headers)
                result = res.json()['message']['result']['translatedText']  # 번역 결과
            
            else:
                result = no_error
        else:  # 띄어쓰기 없음
            if message == '/미세먼지':
                result = '좋음'
            else:
                result = no_error
    else:
        result = str(commands)



    URL = f'{api_url}/bot{token}/sendMessage?chat_id={user}&text={result}'
    requests.get(URL)
    return ('success', 200)

if __name__ == '__main__':
    app.run(debug=True, port=80)	
```



### 다른 컴퓨터에서도 사이트 이용

* python anywhere : 등록시 `debug=` 를 `False` 로 바꿔야한다. 

