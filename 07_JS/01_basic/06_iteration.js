// While 문 
let i = 0;
while (i < 10) {
    console.log(i);
    i++
}

// for 문 
let sum = 0

// for j in range(5):
for (let j=0; j < 5; j++) {
    sum += j;

}
console.log(sum);

// for k in range(1, 6):
for (let k=1; k < 6; k++) {}

// for num in [1, 2, 3, 4, 5]:
for (const number of [1, 2, 3, 4, 5]) {};  // in 이 들어갈 자리에 of 가 들어간다. 
// 왜 let 이 아니라 const 일까? => 재할당되는 코드가 원래 극소수이다. 안전하기 위해서 const 사용 => 그냥 습관처럼 const 사용하면된다. 