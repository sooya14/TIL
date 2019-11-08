import Vue from 'vue';
import App from './App.vue'; // .vue 는 안써도 알아서 동작함

new Vue({
    // el: '#app',
    // Method(함수 in 객체) 정의할 떄 , () => {} 금지이지만, 여기서만 쓴다.  
    render: h => h(App),
}).$mount('#app')  // 이거 쓰면 el 없어도 된다. 