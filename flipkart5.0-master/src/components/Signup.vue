<template>
  <div class="main-bg-container">
    <form class="registration-form" @submit.prevent="registerUser">
      <div class="form-background">
        <h2 class="text-center text-white">Lets Join Hands</h2>
        <p class="text-center text-white">
          Become a member and enjoy a lot of amazing features through this
          platform
        </p>
        <div class="form-row">
          <div class="form-group">
            <label for="fullName" class="input-label">Full Name</label>
            <input
              v-model="fullName"
              type="text"
              class="username-input-field"
              id="fullName"
              required
            />
          </div>
          <div class="form-group">
            <label for="username" class="input-label">Username</label>
            <input
              v-model="username"
              type="text"
              class="username-input-field"
              id="username"
              required
            />
          </div>
        </div>
        <div class="form-row">
          <div class="form-group">
            <label for="password" class="input-label">Password</label>
            <input
              v-model="password"
              type="password"
              class="username-input-field"
              id="password"
              required
            />
          </div>
          <div class="form-group">
            <label for="confirmPassword" class="input-label"
              >Confirm Password</label
            >
            <input
              v-model="cpassword"
              type="password"
              class="username-input-field"
              id="confirmPassword"
              required
            />
          </div>
        </div>
        <div class="form-row">
          <div class="form-group">
            <label for="age" class="input-label">Age</label>
            <input
              v-model="age"
              type="number"
              class="username-input-field"
              id="age"
              required
            />
          </div>
          <div class="form-group">
            <label for="email" class="input-label">Email</label>
            <input
              v-model="email"
              type="email"
              class="username-input-field"
              id="email"
              required
            />
          </div>
        </div>
        <div class="form-group">
          <label class="input-label">Gender</label>
          <div class="gender-options">
            <div class="form-check form-check-inline">
              <input
                v-model="gender"
                class="form-check-input"
                type="radio"
                id="genderMale"
                value="male"
                required
              />
              <label class="form-check-label input-label" for="genderMale"
                >Male</label
              >
            </div>
            <div class="form-check form-check-inline">
              <input
                v-model="gender"
                class="form-check-input"
                type="radio"
                id="genderFemale"
                value="female"
                required
              />
              <label class="form-check-label input-label" for="genderFemale"
                >Female</label
              >
            </div>
            <div class="form-check form-check-inline">
              <input
                v-model="gender"
                class="form-check-input"
                type="radio"
                id="genderOther"
                value="other"
                required
              />
              <label class="form-check-label input-label" for="genderOther"
                >Other</label
              >
            </div>
          </div>
        </div>
        <div class="mt-3 button-container">
          <button type="submit" class="btn btn-primary">Register</button>
          <p class="ml-3 mt-3 paraop text-dark">Already have an Account?</p>
          <router-link to="/" class="mt-1 linkop mr-3 btn btn-primary">
          Login
        </router-link>
        </div>
      </div>
    </form>
  </div>
</template>

<script>
import axios from 'axios'
//import Cookies from 'js-Cookie'
export default {
  name: 'chat-bot-page',
  data() {
    return {
      fullName: '',
      username: '',
      cpassword: '',
      password: '',
      gender: 'male',
      age: '',
      email: '',
    }
  },
  methods: {
    async registerUser() {
      //api call for sending details signinup storing username password role in the db
      if (this.password !== this.cpassword) {
        return (this.flash_message = 'Passwords do not match')
      } else {
        const data = {
          fullName: this.fullName,
          username: this.username,
          password: this.password,
          gender: this.gender,
          age: this.age,
          email: this.email,
        }
        axios
          .post('http://localhost:2000/signup', data)
          .then(response => {
            console.log(response)
            if (response.request.status == 200) {
              this.flash_message = response.data.flash_message
            } else {
              // const token = response.data.token
              //Cookies.set('jwt_token', token, {expires: 1})
            }
          })
          .catch(error => {
            console.error('Login failed:', error)
          })
      }
    },
  },
}
</script>

<style>
.main-bg-container {
  background-color: rgb(53, 55, 62);
  display: flex;
  justify-content: center;
  align-items: center;
  min-height: 100vh;
}
.form-background {
  background-color: rgb(53, 134, 110);
  padding: 20px;
  border-radius: 6px;
  box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.1);
}

.text-center {
  text-align: center;
}
.linkop {
  color: black;
  font-weight: 500;
  font-size: 15px;
  margin-left: 10px;
}
.paraop {
  color: black;
  font-weight: 500;
  font-size: 15px;
  margin-left: 10px;
}
.input-label {
  font-weight: 500;
  font-size: 15px;
  color: black;
}
.button-container {
  display: flex;
  justify-content: flex-start;
  align-items: center;
}

.username-input-field {
  font-size: 14px;
  height: 40px;
  border: 1px solid #d7dfe9;
  background-color: white;
  color: #64748b;
  border-radius: 4px;
  margin-top: 5px;
  padding: 8px 16px;
  width: 100%;
  outline: none;
  transition: border-color 0.2s, box-shadow 0.2s;
}

.form-row {
  display: flex;
  gap: 20px;
  margin-bottom: 20px;
}

.form-group {
  flex: 1;
}

.gender-options {
  display: flex;
  gap: 10px;
}

.btn-primary {
  width: 20%;
  height: 40px;
  padding: 10px;
  background-color: rgb(76, 179, 137);
  border: none;
}
</style>
