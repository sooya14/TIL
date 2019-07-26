# 1907011 start camp - day04



###  HTML 수정작업

https://startbootstrap.com/



* 스테틱웹(정적인 웹) : 내가 직접 찾아서 해야한다. 

  index.html 이 기본적으로 설정되어 있기 때문에 입력하지 않아도 열린다. 

* 다이나믹 웹(웹어플리케이션) :  flask / 파일과 상관없이 능동적으로 움직인다. 



## second_flask



### dday

```python
@app.route('/dday')
def dday():
    today = datetime.datetime.now()
    end_date = datetime.datetime(2019, 11, 29)
    left = end_date - today

    return f'SSAFY 2기 1학기 종료일까지 {left.days} 일 남았습니다.'
```



```python
from flask import Flask, render_template
import datetime


@app.route('/dday')
def dday():
    today = datetime.datetime.now()
    end_date = datetime.datetime(2019, 11, 29)
    left = end_date - today

    return render_template('dday.html', left_days=left.days)


if __name__ == '__main__':
    app.run(debug=True)
```



```html
<!DOCTYPE html>
<html lang="ko">
<head>
    <meta charset="UTF-8">
    
    <title>D-day</title>
</head>
<body>
    <h1>SSAFY 1학기 종료 까지</h1>
    <h2>{{ left_days }}일 남았습니다.</h2>
</body>
</html>
```

* ! + Tad :  기본설정이 만들어진다. 
* ??일 >> 문서이기때문에 
* 계산한 데이터들을 실어서 보내주어야 한다. 



### boxoffice

``` python
@app.route('/boxoffice')
def boxoffice():
    top_5 = [
        '스파이더맨 파 프롬 홈',
        '알라딘',
        '토이스토리4',
        '라이온킹',
        '기생충'
    ]

    return render_template('boxoffice.html', movies=top_5)
```

* a=b : a 는 박스 이름이다. 이름은 최대한 적게 짓는 것이 좋다. 

  ​		추출되는 것은 b 이다. 

  

```html
<!DOCTYPE html>
<html lang="ko">
<head>
    <meta charset="UTF-8">
    <title>Box office</title>
</head>
<body>
    <h1>box office</h1>
    <ol>
        {% for movie in movies %}
            <li>{{  movie  }}</li>
        {% endfor %}    
    </ol>
</body>
</html>
```

* {}  : 로직
* {{}} : 값? 보여주기



### index

링크 클릭해서 들어가기

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>index</title>
</head>
<body>
    <nav>
        <u1>
            <li><a href="/dday">dday</a></li>
            <li><a href="/boxoffice">boxoffice</a></li>
            <li><a href="#">??</a></li>
        </u1>
    </nav>
</body>
</html>
```





### send & recieve

#### app.py

```python
@app.route('/send')
def send():
    return render_template('send.html')


@app.route('/receive')      #요청이 들어오는 경로
def receive():
    data = request.args.get('msg')       #요청중에 넘어온 데이터들만 프린트 해라
    return render_template('receive.html', data=data)      #요청을 응답하는 곳
```



### send.html

``` html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Send message</title>
</head>
<body>
    <h1>Send message here</h1>
    <form action="/receive">
        <input type="text" name="msg">
        <input type="submit" value="보내기">
    </form>
</body>
</html>
```

* input  : 자동완성이 되지 않는다. 

* 기본값으로  text 형식으로 화면에 나오게 되어있다. 

* `<input type="submit" value="보내기">` : 버튼이 '보내기'로 바뀐다.

* `name` 

  * 모든 것은 키와 밸류로 이루어져 있기 때문에 name 을 달아야한다. 

  * 사용자한테는 보이지 않지만 이 칸의 이름을 달아놓은 것이다. 그 속에 입력을 하고 전송을 하면 키는 name 밸류는 입력한 값으로 읽는다. 

  * 데이터를 지칭하기 위한 수단

  * vs `id` , `class` 

    * 같은 id 를 줄 수 없다. 문서 하나에 하나만 존재할 수 있다. 

    * 중복할 수 없다. 
    * 특정 요소들을 selec 하기 위해서 사용한다.



=> 여기서 실어서 보낸 정보가 다음 receive.html 에서 받아서 넘기는 것이다. 

#### receive.html

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>수신함</title>
</head>
<body>
    <h1>{{  data  }}</h1>
</body>
</html>
```



### stock 

#### 주식 정보 불러오기

```python
@app.route('/receive')      
def receive():
    data = request.args.get('msg')      
    token = 'pk_63c229409ff14b67a6cc81e38927f1c4'
    stock = Stock(data, token=token).get_quote()
    company_name = stock['companyName']
    latest_price = stock['iexRealtimePrice']

    return render_template(
        'receive.html', 
        c_name=company_name, 
        l_price=latest_price
    )      
```



#### receive.html

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>수신함</title>
</head>
<body>
    <h1>{{  c_name  }}</h1>
    <p>${{  l_price  }}</p>
</body>
</html>
```



### 숫자 더하기 

```python
@app.route('/add')
def add():
    return render_template('add.html')    #add.html => <input> *2


@app.route('/result')
def result():
    num1 = request.args.get('num1')    
    num2 = request.args.get('num2')    
    result = int(num1) + int(num2)

    return render_template('result.html', result=result)  
    #result.html => input_data 의 합
```

#### add.html

```html
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>add</title>
</head>
<body>
    <h1>숫자를 적으세요.</h1>
    <form action="/result">
        <input type="text" name="num1">
        <input type="text" name="num2">
        <input type="submit" value="더하기">
    </form>
</body>
</html>
```

* `form action` : 거의 필수적인 요소이다. 

* `type` 에서 `number` 로 설정하면 입력칸에 문자를 입력하는 경우를 회피할 수 있다. 

   => 그러나 웹상에서 수정을 할 경우 result.html 에서 오류가 발생한다. 

#### result.html

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>result</title>
</head>
<body>
    <h1>{{  result  }}</h1>
</body>
</html>
```



### art

```python
from art import *

@app.route('/art')
def art():
    return render_template('art.html')       



@app.route('/result')
def result():
    input_text = request.args.get('input_text')
    font = request.args.get('font')
    result = text2art(input_text, font=font)
    
    return render_template('result.html', result=result)
```

#### art.html

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Make art</title>
</head>
<body>
    <h1>Put some text</h1>
    <form action="/result">
        <input type="text" name="input_text">
        <select name="font">
            <option value="ranom">랜덤</option>
            <option value="block">블록</option>
            <option value="white_bubble">동그라미</option>
        </select>
        <input type="submit">
    </form>
</body>
</html>
```

* `select` : 사용자가 확정적으로 선택을 해야하는 경우 사용

#### result.html

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>result</title>
</head>
<body>
    <h1>Result</h1>
    <pre>{{  result  }}</pre>
</body>
</html>
```

* https://github.com/sepandhaghighi/art/blob/master/FontList.ipynb





* `method="GET"` : 기본값. 주소가 그대로 나온다.

* `method="POST"`/ `methods=['POST']` :  중요하게 처리해야하는 경우 사용한다. 

  ​																	  주소에 나타나지 않는다. 예) 비밀번호같은 경우 

 