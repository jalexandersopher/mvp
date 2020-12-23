<template>
    <div>
        <header-component></header-component>
        <div v-for="card in cards" :key="card.id">
            <product-component :productObject="card"></product-component>
        </div>
    </div>
</template>

<script>
import HeaderComponent from "../components/headerComponent.vue";
import axios from "axios";
import ProductComponent from "../components/product.vue"

    export default {
        name: "ShopView",
        data() {
            return {
                cards: []
            }
        },
        components: {
            HeaderComponent,
            ProductComponent
        },
        mounted: function() {
            this.getProducts();
        },
        methods: {
            getProducts: function() {
                axios.request({
                    url: "http://localhost:5000/api/cards",
                    headers: {
                        "Content-Type": "application/json",
                    },
                    method: "GET",
                }).then((response) => {
                    console.log(response)
                    this.cards = response.data
                }).catch((error) => {
                    console.log(error)
                });
            }
        },
    }
</script>

<style lang="scss" scoped>

</style>