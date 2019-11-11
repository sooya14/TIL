import Vue from 'vue';
import App from './App';  // App.vue 를 알아서 확장자 버리고 읽는다. 

// new Vue({
//     el: '#app', // 마운트될 대상을 선언 
//     render: (h) => h(App),  // 유일하게 method 인데 Arrow Funtion | app 에서만 render 사용 | arrow function 사용가능하다.         
// })

new Vue({
    render: (h) => h(App),  
}).$mount('#app')  // 마운트될 대상을 선언 | 위와 똑같은 코드 | 일반적으로 이 코드를 사용한다. 