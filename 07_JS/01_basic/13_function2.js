// 1. 선언형
function a (x, y) {
    return x + y;
}

// 2. 할당형 
const b = function (x, y) {
    return x + y;
};  // = 이 있다면 마지막에 ; 

// 3. arrow function (할당형)
const b = (x, y) => {
    return x + y;
};  

// 3-1. 짧게: 함수 블록에 코드가 return 문 한 줄이라면! {} + return 같이 생략 가능 
const d = (x, y) => x + y;  

// 3-2. 짧게: 함수의 인자가 단 하나! 일때 () 생략 가능 
const e = x => {
    return x ** 2
}

// 3-3. 인자가 하나도 없으면?
const e = () => {  // 없으면 () 써야함
    return false
}

const f = _ => {  // 없으면 _ 쓰기로 함
    return false
}

// 3-4. 인자가 1개고, return 포함 한줄 일때, 
const square = x => x ** 2;