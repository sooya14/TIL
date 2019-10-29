// 1. input 태그 안의 값 (value)을 잡는다. 
// const input = document.querySelector('#js-userinput').value;  // # === id  . === class 


// 2. button 태그에는 'click' 이 일어낰ㅆ을 때, input 에서 ENTER 키를 쳤을 때, 1에서 잡은 값을 요청으로 보낸다. 
// [무엇].addEventListener([언제], [어떻게: function]) 
const button = document.querySelector('#js-go');
const inputArea = document.querySelector('#js-userinput');

const resultArea = document.querySelector('#js-result-area');

const API_KEY = 'KUvKhKjr7ml3PzUyXn7HbJUjCSNiqZfP';
const testWord = 'food';
const url = `https://api.giphy.com/v1/gifs/search?api_key=${ API_KEY }&q=${testWord}&limit=25&offset=0&rating=G&lang=ko`;
// console.log(url)  => 잘 나오는지 확인용

// const whenClicked = function () {
//     console.log('되었다!');
// }

// const whenPressed = function (event) {
//     console.log('꾸욱');
//     console.log(event);
// }

// button.addEventListener('click', function () {
//     const inputValue = inputArea.value
//     console.log(inputValue);
// });

button.addEventListener('click', () => {
    const inputValue = inputArea.value;
    // console.log(inputValue);
    searchAndPush(inputValue);

});


inputArea.addEventListener('keypress', (event) => {
    // console.log('꾸욱');
    // console.log(event.key, event.which);

    if (event.which === 13) {
        const inputValue = inputArea.value
        // console.log(inputValue);

        // inputValue 로 Giphy API 에 요청 보내서 받기.
        searchAndPush(inputValue);
    }
    // const inputValue = inputArea.value  // 칠때마다 일어난다. 
    // console.log(inputValue)
});  // key 가 눌렸을 때, 


// 3. Giphy API 에서 넘겨준 Data 를 index.html 에서 보여준다. 
const searchAndPush = (keyword) => {
    
    const imageCount = document.querySelector('#js-image-count').value;  // 꺼내면 string
    const API_KEY = 'KUvKhKjr7ml3PzUyXn7HbJUjCSNiqZfP';
    const url = `https://api.giphy.com/v1/gifs/search?api_key=${ API_KEY }&q=${keyword}&limit=${imageCount}&offset=0&rating=G&lang=ko`;

    
    const AJAX = new XMLHttpRequest();  // 요청 준비
    AJAX.open('GET', url);  // 요청 세팅
    AJAX.send();  // 요청 보내기 
    AJAX.addEventListener('load', function (answer) {
        const res = answer.target.response;
        const giphyData = JSON.parse(res);
        const dataSet = giphyData.data;

        inputArea.innerHTML = null;  // 검색창 비우기 
        resultArea.innerHTML = null; // 새로 검색하면 이전꺼 비우기
        for (const data of dataSet) {
            pushToDom(data.images.fixed_height.url);
        }
        
    });

    const pushToDom = (imageUrl) => {
        const imageTag = document.createElement('img');
        imageTag.src = imageUrl;
        imageTag.alt = 'giphy-image';
        imageTag.classList.add('container-image');

        resultArea.appendChild(imageTag);

        // resultArea.innerHTML +=`<img src="${imageUrl}" class="container-image"/>`;  => 직접 친 경우 / 위의 경우가 더 바람직 

    }
}



function sendAjaxReq () {
    // console.log('시작');
    const AJAX = new XMLHttpRequest();  // 요청 준비
    AJAX.open('GET', url);  // 요청 세팅

    // console.log('보낸드앗');
    AJAX.send();  // 요청 보내기 

    AJAX.addEventListener('load', function (answer) {
        // console.log(answer);
        // console.log(answer.target);
        const res = answer.target.response;
        const giphyData = JSON.parse(res);
        console.log(giphyData);
    });
    // console.log('끝');

    // const res = AJAX.res;
    // console.log('응답: ' + res)
    // const giphyData = JSON.parse(reponse);
    // console.log(giphyData);

};