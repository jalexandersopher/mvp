<template>
    <div>
        <header-component></header-component>
        <admin-selection></admin-selection>
    </div>
</template>

<script>
import AdminSelection from "../components/adminSelectionComponent.vue";
import HeaderComponent from "../components/headerComponent.vue"

    export default {
        name: "AdminPanel",
        components: {
            AdminSelection,
            HeaderComponent
        }
    }
</script>

<style lang="scss" scoped>

</style>