// auth.js 인증관련 모든 State 를 작성. 
// State 에 접근/변경 하는 모든 로직은 여기로. 

const state = {
    token: null, // 시작할 떄 값은 로그인을 안하니깐 null 
};


// Vuex 에서는 Arrow Fuction 을 사용한다. 
const getters = {  // state 를 가져오려고 
    // isLoggedIn: (state) => {
        // if (state.token === null) {
        //     return false;
        // } else {
        //     return true;  // token 이 없으면 로그인하지 않은 것이다..... 
        // }
        isLoggedIn: state => !!state.token,   // 특정 값을 true/false 로 바꾸는 구문 
};


const mutations = {
    setToken: (state, token) => state.token = token,
    
};

const actions = {
    // logout: (options) => {
    //     // mutations.serToken(state, null) === 절대로 이렇게 쓰면 안된다. 
    //     options.commit('setToken', null) // GREAT 
    // }
    logout: ({ commit }) => {
        commit('setToken', null)
    },  // 위에 코드와 동일

    login: ({ commit }, token) => {
        commit('setToken', token)
    },  
    
};

export default {
    state, getters, mutations, actions
}