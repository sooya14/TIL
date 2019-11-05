typeof true;  // boolean
typeof false;

// 없다. 확실히 없다. => 의도함
typeof null;  // object
// 아 몰랑 없어... => 의도하지 않음 
typeof undefined;  // undefined

typeof 'asdf';  // string
typeof 1;  // number | integer, floot 라는 개념이 따로 없다. 
typeof 1.1;  // number
typeof Infinity;  // number
typeof NaN;  // 숫자가 아니다. // number

typeof [1, 2];  // object
Array.isArray([1, 2]) // true 출력 | array 검증하는 방법 
typeof {a:1, b:2};  // object

typeof function () {};  // function

// method: 객체에 종속된 함수. 주어가 있어야 한다. 
// vs 함수: 
