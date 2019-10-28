const numbers = [1, 2, 3, 4];

numbers[0];  // 1 
numbers[-1];  // undefined : index 는 양의 정수만 가능하다. 
numbers.length;

// 원본 파괴 
numbers.reverse(); n // return 이 있다.

numbers.push('a');  // 스택 기준으로 맨 뒤에 들어간다. 

numbers.pop();

numbers.unshift('a');  // 맨앞에 추가된다. 

numbers.shift();  // 맨 앞에값이 삭제된다. 


// 원본 그대로인 methods
numbers.includes('a');  // false

numbers.indexOf(1);  // 0

numbers.join();  // "1, 2, 3"
numbers.join('');  // 123
numbers.join('-');  // 1-2-3
