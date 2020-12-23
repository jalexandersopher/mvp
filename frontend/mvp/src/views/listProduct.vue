<template>
    <div>
        <header-component></header-component>
        <div class="input">
          <label for="title">Title</label>
          <input type="text" id="title" v-model="title" />
        </div>
        <div class="input">
          <label for="price">Price</label>
          <input type="text" id="price" v-model="price" />
        </div>
        <div class="input">
          <label for="picture">Picture</label>
          <input type="file" id="picture" />
        </div>
        <div class="input">
          <label for="description">Description</label>
          <input type="text" id="description" v-model="description" />
        </div>
        <div class="input">
          <label for="category">Category</label>
          <input type="text" id="category" v-model="category" />
        </div>
        <div class="submit">
          <button @click="postProduct" >Submit</button>
        </div>
        <div>
            <p>
                {{ listContentStatus }}
            </p>
        </div>
    </div>
</template>

<script>
import axios from "axios"
import cookies from "vue-cookies";
import HeaderComponent from "../components/headerComponent.vue";

    export default {
        name: "ListProduct",
        components: {
            HeaderComponent
        },
        data() {
            return {
                title: "",
                price: "",
                picture: "",
                description: "",
                category: "",
                listContentStatus: "Waiting to List",
            }
        },
        methods: {
            postProduct: function() {
                this. listContentStatus = "Listing!"
                axios.request({
                    url: "http://localhost:5000/api/card",
                    headers: {
                        "Content-Type": "application/json",
                    },
                    method: "POST",
                    data: {
                        "loginToken": cookies.get("loginToken"),
                        "title": this.title,
                        "price": this.price,
                        "picture": this.picture,
                        "description": this.description,
                        "category": this.category
                    }
                }).then((response) => {
                    console.log(response)
                    this.listContentStatus = "Listing Successful!"
                }).catch((error) => {
                    console.log(error)
                    this.listContentStatus = "Listing Failed!"
                })
            }
        }
    }
</script>

<style lang="scss" scoped>

</style>