<template>
    <div class="login-form">
        <div v-if="isLoading" class="spinner-border" role="status">
            <span class="sr-only">Loading</span>
        </div>

        <div v-else class="login-input">
            <div v-if="errors.length" class="error-list alert alert-danger">
                <h4>아래의 오류를 해결해 주세요.</h4>
                <ul>
                    <li v-for="(error, idx) in errors" :key="idx">{{ error }}</li>
                </ul>
        </div>

            <div class="form-group">
                <label for="username">ID</label>
                <input @keyup.enter="login" v-model="credentials.username" type="text" class="form-control" id="username"
                    placeholder="아이디를 입력해주세요">
            </div>
            <div class="form-group">
                <label for="password">Password</label>
                <input @keyup.enter="login" v-model="credentials.password" type="password" class="form-control" id="password"
                    placeholder="비밀번호를 입력해주세요">
            </div>
            <button @click="login" class="btn btn-primary">로그인</button>
        </div>
    </div>
</template>

<script>
    import router from '../router';  // '../router/index.js' (자동으로 index.js 를 찾는다.)

    const axios = require('axios');
    export default {
        name: 'LoginForm',
        data() {
            return {
                credentials: { // id/password 에 해당하는 data
                    username: '',
                    password: '',
                }, 
                isAuthenticated: false, // 인증 여부
                isLoading: false,
                errors: [],
            }
        },
        methods: {
            login() {
                this.isLoading = true;
                if (this.checkUserInput()) {
                    console.log('django 서버로 데이터를 보냅니다. ')
                    axios.post('http://localhost:8000/api-token-auth/', this.credentials)  // 로그인 정보 입력하면 credentials 에 담긴다. 
                        .then(res => {
                            this.isLoading = false;
                            
                            // VueSession 설치 후,
                            this.$session.start();  // sessionStorage.session-id: sess + Date.now()
                            this.$session.set('jwt', res.data.token);  // 인증 한 것을 token 으로 저장하는 것이 로그인이다. 저장하는 순간부터 로그인이 된것이다. 

                            router.push('/');  // Django 에서의 return redirect('/') 랑 똑같다. 
                         
                        })
                        .catch(err => {
                            if (!err.response) {
                                this.errors.push('Network error')
                            } else if (err.response.status === 400) {
                                this.errors.push('Invalid username or password');
                            } else if (err.response.status === 500) {
                                this.errors.push('Internal Server error. Please try again');
                            } else {
                                this.errors.push('Some error occured');
                            }
                            this.isLoading = false;
                        });
                }   
                else {
                    this.isLoading = false;
                }
            },

            checkUserInput() {
                this.errors = [];
                if (!this.credentials.username) this.errors.push("username 을 입력하세요.");
                if (this.credentials.password.length < 8) this.errors.push("password 는 8 글자 이상입니다.");
                if (!this.errors.length) return true;  // 비어있다면 true 이다. 
                
            },
        },
    }
</script>

<style>

</style>