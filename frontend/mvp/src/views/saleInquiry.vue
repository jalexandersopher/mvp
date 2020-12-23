<template>
    <div>
        <div class="input">
          <label for="item_name">What is the listed title of the item which you wish to inquire about?</label>
          <input type="text" id="item_name" v-model="item_name" />
        </div>
        <div class="input">
          <label for="email">What is your email?</label>
          <input type="text" id="email" v-model="email" />
        </div>
        <div class="input">
          <label for="description">Additional Notes</label>
          <input type="text" id="description" v-model="description" />
        </div>
        <div class="submit">
          <button @click="sendInquiry" >Submit</button>
        </div>
        <div>
            <p>
                {{ saleInquiryStatus }}
            </p>
        </div>
    </div>
</template>

<script>
import axios from "axios";

    export default {
        name: "SaleInquiry",
        data() {
            return {
                item_name: "",
                email: "",
                description: "",
                saleInquiryStatus: "Waiting to Send",
            }
        },
        methods: {
            sendInquiry: function() {
                this.saleInquiryStatus = "Sending!"
                axios.request({
                    url: "http://localhost:5000/api/contact",
                    headers: {
                        "Content-Type": "application/json",
                    },
                    method: "POST",
                    data: {
                        "item_name": this.item_name,
                        "email": this.email,
                        "description": this.description,
                    }
                }).then((response) => {
                    console.log(response)
                    this.saleInquiryStatus = "Sent Successfully!"
                }).catch((error) => {
                    console.log(error)
                    this.saleInquiryStatus = "Send Failed!"
                })
            }
        }
    }
</script>

<style lang="scss" scoped>

</style>