
/*
    key - value 에 같은 단어를 쓸 때 축약할 수 있다. 
 */
 // ES5
// var => const/let
var books = ['Learning JS', 'Eloquent JS'];
var comics = {
    dc: ['Joker', 'Batman'],
    marvel: ['Avengers', 'spiderman'],
};

var magazine  = {};

var bookshop = {
    books: books,
    comics: conmics, 
    magazine: magazine,
}

// ES6+
const books = ['Learning JS', 'Eloquent JS'];
const comics = {
    dc: ['Joker', 'Batman'],
    marvel: ['Avengers', 'spiderman'],
};

const magazine  = {};

const bookshop = {
    books, // books: books, 를 줄여서 한번만 작성 가능하다.
    conmics, 
    magazine,
};

// Method(객체 안의 함수)
// 절대 arrow function () => {} 쓰지 말자. 
const me = {
    name: 'sooya',
    // 메서드 정의.
    greet: function () {
        console.log(this)
        return `Hello, I'm ${this.name}`  // this 는 self 에 대응하는 느낌 
    },
    walk: () => {
        console.log(this)  // arrow function 에서 this 가 위의 this 가 아나리 한단계 위로 가버린다. 
        return `${this.name} is walking...`
    }
};
// method : function
// this => me
