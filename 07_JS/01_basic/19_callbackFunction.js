function a(x, y) {
    return x + y;
}

function b(n) {
    return n++;  //  return 하고나서 n += 1
    // return ++n;  // n += 1 하고 return  한다. 
}

function c(f1, f2) {
    return f1(10,10) + f2(99);
}

console.log(
    c(a, b)  // 119 출력
    c(b, a)  // NaN 출력 => a 함수에서 y 자리에 undifided 가 들어가서 더했을 때 NaN 가 나온다. 
)  


