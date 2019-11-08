const likeButtons = document.querySelectorAll('.js-like-button');

likeButtons.forEach((likeButton) => {  // forEach: 버튼 하나하나를 돈다. 
    likeButton.addEventListener('click', function(event) {
        // 자바스크립트는 인자개수 안맞아도 돈다. 
        const URL = `/insta/${event.target.dataset.id}/like/`  // 최종적으로 보내야하는 URL
        axios.defaults.xsrfCookieName = 'csrftoken'  
        axios.defaults.xsrfHeaderName = 'X-CSRFToken'
        axios.get(URL)  // 이 순간 get 요청이 날라간다. 
            .then((res) => {
                console.log(res.data)
                if (res.data.liked) {  // 지금 좋아요가 끝난거면 
                    event.target.classList.remove('far');
                    event.target.classList.add('fas');
                }
                else {  // 지금 좋아요를 해제한다면 
                    event.target.classList.remove('fas');
                    event.target.classList.add('far');
                }
                console.log(event.target.classList)
            })  // res 의 data 까지 접근해야한다. 
            

    })

})  


