<template>
    <div>
        <header-component></header-component>
        <login-component></login-component>
    </div>
</template>

<script>
import LoginComponent from "../components/loginComponent.vue";
import HeaderComponent from "../components/headerComponent.vue";

    export default {
        name: "AdminLogin",
        components: {
            LoginComponent,
            HeaderComponent
        }
    }
</script>

<style lang="scss" scoped>

</style>