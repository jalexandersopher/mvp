<template>
    <div id="headerContainer">
        <div>
            <h1>
                TS Wooden Creations
            </h1>
        </div>
        <div>
            <router-link class="headerLinks" to="/">Home</router-link>
        </div>
        <div>
            <router-link class="headerLinks" to="/aboutus">About Us</router-link>
        </div>
        <div>
            <router-link class="headerLinks" to="/shop">Shop</router-link>
        </div>
        <div>
            <router-link class="headerLinks" to="/gallery">Gallery</router-link>
        </div>
        <div>
            <router-link class="headerLinks" to="/contactus">Contact Us</router-link>
        </div>
    </div>
</template>

<script>
    export default {
        name: "HeaderComponent"
    }
</script>

<style lang="scss" scoped>
    

    #headerContainer {
        display: grid;
        grid-template-columns: 26vw 14.8vw 14.8vw 14.8vw 14.8vw 14.8vw;
        grid-template-rows: 10vh;
        justify-content: center;
        align-items: center;
        justify-items: center;
        background-color: #4d4d4d;
    }

    .headerLinks {
        text-decoration: none;
        color: black;
        font-size: 20px;
    }

</style>