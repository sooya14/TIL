<template>
    <div>
        <!--() 는 커스텀 인자 없으면 안붙임-->
        <!-- v-on: 을 줄여서 @ -->
        <!-- <input @input="onInput" type="text">   -->
        <input @keypress.enter="onInput" type="text">  

    </div>
</template>

<script>
export default {
    name: 'SearchBar',  // new component: 0. 이름적기
    methods: {
        onInput (e) {
            // console.log(e.target.value)  // input 창에 들어가있는 값
            // this.$emit('Event이름', 전송할 값) : 위에 인풋에 값이 바뀔때마다 계속 발생시키겠다. => 자식component 에서 부모component 에게 정보(데이터)를 올려보낼 때
            this.$emit('inputChange', e.target.value);  // e.target.value => input 안에서 바뀐 값
        }
    }, 
    
}
</script>


<style scoped>  
/* scoped: 해당 컴포넌트의 태그들만 영향을 받는다! */
    input{
        width: 75%;
    }

    div{
        text-align: center;
        margin: 20px;
    }
</style>