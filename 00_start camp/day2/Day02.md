# 190709 start camp - day02

## What is git

* Git

  * scm (source code manager) 
  * vcs (version control system) 

* git => 버전관리를 해주는 감시카메라같은 존재 

  

* (master) 가 붙으면  git 이 관리한다는 의미이다. 

* cd .. : 위로 간다는 의미. 상위폴더/ cd TIL : TIL 을 들어간다는 의미. 더블클릭

*  mkdir 폴더명 :  폴더를 생성한다. >>폴더라는 말 보다 디렉토리라는 말을 쓴다. 

* tab 을 누르면 어느정도 자동완성을 해준다. 

* git init 하면 관리가 된다. 

* `touch ` :  생성한다. 

* `rm` : 제거한다. 

* 띄어쓰기가 핵심이다. 

* `ls` : 리스트

* final-처음만들었음.txt : git commit -m '처음 만들었음'

* add 잠깜만 여기 볼게요~ / commit 의 반복이다. 

* git log  라고 치면 갤러리를 볼 수 있다. 



* 정리

  `git init`

  `git add <filename>`

  `git commit -m '<message>`

  변경사항 저장

  `git add <filename>`

  `git commit -m '<message>`

  ...

​		`git sataus` => 상태를 물어보는 명령어

​		`git log` => 사진(commit)를 로그를 보여줌



git == 내 로컬 카메라 

github==드라이브, SNS. 공개프로젝트 // gitlab: 숨기는 기능을 잘한다. 팀프로젝트 // 





하위 파일은 자동으로 마스터 관리가 된다. 

git add -A 또는 git add .  : 지금 내가 있는 것을 통째로 하겠다. 



git 이 관리하는 폴더를 repo 라고 부른다. 



매일매일 퇴실버튼 누리기전에... 

git add . -m '블라블라'

git push github master



```python
import webbrowser

urls = [
    'www.github.com',
    'www.google.com',
    'www.edu.ssafy.com',
    'www.naver.com',
    'www.youtube.com'
    ]

for url in urls:
    webbrowser.open(url)
```



### 웹은 요청과 응답이다.

요청: 브라우저는 요청을 보내주는 프로그램이다. 주소(url)로 보내는 것이다. 

응답: 문서로 온다. 

* 핵심: 요청(주소) >> 응답(문서)

클릭의 모든 핵심은 주소창을 바꾸는 것이다. 주소가 바뀌는 것이 핵심이다! 



## requests

`requests` 는 우리가 따로 사야하는 물건이다. 

터미널에서 `pip install requests`



```python
import requests
import bs4

url = 'https://finance.naver.com/sise/'
response = requests.get(url).text
text = bs4.BeautifulSoup(response,'html.parser') #이쁘게 만들어준다. 
kospi = text.select_one('#KOSPI_now') 
#F12 눌러서 웹에서 확인하여 복사해오기 (copy selector)

print(kospi.text)
```

url 과 

* `bs4` : 예쁘게 만들어주는 코드

* 한번 샀으니깐 또 안써도 되다. 

* rows : 가로

  

### melon 50 순위 가져오기

```python
import bs4
import requests

url = 'https://www.melon.com/chart/index.htm'

headers = {'User-Agent': ':)'} 
#사용자의 요원이다. 우리 대신해서 요청을 보내는 사람을 쓰라는 것. 
#약간의 변형이 필요한 경우도 있다. 

response = requests.get(url, headers=headers).text
text = bs4.BeautifulSoup(response, 'html.parser')
rows = text.select('.lst50')

for row in rows:
    rank = row.select_one('td:nth-child(2) > div > span.rank').text
    title = row.select_one('td:nth-child(6) > div > div > div.ellipsis.rank01 > span > a').text
    artist = row.select_one('td:nth-child(6) > div > div > div.ellipsis.rank02 > a').text
    print(rank, title, artist)
```

* 200 : 웹상에서 ok 라는 상징이다. 
* 406 : not acceptable. 너의 코드를 받지 않는다. 



* `print(rows)` : rows는 list이다. / type()안에 궁금한 것을 넣어서 물어보면 어떤 유형인지 알려준다. 

  



### 파일조작

file_write

```python
lunches = {
    '양자강' : '02-557-4211',
    '김밥카페' : '02-553-3181',
    '순남시래기' : '02-508-0887'
}

#파일을 열기위한 문법
with open('lunch.csv', 'w', encoding='utf-8') as f:
    for name, phone in lunches.items():
        f.write(f'{name}, {phone}\n')
```

* utf-8 은 한글일 때, 깨짐을 방지하기 위해 작성

  

file_read

```python
import csv

#내가 이 파일은 읽고 f 라고 부르겠다. 
with open('lunch.csv', 'r', encoding='utf-8') as f:
    items = csv.reader(f)
    for item in items:
        print(item)
```

* git commit -m 'typo' : 약간의 수정만 할때 



멜론

```python
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
```





