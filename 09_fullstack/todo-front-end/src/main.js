import Vue from 'vue'
import App from './App.vue'

import router from './router'  // from './router/index.js'  
// 무엇을 불러오는 것이 아니라 여기에 담아주세요 이기 때문에 import r 이라고 해도 무방하다. => 아래 코드에도 router 대신 r 로 담고 
import store from './store'  // from './store/index.js'

// $ npm i vue-session => token 을 저장하게 해준다. | 서버를 끄고 설치하기 (혹시 모르니깐)
import VueSession from 'vue-session'  // 발급받은 Token 을 SessionStorage 에 저장하는 것을 도와줌 




Vue.config.productionTip = false;
Vue.use(VueSession); // Vue 에게 VueSession 이라는 Middleware 등록

new Vue({
  // router: router 키랑 밸류값이 같으면 그냥 하나로 간단히 적는다. 
  router,  // router/index.js 에서 악수하고, 본격적으로 일을 시작. 
  store,  // store/index.js 에서 악수, 일은 여기서 시작  
  render: h => h(App)
}).$mount('#app')

