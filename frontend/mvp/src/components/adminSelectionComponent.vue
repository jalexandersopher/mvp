<template>
    
    
    <div id="pageContainer">
        <div>

        </div>
        <div id="adminLinksContainer">
            <div>

            </div>
            <div>
                <router-link id="adminLinks" to="/listproduct">List a new Product</router-link>
            </div>
            <div>
                <router-link id="adminLinks" to="/deleteproduct">Delete a Product</router-link>
            </div>
            <div>
                <router-link id="adminLinks" to="/clientmessages">View Client Messages</router-link>
            </div>
            <div>
                <router-link id="adminLinks" to="/deleteclientmessages">Delete Client Messages</router-link>
            </div>
            <div>

            </div>
        </div>
    </div>
</template>

<script>
    export default {
        name: "AdminSelection",
    }
</script>

<style lang="scss" scoped>
    #pageContainer {
        display: grid;
        grid-template-rows: 8vh 8vh;
    }

    #adminLinks {
        text-decoration: none;
        color: black;
        font-size: 20px;
        font-weight: bold;
    }

    #adminLinksContainer {
        display: grid;
        grid-template-columns: 10vw 20vw 20vw 20vw 20vw 10vw;
        justify-content: center;
        align-items: center;
        justify-items: center;
        align-content: center;
    }
</style>