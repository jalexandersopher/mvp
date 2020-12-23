<template>
    <div>
        <div>{{messageObject}}</div>
    </div>
</template>

<script>
    export default {
        name: "MessageComponent",
        props: {
            messageObject: {
                type: Object,
                required: true
            }
        }
    }
</script>

<style lang="scss" scoped>

</style>