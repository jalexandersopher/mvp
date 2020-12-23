<template>
    <div>
        <header-component></header-component>
        <div v-for="contact in contacts" :key="contact.id">
            <message-component :messageObject="contact"></message-component>
        </div>
    </div>
</template>

<script>
import HeaderComponent from "../components/headerComponent.vue";
import axios from "axios";
import MessageComponent from "../components/message.vue";

    export default {
        name: "ViewClientMessages",
        data() {
            return {
                contacts: []
            }
        },
        components: {
            HeaderComponent,
            MessageComponent
        },
        mounted: function() {
            this.getMessages();
        },
        methods: {
            getMessages: function() {
                axios.request({
                    url: "http://localhost:5000/api/contact",
                    headers: {
                        "Content-Type": "application/json",
                    },
                    method: "GET",
                }).then((response) => {
                    console.log(response)
                    this.contacts = response.data
                }).catch((error) => {
                    console.log(error)
                });
            }
        },
    }
</script>

<style lang="scss" scoped>

</style>