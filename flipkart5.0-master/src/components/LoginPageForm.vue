<template>
  <div class="helloworld-login">
    <div class="login-form-container2">
      <img
        src="https://assets.ccbp.in/frontend/react-js/nxt-trendz-login-img.png"
        className="login-image2"
        alt="website login"
      />
      <form @submit.prevent="login" class="form-container2">
        <div class="input-container2">
          <label className="input-label2" htmlFor="username"> USERNAME </label>
          <input
            v-model="username"
            type="text"
            placeholder="Username"
            class="username-input-field2"
            required
          />
        </div>
        <div class="input-container2">
          <label className="input-label2" htmlFor="password"> PASSWORD </label>
          <input
            v-model="password"
            type="password"
            class="password-input-field2"
            placeholder="Password"
            required
          />
        </div>
        <button type="submit" class="btn btn-primary w-100 mt-4" @click="login">
          Login
        </button>
        <router-link to="/signup" class="mt-1 linkop mr-3 btn btn-outline-primary mt-3 w-100">
          Sign Up
        </router-link>
        <p v-if="flash_message" class="mt-3">{{ flash_message }}</p>
      </form>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
//import Cookies from 'js-Cookie'
export default {
  name: 'login-botPage',
  data() {
    return {
      username: '',
      password: '',
      flash_message:''
    }
  },
  methods: {
    async login() {
      //api call for sending details signinup storing username password role in the db
      const data = {
        username: this.username,
        password: this.password,
      }
      axios
        .post('http://localhost:2000/logger', data)
        .then(response => {
          console.log(response)
          if (response.request.status == 200) {
            this.flash_message = response.data.message
            this.$router.push("/home")
          } else {
            this.flash_message = response.data.message
          }
        })
        .catch(error => {
          console.error('Login failed:', error)
        })
    },
  },
}
</script>

<style>
.login-form-container2 {
  display: flex;
  flex-direction: row;
  justify-content: space-between;
  align-items: center;
  height: 100%;
  width: 100%;
  max-width: 1110px;
  margin: auto;
}
.helloworld-login {
  display: flex;
  justify-content: center;
  align-items: center;
  min-height: 100vh;
}
.login-image2 {
  width: 60%;
  max-width: 524px;
  flex-shrink: 1;
  margin-right: 20px;
}
.form-container2 {
  background-color: wheat;
  display: flex;
  flex-direction: column;
  justify-content: flex-start;
  align-items: center;
  padding: 20px;
  border-radius: 8px;
  width: 100%;
  max-width: 350px;
}
.input-container2 {
  display: flex;
  flex-direction: column;
  margin-top: 20px;
  width: 100%;
}

.input-label2 {
  margin-bottom: 0px;
  font-size: 14px;
  line-height: 16px;
  color: #475569;
}

.username-input-field2 {
  font-size: 16px;
  height: 40px;
  width: 100%;
  border: 1px solid #d7dfe9;
  background-color: #e2e8f0;
  color: #64748b;
  border-radius: 2px;
  margin-top: 5px;
  padding: 8px 16px 8px 16px;
  outline: none;
}

.password-input-field2 {
  font-size: 16px;
  height: 40px;
  width: 100%;
  border: 1px solid #d7dfe9;
  background-color: #e2e8f0;
  color: #64748b;
  border-radius: 2px;
  margin-top: 5px;
  padding: 8px 16px 8px 16px;
  outline: none;
}

.login-button2 {
  font-size: 14px;
  color: #ffffff;
  height: 40px;
  width: 90%;
  margin-top: 20px;
  margin-bottom: 2px;
  margin-left: 10px;
  margin-right: 40px;
  background-color: #0b69ff;
  border-radius: 8px;
  border: none;
  outline: none;
  cursor: pointer;
}
</style>
