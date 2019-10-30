// map 등등 많은 함수들이 인자로 함수를 요구한다. 

// ES5
var colors = ['red', 'blue', 'green'];

for (var i=0; i < colors.length; i++) {
    console.log(colors[i]);
}

// ES6+ forEach 가 끝나고 아무것도 return 을 하지 않는다. 
colors.forEach(function (x) {  // forEach: 하나만 꺼내기만 한다. 
    console.log(x)
})

// ES5
const numbers = [1, 2, 3];
const double_numbers = [];

for (let i=0; i < numbers.length; i++) {
    double_numbers.push(numbers[i] * 2);
}
console.log(double_numbers)

// ES6+
/*
    map(lambda number: number*2, numbers)    
*/

const triplNumbers = numbers.map((number) => {
    return number * 3;
})
console.log(triplNumbers)


// ES5
const products = [
    {name: 'apple', type: 'fruit'},
    {name: 'carrot', type: 'vegetable'},
    {name: 'tomato', type: 'fruit'},
    {name: 'cucumber', type: 'vegetable'},
];

const fruits = []
for (const product of products) {
    if (product.type === 'fruit') {
        fruits.push(product);
    }
}
console.log(fruits);

// ES6+
const vegetables = products.filter((product) => {
    return product.type === 'vegetable';
})
console.log(vegetables)