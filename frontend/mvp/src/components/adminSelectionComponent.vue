<template>
    <div>
        <div>
            <router-link to="/listproduct">List a new Product</router-link>
        </div>
        <div>
            <router-link to="/deleteproduct">Delete a Product</router-link>
        </div>
        <div>
            <router-link to="/clientmessages">View Client Messages</router-link>
        </div>
    </div>
</template>

<script>
    export default {
        name: "AdminSelection",
    }
</script>

<style lang="scss" scoped>

</style>