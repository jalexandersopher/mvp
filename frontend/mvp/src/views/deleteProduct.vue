<template>
    <div>
        <div class="input">
          <label for="title">Title</label>
          <input type="text" id="title" v-model="title" />
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
import cookies from "vue-cookies"

    export default {
        name: "DeleteProduct",
        data() {
            return {
                title: "",
                deleteContentStatus: "Waiting to List",
            }
        },
        methods: {
            deleteProduct: function() {
                this. deleteContentStatus = "Deleting!"
                axios.request({
                    url: "http://localhost:5000/api/card",
                    headers: {
                        "Content-Type": "application/json",
                    },
                    method: "DELETE",
                    data: {
                        "loginToken": cookies.get("loginToken"),
                        "title": this.title
                    }
                }).then((response) => {
                    console.log(response)
                    this.deleteContentStatus = "Product Deleted Successfully!"
                }).catch((error) => {
                    console.log(error)
                    this.deleteContentStatus = "Product Deleting Failed!"
                })
            }
        }
    }
</script>

<style lang="scss" scoped>

</style>