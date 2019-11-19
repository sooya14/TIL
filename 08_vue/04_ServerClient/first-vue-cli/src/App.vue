<template>

<!-- 반드시, Templates 안에는 단 1개 의 최상단 태그 -->
<div>
    <h1>나쁜말 ㄴㄴ </h1>
    <input type="text" v-model="input">
    <p>{{ filteredInput }}</p>

</div>
</template>

<script>
/* eslint-disable no-console */
export default {
    name:'App',
    data: function () {
        return {
            input: 'Type something'
        }
    },

    methods: {},
    computed: {
        filteredInput: function() {
            // [바보] 가 들어오면, ** 로 바꿔서 return 하도록 한다. 
            
            // return this.input.replace(/바보/gi, '**');  // g: 글로벌하게 다 찾아라 | i: 대소문자 구분하지 않는다. 
            return this.input.replace(/바보|멍청이|똥개/g, '**');
        }
    }
}
</script>

<style>

</style>