# Web 과목평가 

* 셀렉터

* https://poiemaweb.com/ 에서 css 에서 보는게 가장 나으다

* 포지션 릴레이티브스 셀렉팅 

  



## 00_Web

### web

인터넷에 연결된 컴퓨터들을 통해 사람들이 정보를 공유 => 정보공간 

### +

### service

1. 내가 달라고 하면 주는 것 (달라고 안하면 안 주는 것을 의미하기도 하다.)

2. 어떤 것을 처리해달라고 요구한다. 

   => 1번과 2번의 공통점은 내가 먼저 시작을 해야하는 것이다. 

   

    	고객 클라이언트<요청 request> <=====> 해주는 사람  서버 <응답 response> 

   

**web + service** == 서버 컴퓨터에서 요청과 응답을 처리할 프로그램을 개발한다. 



* IP (Internet Protocol)  
  * 8비트 / 
  * ex) 172.217.27.78 :
* 도메인 (Domain)
  * 호스트 명
  *  ex) google.com
* URL (Uniform Resaurce Locator) 
  * 도메인 + 경로 / 실제로 해당 서버에 저장된 자료의 위치
  * ex) https://www.google.com/search?q=구글



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



#### 다이나믹 웹 / 웹 어플리케이션 프로그램 (Web APP)

주소가 스태틱 웹과 달라진다. 



URL (Union Resourcr Locator) 파일식별자 

- 네트워크상에서 자원이 어디 있는지를 알려주기 위한 고유 규약이다. 
- url 은 흔히 웹사이트 주소로 알고 있지만, 웹사이트 주소 뿐만 아니라 컴퓨터 네트워크상의 자월을 모두 나타낼 수 있다. 





## 01_HTML

- HTML이 무엇인가?
- 기본 구조
- 시멘틱 태그 (Semantic Tag)
- 자주 사용하는 태그들 (a, img, form 등)

---





### 01) HTML이 무엇인가?

* HTML == Hyper Text Markuo Language



* 하이퍼 텍스트 
  * (기존의 텍스트 : 순차적으로 넘겨야지만 도달할 수 있었다. )
  * 링크들로 이루어 있는 것으로 변함
  * http == Hyper Text Transfoer Protocol



* 웹 페이지를 위한 역할 표시 언어 
* 최종적으로 내뱉는 것은 html 이기 때문에 배워야한다. => 역할 표시 언어이다. => html 로 작성된 문서파일이다. 
* GET (받다) : HTML 로 작성된 문서파일은 단 하나이다. 



### 02) 기본 구조

`<!Doctype html>`

* Doctype 선언부 : 사용하는 문서의 종류를 선언하는 부분



html 의 요소는 `<head>` 와 `<body>` 로 구성된다. 

`<head>`

* 문서 제목, 문자코드(인코딩)와 같이 해당 문서 정보를 담고 있고, 브라우저에 나타나지 않는다. 

`<body>` 

* 브라우저 화면에 실제의 내용에 해당 



### 03) 시맨틱 태그



* header, nav, aside, section, article, footer => div, span 등 은 시맨틱태그가 아니다. 
* 











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



- `<div id=""> </div>`
  - text 나 다른 HTML 을 포함할 수 있다. (링크, 이미지, 비디오와 같은)
  - `id=""` : 구체적으로 속성을 부여 



- `<em> </em>` : 삐뚤게 써지기 

- `<strong> </strong>` : 글씨체 굵게 

  

- `<br><br>` : 엔터 같은거?



- list 항목  (● 형태)

```html
<ul>
  <li>Arctos</li>
  <li>Collarus</li>
</ul>
```

- list 항목 (넘버링)

```html
<ol>
	<li>Russia </li>
	<li>United States </li>
    <li>Canada</li>
</ol>
```

​	

- 삽입

  - 이미지 삽입 : `<img src="이미지url" />`
  - 동영상 삽입 

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







