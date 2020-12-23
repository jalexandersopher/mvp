<template>
  <div id="login-form-container">
    <div class="login-form">
      <div>
        <div class="input">
          <label for="username">Username</label>
          <input type="text" id="login-username" v-model="username" />
        </div>
        <div class="input">
          <label for="password">Password</label>
          <input type="password" id="login-password" v-model="password" />
        </div>
        <div class="submit">
          <button @click="loginUser" id="login-submit">Submit</button>
        </div>
      </div>
    </div>
    <div>
      <p>
        {{ loginStatus }}
      </p>
    </div>
  </div>
</template>

<script>
import axios from "axios";
import cookies from "vue-cookies";

export default {
  name: "LoginComponent",
  data() {
    return {
      password: "",
      username: "",
      loginStatus: "",
    };
  },
  methods: {
    loginUser() {
      
      axios.request({
        url: "http://127.0.0.1:5000/api/login",
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        data: {
          "username": this.username,
          "password": this.password,
          "userId": this.userId,
        }
      })
        .then( (result) => {
          console.log(result)
          this.loginStatus = "Success!"
          cookies.set('loginToken', result.data.loginToken)
          cookies.set('userId', result.data.userId)
          this.$router.push("/adminpanel")
          })
        .catch( (error) => {
          console.log(error)
          this.loginStatus = "Error"
          })
    }
  }
};
</script>