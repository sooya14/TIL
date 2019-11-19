<template>
  <div id="app">
    <div id="nav">
      <router-link to="/">Home</router-link> |<!-- a 태그 대용 -->
      <router-link to="/login">Login</router-link>
    </div>
    

    <div class="container">
      <router-view/> <!-- router 를 여기다가 보내주세요용 (위치가 변경되면 화면구성도 달라진다. ) --> 

    </div>
  </div>
</template>

<style>
</style>
