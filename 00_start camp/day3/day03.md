# 1907010 start camp - day03

### Review

* 요청은 주소로 가고 응답은 문서로 온다. 



## Quiz

```python
name = input('What\'s your name?: ') 
#name을 마지막에 읽는다. input을 읽고 그것을 name박스에 넣는다. 

print('hi, ' + name)
```

$ : 말해도 돼 라는 의미다. 

ctrl+c : 취소가 된다. 

ctrl+d : 이 터미널을 종료하겠다는 의미. 그러나 안될 수도 있다. 



프로세스  : 작업단위 하나하나

`input('What\'s your name?: ')` : ""는 \가 필요없으나 '' 쓰리고 했으니깐.

```python
#words = input('입력 고고: ')

# words의 첫 글자와 마지막 글자를 출력하라. 

import random

length = random.choice(range(1,100))    # 50
numbers = list(range(length)) #[0, 1, 2,... 49]
print(numbers[length - 1]) 

print(numbers[-1]) #마지막은 항상 -1이다.  



#numbers = [1,2,3,4,5]

#numbers 의 첫 요소와 마지막 요소를 출력하라

#numbers[0], numbers[4]
```



### 문자 처음과 마지막 추출

```python
words = input('입력 고고: ')	#words는 리스트이다. str이다. input안의 내용은 영향을 받지 않는다. 
print(type(words))  #항상 사용자의 입력을 받으면 str이 나온다. 

# words의 첫 글자와 마지막 글자를 출력하라. 
print(words[0], words[-1])  #문자열도 리스트이다. 숫자도 문자열에서 가능하구나!! 

#이렇게 굳이 하지 않아도 된다. 알아서 리스트화 된다. 
my_list = list(words)
print(my_list[0], my_list[-1])
```

- `numbers[-1]` : 마지막은 항상 -1이다.  

- 박스안의 값보단 얘의 class(타입)가 무엇인지가 중요하다. 어떤 타입인지?

  `type()` 



### 자연수 출력(1부터 n까지)

```python
# n 을 입력받고, 1부터 n까지 출력하라

n = input('자연수를 입력하세요: ')   #'10' => 10 으로 바꾸어야 출력할 수 있다. 
print(type(n))
n = int(n)  #str은 list(str)가 될 수 있었다. / str => int(str) : int는 정수로 만들어준다. 그러나 모두가능한 것은 아니다.  
print(type(n))


#1부터 n까지 출력하라
for i in range(n):
   print(i + 1, end=',')
```



`print` 는 출력할때 엔터가 자동으로 기본값으로 되어있다. 

 end=',' 를 통해서 조정할 수 있다. 



### `%` 짝수 홀수 구분

```python
#string = input('숫자를 입력하세요: ')
#number = int(string)

number = int(input('숫자를 입력하세요: '))

# 짝수/홀수를 구분하자. 2=>짝! 3=>홀!
if number % 2 == 1:
    print('홀!')
else:
    print('짝!')
```

* 가로로 코드가 길어지면 가독성이 떨어진다.

* `%` : 나누어서 나머지를 알 수 있다. 

  EX. 3%2 => 1

  

#### fizz buzz

```python
number = int(input('숫자를 입력하세요: '))

# 1 ~ number까지 출력
# 그와중에 3배수 fizz/ 5배수 buzz/ 15배수 fizz buzz

for i in range(1, number + 1):
    if i % 15 == 0:         
        print('Fizz Buzz') 
    elif i % 5 == 0:
        print('Buzz')
    elif i % 3 == 0:
        print('Fizz') 
    else:
        print(i)
```



### check_lotto (추후에 진행)

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

```



#### pick_lotto

```python
import random

numbers = range(1,46)
lucky_numbers = random.sample(numbers, 6)
```

* 현실데이터는 대부분 kye 와 value 로 표현된다. 



### 데이터를 가져오는 방법

1. 스크래핑 : 눈으로 보기는 쉬우나 많은 작업을 해야한다. 

2. API : 보통 딕셔너리 형태로 제공한다.

   ​		 깔끔하게 많은 정보를 딕셔너리화되어 있어서

3. 패키지, 모듈 : inexfinace 

   ​						가져다 써 주세요. 그러나 대부분 제공하지 않는다. 



#### get_lotto

```python
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

[39, 34, 37, 15, 29, 9]
```

* API로 받아오는 정보도 무조건 스트링이다. 

* `data` : 스트링을 딕셔너리로 만드는 방법
* `items` : value 값이 등장한다. (원래는 딕셔너리는 for에 넣으면 key 값만 나온다. )



### server

#### first web app_app

`flask` : 요청이 들어오면 응답을 한다. 

var routing : 사용자 입력을 받는 방법 

```python
from flask import Flask
import random

app = Flask(__name__)
					# 두칸씩 띄어야 한다.

@app.route('/')     # / 뒤에 오면 def 밑의 내용을 실행해라. 
def index():
    return 'Hello World'


@app.route('/hi')     
def hi():
    return 'Hi'


@app.route('/pick_lotto')     
def pick_lotto():
    numbers = range(1,46)
    lucky = random.sample(numbers, 6)
    return str(lucky)
    

if __name__ == '__main__':
    app.run(debug=True)

```

* 비지니스 로직 
* `route` :  길이라는 의미



```python
@app.route('/pick_lunch/<int:count>')   #사용자 입력을 받는 방법 : var routing
def pick_lunch(count):
    menus = [
        '짜장면',
        '짬뽕',
        '탕수육',
        '볶음밥',
        '사천탕수육',
        '마라탕'
    ]
    picks = random.sample(menus, count)
    return str(picks)         #스트링만 나갈 수 있다.  
```



#### 세제곱수 구하기

```python
@app.route('/cube/<int:count>')
def cube(count):
    return str(count ** 3)	
```



### 문서작성법

#### HTML

```html
<!DOCTYPE html>
<html>
    <head>					
        <meta charset="utf-8">
    </head>
    <body>
        <h1>Today I Learned</h1>
        <h2>Learn Flask</h2>
        <ol>
            <li>pip install flask</li>
            <li>touch app.py</li>
            <li>python app.py</li>
        </ol>

        <h2>Learn HTML</h2>
        <u1>
            <li>doctype html</li>
            <li>head, body</li>
            <li>h1, h2, ol, ul, li</li>
        </u1>
    </body>
</html>
```

* HTML 은 무조건 ""을 사용할 것이다. (python은 '')







