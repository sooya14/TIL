# Web 과목평가 | 190812

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



* W3C : 웹 표준을 정하는 곳  



## 01_HTML

- HTML이 무엇인가?
- 기본 구조
- 시멘틱 태그 (Semantic Tag)
- 자주 사용하는 태그들 (a, img, form 등)

---

### 01) HTML이 무엇인가?

* HTML == Hyper Text Markup Language



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
* 사진이라는 데이터에 대한 데이터 

`<body>` 

* 본문
* 브라우저 화면에 실제의 내용에 해당 



`<meta charset="UTF-8">`

- 이것을 안쓰면 한글이 깨지는 경우도 있을 수가 있다. 
- 쓰는게 무조건 옳다. 



`<title>`

- 문서의 제목 
- 브라우저 탭, 북마킹 할 때 사용되는 것 



태그 (Tag)

* `<h1></h1>` 
* `<img src="url"/> ` => 닫는 태그가 따로 없는 것도 있다. 

속성 (Attribute)

* `<a href="url"/>` 

  => `href` 가 속성명 / `"url"` 가 속성값



### 03) 시맨틱 태그

=> 의미를 가지는 태그들

* header,
* nav
* aside : 메인 콘텐츠와 관련성이 적은 콘텐츠에 사용
* section 
  * 문서의 일반적인 구분
  * h1~h6
*  article
* footer 
* div, span 등 은 시맨틱태그가 아니다. 



### Tag_index.html 

* `<strong></strong>` : 글씨 굵게 (과거: `<b></b>`)
* `<em></em>` : 글씨 기울어지게 (`<i></i>`)
* `<mark></mark>` : 형광펜
* `<del></del>` : 글씨 가운데에 밑줄
* `<ins></ins>` : 밑줄
* `<p></p>` 
* `<br>` : 다음 줄로 넘어가기 (엔터같은 )
* `<hr>` : 크게 가로줄 
* `<blockquote></blockquote>` : 인용문구
* `<li></li>` :  ●

* `<ol><li></li><ol>` : 넘버링 된다. 



//

`<div>` 

* 의미 없이 영역을 구분짓는 용도 => 레이아웃을 잡는 용도로 많이 사용하기 때문에 중첩이 특히 많다. 
* 블록속성

`<span>` 

* div 와 마찬가지 
* 인라인 속성

//



### 04) 자주 사용하는 태그들 (a, img, form 등)

* ` <a href="#" target="_blank">이곳</a>`
  
* href 에 URL 입력 / 없으면 #
  
* 이미지 삽입

  `<img width="500" alt="cat" src="./images/cat.jpeg">`

  * alt : 그림에 대한 설명 
  * src : url 또는 파일 위치 

* 동영상 삽입 

`<iframe width="560" height="315" src="URL"></iframe>`

* Table
  * th : table head => 표의 제목
  * tr : table row => 가로줄을 만드는 역할 
  * td : table data => 셀을 만드는 역할 
  * `rowspan="2"` : 위아래를 합친다. => 행 두개를 합친다. 
  * `colspan="2"` : 양옆을 합니다 => 열 두개를 합친다. 



% 04, 05, 05_subway %



## 02_CSS

https://poiemaweb.com/

* CSS는 무엇인가?

- 선택자 (Selector)
- 프로퍼티 값의 단위 (키워드, 크기 단위, 색깔 등)
- Box Model의 이해 (box-sizing, margin, border, padding 등)
- display 속성 (block, inline, inline-block, none)
- font 속성 (font-size, font-family 등)
- position (relative, absolute 등)

---

% css 는 모든 파일 복습 %

### 01) CSS는 무엇인가?

* CSS == Cascading Style Sheets

* html 의 각 요소의 style 을 정의하여 화면 등에 어떻게 렌더징 하면 되는지 브라우저에게 설명하기 위한 언어 => styling  (html: 정보의 구조화)
* html 없이 단독으로 존재하는 css 는 없다. (html은 css 를 포함할 수 있다. )



` <link rel="stylesheet" href="css/style.css">`

=> html 이랑 css 연결하는 방법 



### 02) 선택자 (Selector) ☆

![](C:\Users\user\AppData\Roaming\Typora\typora-user-images\1565412936034.png)

전체 `*` 

태그 셀렉터 : 그냥 태그 기입 

id 셀렉터 : `#` 

클래스 셀렉터 : `.`  (class  이름을 지을 때 띄어쓰기 기준은 _  이 아니라 - 로 짓는다. )



`div p` 

* div 안에 있는 모든 p 에게 적용 
* 어딘가에 또 들어있더라도 적용 ㅇㅇ

`div > p` 

* div 안에 있는 p 에게만 적용

   만약 div 안에 span 안에 p 가 있다면 적용 ㄴㄴ 



`p:first-child` / `p:last-child`

* 첫번째의 태그와 마지막 태그가 p 태그이면 적용된다. 
* 그리고 만약 그 안에 div 가 있으면 div 안에 p 가 있으면 이것도 적용된다. 

`p:fritst-child` / `p:last-of-tyrpe`

* p 태그 들 중에서 처음과 마지막 
* 만약 body 안에 따로 div 가 있으면 빼고 따로 각자 적용한다. 



후손요소 (하위요소) 에 프로퍼티 값이 지정 되면 부모셀렉터가 아닌 자신에게 부여된 값을 따른다. 



### 03) 프로퍼티 값의 단위 (키워드, 크기 단위, 색깔 등)

* 크기 단위

  * 절대값

    * px
    * rem :  html 의 기본 폰트 값 == 1rem

  * 상대값

    * em : 상속받은 폰트 값을 물려받아서 적용을 하는 것이고 

      ex) 2em => 부모의 폰트값 px * 2

    * % : 부모의 폰트 값에 적용 

      ​	ex) 120% => 부모의 폰트값 px * 1.2

      

* Viewport 

  *  디스플레이가 비율이 변화함에 따라서 달라진다. 

  * `vw` , `vh`  => 퍼센트 느낌 / 화면 전체가 100 이다. 

    ex) 100vh => 화면 높이 전체 



### 04) Box Model의 이해 (box-sizing, margin, border, padding 등) ☆

content : 컴퓨터 => 내용 

padding : 컴퓨터 밖의 책상 부분 => 컨텐트 밖 부분

border : 책상 모서리 

* border-radius : 모서리 둥글게 => px 로 조정

margin : 옆 책상과의 간격 



* content 가 반드시 있어야 한다. 그렇지 않으면 잡히지 않는다. 
* 가로에 아무것도 없지만 끝까지 선점하려고 한다. 



### 05) display 속성 (block, inline, inline-block, none) ☆

#### Block 

* 나란히 안되고 아래에  쓰여진다. 아무얘기 안했는데 엔터를 한 느낌 
* `div / h1 ~ h6, p, ol, ul, li, hr, table, form`

* ★특징

  1. 항상 새로운 line 에서 시작 
  2. 기본으로 width 100% (욕심쟁이~)
  3. width height margin padding 속성 지정 가능.
  4. block 요소 안에 inline 요소를 포함 가능 

  

#### Inline 

* 나란히 쓰여진다. 
* 폭개념이 없다. => margin, padding 이 없다. 
* `span, a, stong, em, del, img, br, input, select, textarea, button`
* ★특징
  1. 새로운 라인에서 시작하지 않으며, 문장 중간에서 쓸 수 있다. => 선의 영역이기 때문에 옆에 이어진다. 
  
  2. content 너비만큼 가로 폭을 차지한다. 
  
  3. width height margin padding 속성을 지정할 수 없다. 
     
     세로공간이 없다. 
     
     - 줄과 줄 사이의 너비 == 행간이 존재한다. => 행간으로 상하 여백을 지정한다. `line-height`
     
  4. inline 요소 뒤에 공백(\n , space)이 있으면, 자동으로 space (4px)가 들어간다. 
  
  5. liline 요소안에 block 요소 포함이 불가능한다. (망한다)



#### Inline-block

* `display: inline-block;`  => 블록을 인라인으로 만들어 준다. 
* 박스인데 욕심없는 박스이다. 
* 특징
  1. inline  의 한줄표시 + block 의 margin, padding, width, height 
  2. content 너비 만큼 가로폭
  3. display: inline-block 인 요소들 뒤에 공백은 space(4px)
  4. 상하 여백: margin 과 line height 로 가능



### 06) position (relative, absolute 등) ☆

https://poiemaweb.com/css3-position

absolute 

relative



### 07) font 속성 (font-size, font-family 등)



## 03_Bootstrap

- Bootstrap은 무엇인가?
- Spacing (m-\*, p-\*, mx-\*, my-\* 등)
- Colors (primary, secondary 등)
- 그리드 시스템 (Grid System)
- 사용 가능한 클래스
- 사용 가능한 컴포넌트 (Components) 

---

### 01) Bootstrap은 무엇인가?

* 반응형 웹 디자인을 위한 오픈 소스 프레임 워크 
* 디바이스에 따라 가로폭이나 배치를 변경하여 가독성을 높이도록
* `<meta name="viewport" content="width=device-width, initial-scale=1.0">`



### 02) Spacing (m-\*, p-\*, mx-\*, my-\* 등)

* m : 마진
* p : 패딩
* t, r, b, l
* x : 좌우 / y : 상하



### 03) Colors (primary, secondary 등)

* primary : 파랑
* secondary : 짙은 회색
* success : 초록색
* danger : 빨강
* warning : 노랑
* info : 청록색 (하늘색)
* light : 흰색같은데...
* dark : 검정
* white : 흰색 



### 04) 그리드 시스템 (Grid System)

* `col-12 col-sm-6 col-md-4 col-lg-3 col-xl-2`

* `<div class="row">` 안에 또 넣으면 그 안에서 12를 기준으로 나누어서 할 수 있다. 

* `offset-5` : 내 앞에 5자리 비워놔 

* extra small : <576px (.col-)


  small : ≥576px  (.col-sm-)


  medium : ≥768px (.col-md-)


  large : ≥992px (.col-lg-)


  extra large : ≥1200px (.col-xl-)



### 05) 사용 가능한 클래스

display

* `d-inline` : block 을 inline 처럼 display 된다. 
* `d-block` : inline 을 block 처럼 displaly 된다. => 다음 tag 가 옆에 오는 것이 아니라 블록처럼 아래칸에 위치한다. 
* `d-lg-none` : 특정 크기일때 보여지는 것 => 라지의 경계선일 때 없다가 그보다 작아지면 등장한다. 
* `d-none` : 라지일 때 등장하고 라지보다 작아지면 사라진다. 



Text

* `class=text-left` : text 클래스는 블록한테만 적용된다. 인라인은 안된다. 

  (인라인은 텍스트의 길이에 따라 범위가 있는데 움직일 수가 없겟지)

  

`<div class="container"></div>` : 모바일처럼 사용을 할 수 있다. 



### 06) 사용 가능한 컴포넌트 (Components) 


