// JS : Non - Blocking

// function sleep_3s() {
//     setTimeout(() => {console.log('wake up!')}, 3000);  // 3초
// }

// console.log('start sleeping');
// sleep_3s()
// console.log('end of program');  // 기다려주지 않고 흘려보내버린다.
// end of program 가 wake up 보다 먼저 등장


// 그럼 어떤 함수/작업들이 Non blocking 한가여?
/*
    지금 당장 해결할 수 없고 
    결과도 확신할 수 없는 모든 일 
*/

function complexTask() {
    console.log('시작');
    for (let i=0; i < 1000000000; i++) {}
        console.log('오래걸림')
    
}

setTimeout(() => {console.log('짱빨리끝남!')}, 1)  // 시작이 먼저 나옴 => 
complexTask()

// node === 환경 === python 