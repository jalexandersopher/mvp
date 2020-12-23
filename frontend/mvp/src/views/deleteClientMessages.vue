<template>
    <div>
        <header-component></header-component>
        <div class="input">
          <label for="title">Client Email</label>
          <input type="text" id="title" v-model="email" />
        </div>
        <div class="submit">
          <button @click="deleteProduct" >Submit</button>
        </div>
        <div>
            <p>
                {{ deleteContentStatus }}
            </p>
        </div>
    </div>
</template>

<script>
import axios from "axios"
import cookies from "vue-cookies";
import HeaderComponent from "../components/headerComponent.vue";

    export default {
        name: "DeleteClientMessages",
        components: {
            HeaderComponent
        },
        data() {
            return {
                email: "",
                deleteContentStatus: "Waiting to List",
            }
        },
        methods: {
            deleteProduct: function() {
                this. deleteContentStatus = "Deleting!"
                axios.request({
                    url: "http://localhost:5000/api/contact",
                    headers: {
                        "Content-Type": "application/json",
                    },
                    method: "DELETE",
                    data: {
                        "loginToken": cookies.get("loginToken"),
                        "email": this.email
                    }
                }).then((response) => {
                    console.log(response)
                    this.deleteContentStatus = "Message Deleted Successfully!"
                }).catch((error) => {
                    console.log(error)
                    this.deleteContentStatus = "Message Deleting Failed!"
                })
            }
        }
    }
</script>

<style lang="scss" scoped>

</style>