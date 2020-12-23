<template>
  <div>
    <header-component></header-component>
    <div>
      <div>
          Send me a message!
      </div>
      <div class="input">
          <label for="name">What's your name?</label>
          <input type="text" id="name" v-model="name"/>
      </div>
      <div class="input">
        <label for="item_name"
          >What is the listed title of the item which you wish to inquire
          about?</label
        >
        <input type="text" id="item_name" v-model="item_name" />
      </div>
      <div class="input">
        <label for="email">What is your email?</label>
        <input type="text" id="email" v-model="email" />
      </div>
      <div class="input">
        <label for="description">Message</label>
        <input type="text" id="description" v-model="description" />
      </div>
      <div class="submit">
        <button @click="sendInquiry">Submit</button>
      </div>
      <div>
        <p>
          {{ saleInquiryStatus }}
        </p>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";
import HeaderComponent from "../components/headerComponent.vue";

export default {
  name: "ContactUs",
  components: {
    HeaderComponent,
  },
  data() {
    return {
      name: "",
      item_name: "",
      email: "",
      description: "",
      saleInquiryStatus: "Waiting to Send",
    };
  },
  methods: {
    sendInquiry: function () {
      this.saleInquiryStatus = "Sending!";
      axios
        .request({
          url: "http://localhost:5000/api/contact",
          headers: {
            "Content-Type": "application/json",
          },
          method: "POST",
          data: {
            name: this.name,
            item_name: this.item_name,
            email: this.email,
            description: this.description,
          },
        })
        .then((response) => {
          console.log(response);
          this.saleInquiryStatus = "Sent Successfully!";
        })
        .catch((error) => {
          console.log(error);
          this.saleInquiryStatus = "Send Failed!";
        });
    },
  },
};
</script>

<style lang="scss" scoped>
</style>