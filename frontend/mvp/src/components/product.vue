<template>
    <div>
        <div>{{productObject}}</div>
    </div>
</template>

<script>
    export default {
        name: "ProductComponent",
        props: {
            productObject: {
                type: Object,
                required: true
            }
        }
    }
</script>

<style lang="scss" scoped>

</style>