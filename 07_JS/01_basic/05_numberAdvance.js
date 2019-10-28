//typeof 는 함수가 아니라 단항 연산자이다!
// typeof 1 해도 "number" 라고 뜨긴하다. 

typeof(1)  // number
typeof(Infinity)  // Infinity
typeof(NaN) // Not A Number : number

// number 연산이 이상할 경우 
// 에러가 아니라 NaN 이라는 값을 return

Infinity - Infinity // NaN
'asdf' + 1 // 덧셈이 아니라 string contact: 'asdf1
'asdf' - 1 // NaN
'asdf' * 1 // NaN

