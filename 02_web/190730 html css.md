# Web 02 |190730



## HTML



Open graph (og)

* 컨텐트 안에 들어있는 사진 
* 메타 정보들을 조합해서 다른 어플리케이션에서 사용할 수 있다. 
* 



W3C vs WTG 

*  최근의 흐름이 넘어갔다. 





### 00_basic.html  

* 공백 4 를 2로 변경



요소 : doctype 아래부터는 모든것이 다 요소이다. 

    <h1>Hi</h1>  {'tagname': 'hi', 'content': 'Hi'}



<img src="" alt=""/> 

src, alt => 속성



### semantic tag

의미만 가지고 있다. 다른 기능은 없다. 

* `<div><div/>`  (division)
  * 문서 안에서 구역을 의미한다. 물리적인 구역  => 공간을 분할해 준다.

* `<header>  `등 의미를 갖는 역할이 있는 태그이다.  
  * `<div>` 와 다른 기능 차이는 없다. 그러나 
  * SEO 영역(검색엔진 최적화)에 영향을 주기 때문에 사용하는 것이 맞다. 
  * 

* `<html lang="ko"> `  : 이 html 은 주로 한국어로 쓰여져 있다는 의미



이미지 가져오기 

alt 값이 필수

다른 곳에 있는 파일 

보여지는 크기만 줄어드는 것일 뿐이다. 이미지 사이즈를 줄인다고 해서 용량이 작아지는 것이 아니다. 용량은 여전히 크다. => 로딩이 오래걸려서 유저들이 사용하기 힘들다. 



인라인 : 이미지는 인라인 으로써 ,  문장안에 녹아들어간다. 한줄로 나오면 

블록 : 아무얘기 안햇는데 엔터느낌



### table

* 블록이다. 인라인이 아니라

가로 row

html 속성에서 속성값을 여러개 줄 때 콤마, 가 아니라 띄어쓰기를 통해 구분을 한다. 



### form

`<form action="#"> ` 



`<input type="radio" value="Python"checked>Python<br>`

 value 값을 설정해야 나중에 우리가 그 값을 받아 볼 수 있다. 



value 값이 우리가 받을 수 있는 데이터 이다. 그밖의 시간은 그냥 보여지는 것 일 뿐



## CSS



html : 정보의 구조화 

css : 스타일링



`h1{color: blue;}`

셀렉터

프로퍼티



픽셀이 높을 수록 고해상도이다. 



**우선순위**

* seletor spcificity 가 노픈 것이 우선순위이다. 

* 셀렉팅을 어떻게 하느냐에 따라 많이 달라지기 때문에 이것이 어렵다.... 

* 우선순위 순서 : !important > inline css > [id > class] > tag > browser 기본 세팅 

  * !important => 프로들이 사용하지만 우리 수준에서는 사용하지 않는다. 

  * id 도 사용하지 않을 것이다. (자바 스크립트 할 때 사용할 것이다.)

    => **모든 것은 class 로 진행할 것이다. !!!! **

  * id 와 class 는 셀렉터를 위한 존재



* class 이름 짓는 방법 

  띄어쓰기 기준은 _ 가 아니라 - 로 구분한다. 














