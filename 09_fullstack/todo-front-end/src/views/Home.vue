<template>
  <div class="home">
    <h1>This is home!</h1>
    <TodoList />
  </div>
</template>

<script>
// @ is an alias to /src
// import HelloWorld from '@/components/HelloWorld.vue'

import router from '../router';
import TodoList from '../components/TodoList';

export default {
  name: 'home',
  components: {
    TodoList,
  },
  methods: {
    isLoggedIn () {
      this.$session.start();
      if (!this.$session.has('jwt')) {  // jwt 가 없으면 => Login 안했으면 
        router.push('/login');
      }
    }
  },

  created () {
    this.isLoggedIn()
  },
}
</script>
