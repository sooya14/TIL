function init() {  // 모든 로직을 여기에 때려 박는다 ㅇㅅㅇ 
    
    const button = document.querySelector('#js-todo-button');
    const inputTag = document.querySelector('#js-todo-input');
    const reverseBtn = document.querySelector('#js-reverse-btn');

    reverseBtn.addEventListener('click', () => {
        const todoArea = document.querySelector('#js-todo-area');
        const todos = Array.from(document.querySelectorAll('.js-card')); // reverse 는 배열한테만 작용하기 때문에 배열로 만들어준다

        while (todoArea.firstChild) { // 공간에 뭐가 있다면 
            todoArea.removeChild(todoArea.firstChild); // 지우겠다. 
        }
        todos.reverse().forEach((todo) => {
            todoArea.appendChild(todo);
        })

    });


    button.addEventListener('click', () => {
        const inputArea = document.querySelector('#js-todo-input');
        createToCard(inputArea.value);
        inputArea.value = null; // 카드가 생성되고 나면 비우기

    })

    inputTag.addEventListener('keydown', (e) => {
        if (e.which === 13) {
            const inputArea = document.querySelector('#js-todo-input');
            createToCard(inputArea.value);
            inputArea.value = null; // 카드가 생성되고 나면 비우기
        }

    })

    // Card 만들기
    const createToCard = (content, completed = false) => { // completed=flase: 아무말도 안들어오면 false 가 기본값, 뭐라도 들어오면 그 값을 갖게 된다.  
        const cardArea = document.querySelector('#js-todo-area');

        const todo = document.createElement('div'); // createElement: 태크를 만들 수 있다. 
        todo.className = 'ui segment js-card';

        const wrapper = document.createElement('div');
        wrapper.className = 'ui checkbox';

        const checkbox = document.createElement('input');
        checkbox.type = 'checkbox'; // ??

        checkbox.addEventListener('click', () => {

            // 새로고침 이후에도 이벤트 리스너가 달리는지?

            if (checkbox.checked) {
                todo.classList.add('secondary');
                label.classList.add('done'); // label 이 정의되지 않은 상황이지만 실행이 된다. 
            } else {
                todo.classList.remove('secondary');
                label.classList.remove('done');
            }

        })

        const label = document.createElement('label');
        label.innerHTML = content;

        // 할일 삭제하기 코드 
        const deleteIcon = document.createElement('i');
        deleteIcon.className = 'icon close custom-icon';

        deleteIcon.addEventListener('click', () => {
            cardArea.removeChild(todo); // 하나의 todo 만을 말하고 있다. 
        })

        wrapper.appendChild(checkbox);
        wrapper.appendChild(label);
        todo.appendChild(wrapper);
        todo.appendChild(deleteIcon);
        cardArea.appendChild(todo);
    }

}

init();