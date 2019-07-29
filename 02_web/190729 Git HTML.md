# Git & HTML |190729



## git bash



`master` :  없으면 git 이 관리하지 않고 있는 상태를 의미한다. 

`~` : home 이라는 의미 



`cd ..` 밖으로 나오는 것 



- 프로젝트 할 때 사용한다. 



### 버전 관리 



`mkdir 폴더명` : 폴더 생성



`git init` : '.git '이라는 폴더가 생긴다. => master 가 된다. 

​					 repo가 된다. == git 이 관리하고 있다. 



`touch .gitignore`  => 가장 먼저 만들어서 작성해야한다. 

- gitignore : 관리하면 안되는 것들을 나열한다. 

- `git add .gitignore` : git 이 추적을 할 수 있게 만든다. => 트랙킹을 시작한다. 
  - 수정이 된 후에도 추가적으로 다시 스테이지에 올려야한다. 
- `git rm --cached .gitignore` : 트랙킹을 끊고 싶을 때 사용

```python
venv/ 
.env
```



`git add .` => (주의) 위치가 중요하다. 그 위치에서 add 전체가 진행된다. 

​						

`git commit -m '~~~'` : 추가적인 것이나 변경 된 부분만 저장이 되는 것이다. 

=> 위치가 중요하지 않다. add 했을 때 초록불이 들어올 것을 commit 하는 것이다. 



`git log` : 기록들을 볼 수 있다. 

- uu : 위로 

- dd : 아래로

- q 

- `HEAD` : 가장 많이 앞서 있다는 뜻이다. => 시간이 가장 뒤에 찍혀있다는 것 

  ​			변경 사항이 가장 많을 것이다. 



`git diff` : 마지막과 이전에 차이를 보여준다. 



`code .` : 그 자리에서 비쥬얼 스튜디오 코드를 열 수 있다. 



`git rm --cached 파일명` : git 에서 git commit 한 것을 없애준다. 



`vim 파일명`  (외울 필요는 없다. 혹시라도 만났을 때 당황하지말라규~)

- `i`  입력
-  ` :w` 저장
- `:q`  : 나가기 
  - `:q!` : 저장안하고 나가기 



**git commit 한 것들을 github 과 gitlab 에 백업하는 방법?**

`git remote add 뭐라고부를이름 주소`

- ex) `git remote add bb https://lab.ssafy.com/soo14906/learn_git.git`

- `git remote -v` 를 통해 잘 연결이 되어있는지 확인할 수 있다. 
- 지우는 방법 
  - `git remote rm 지은이름` 



`git push 지은이름 master`

- ex) `git push aa master && git push bb master`  => 두개의 일이 `&&` 을 통해서 동시에 일어날 수 있다. 
- `git push -u aa master` => -u 를 통해서 다음에 칠때는 그냥 `git push` 까지만 치면 된다. 



가져오기 (노트북 사용할 때?)

`git clone 연결할클론주소 (변경할폴더이름)` : 폴더 이름 설정안할거면 안해도된다. 

=> `.git` 이 같이 온다. / git 설정을 이어받아서 같이 시작한다. 



기본적인  루틴

끝날 때 해야될 일 push => 집에서 해야하는 일 pull => 컴터 끄기전 push => 싸피와서 할일 pull



둘이 동시에 commit 을 할 경우 먼저 push 못 하는 사람은 pull 을 해서 내용을 수정하거나 해야한다. 



## WEB



### web

인터넷에 연결된 컴퓨터들을 통해 사람들이 정보를 공유 => 정보공간 

### +

### service

1. 내가 달라고 하면 주는 것 (달라고 안하면 안 주는 것을 의미하기도 하다.)

2. 어떤 것을 처리해달라고 요구한다. 

   => 1번과 2번의 공통점은 내가 먼저 시작을 해야하는 것이다. 

   

    고객<요청>  =====> <응답> 해주는 사람

   ​	클라이언트<=======   서버

   

**web + service** == 서버 컴퓨터에서 요청과 응답을 처리할 프로그램을 개발한다. 



### 요청의 종류

1. 줘라 (Get)

- 웹에서 주고 받는 것의 종류가 대부분 HTML 이다.  (일반 사용자가 받는 것에서)
- 서버는 url==주문서 로 요청이 오니깐 그것을 받고 내보내는 것이 핵심이다. 
- 90% 가 get 이다. 



2. 받아라 (Post)

- 처리해달라고 데이터를 넘기고 받은 것을 어떻게서든지 처리를 하고 끝났을 때 OK 가 나가게 되는 것이다. 
- ex) 로그인, 회원가입



#### 누가  요청을 보내는가?

유저==사람 이 일반적으로 보낸다. 

**그러면 응답은?** => 자동화된 프로그램이 하게 된다. 그리고 이것을 하는 것이 우리이다. 



### 브라우저

브라우저가 파일 탐색기(file explorer)와 다를바가 없다.  => 내 컴퓨터를 넘어서 남의 컴퓨터에서도 사용할 수 있다. 

남의 컴퓨터를 지칭할 수 있다는 것이 핵심이다. 

file:// (내컴퓨터)

http:// google.com

​		google.com => 컴퓨터 주소



### 스태틱 웹 

브라우저 와 서버가 있는데 컴퓨터 주소를 안 상태에서 접속을 하면 .... 

이 파일을 어디에 있는지 요청을 정확하게 해야한다. 

서버는 파일을 그냥 들고만 있는 것이고 나는 정확하게 가서 그 파일을 들고 올 수 있다. 



<=>



### 다이나믹 웹 / 웹 어플리케이션 프로그램 (Web APP)



주소가 스태틱 웹과 달라진다. 



URL (Union Resourcr Locator) 파일식별자 

- 네트워크상에서 자원이 어디 있는지를 알려주기 위한 고유 규약이다. 
- url 은 흔히 웹사이트 주소로 알고 있지만, 웹사이트 주소 뿐만 아니라 컴퓨터 네트워크상의 자월을 모두 나타낼 수 있다. 





## HTML



기존의 텍스트 : 순차적으로 넘겨야지만 도달할 수 있었다. 



#### 하이퍼 텍스트 

링크들로 이루어 있는 것으로 변함 

http(Hyper Text Transfoer Po???)



웹 페이지를 위한 

최종적으로 내뱉는 것은 html 이기 때문에 배워야한다. => 역할 표시 언어이다. => html 로 작성된 문서파일이다. 



**웹 표준** 

W3C : 웹 표준을 정하는 곳  



`head` => 뇌 : 정보가 담겨있고 밖에 보이지 않는다. 

`body` 



"" 을 전부 사용한다. 



☆ 가장 중요한 제목은 h1 은 하나여야한다. html 을 작성할 때 역할을 생각해야한다. 





## 코드카데미 

https://www.codecademy.com/

=> 'Introduction to HTML'  pro 빼고 5개 해오기 / (예습 : css)



### 1. Learn HTML: Elements and Structure



```html
<h1>큰 제목</h1>

<body>
    <div>
        <p>본문 내용</p>
        </div> 
</body>
```



* `<div id=""> </div>`
  * text 나 다른 HTML 을 포함할 수 있다. (링크, 이미지, 비디오와 같은)
  * `id=""` : 구체적으로 속성을 부여 



* `<em> </em>` : 삐뚤게 써지기 

* `<strong> </strong>` : 글씨체 굵게 

  

* `<br><br>` : 엔터 같은거?



* list 항목  (● 형태)

```html
<ul>
  <li>Arctos</li>
  <li>Collarus</li>
</ul>
```
* list 항목 (넘버링)

```html
<ol>
	<li>Russia </li>
	<li>United States </li>
    <li>Canada</li>
</ol>
```

​	

*  삽입

  * 이미지 삽입 : `<img src="이미지url" />`
  * 동영상 삽입 

  ```html
  <video src="myVideo.mp4" width="320" height="240" controls>
    Video not supported
  </video>
  ```

  `src` : 



### 2. Learn HTML: Tables



```html
<table>
    <tr>
        <th>Company Name</th>
        <th>Number of Items to Ship</th>
        <th>Next Action</th>
    </tr>
</table>
```











