/* Python
    def adder_1(x, y):
    return x + y
 */

 function adder1(x, y) {  // 선언식 : ; 없음
     return x + y;
 }

 /* Python 에서는 안됨!
    adder2 = (x, y): return x + y
  */

const adder2 = function (x, y) {  // 할당식 : ; 있음 (위랑 아래랑 같은 코드)
    return x + y;
};


/* python Lamda 표현식
    adder3 = lamda x, y: x + y
*/

// ES6 Arrow function 
// 1. function 을 지운다. 
// 2. () 와 {} 사이에 => 넣는다. 

// const adder3 = function (x, y) { return x + y; };

const adder3 = (x, y) => { 
    return x + y; 
};



