// JavaScript Object Notation : JS 의 Object 처럼 표기하는 방법
// json 으로 표현된 데이터의 타입은 무조건 string 이다. 

const rawjson = 
    `{
        "name": "sooya", 
        "job": "student"
    }`

// me 에서 student 를 뽑을 수 있을까? => string 이니깐 불가능하다. => json 으로 넘어온 데이터를 그 언어로 바꿔줘야한다. 


// parsing : 구문 분석 
const parseData = JSON.parse(rawjson);  // 해석이라는 단계가 필요하다. 

// serializing : 공용어로 번역 (직렬화) (거꾸로 데이터를 상대방에게 보내줄 때,)
const backToJSON = JSON.stringify(parseData);  // 객체를 스트링으로 만들어준다. 