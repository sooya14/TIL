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
    books, conmics, magazine,
};