import Vue from "vue";
import VueRouter from "vue-router";
import AdminLogin from "../views/adminLogin.vue";
import AdminPanel from "../views/adminPanel.vue";
import ClientMessages from "../views/clientMessages.vue";
import DeleteProduct from "../views/deleteProduct.vue";
import ListProduct from "../views/listProduct.vue";
import HomePage from "../views/homePage.vue";
import GalleryView from "../views/galleryView.vue";
import AboutUs from "../views/aboutUs.vue";
import ShopView from "../views/shopView.vue";
import ContactUs from "../views/contactUs.vue";
import DeleteClientMessages from "../views/deleteClientMessages";

Vue.use(VueRouter);

const routes = [
  {
    path: "/",
    name: "HomePage",
    component: HomePage
  },
  {
    path: "/adminlogin",
    name: "AdminLogin",
    component: AdminLogin
  },
  {
    path: "/adminpanel",
    name: "AdminPanel",
    component: AdminPanel
  },
  {
    path: "/clientmessages",
    name: "ClientMessages",
    component: ClientMessages
  },
  {
    path: "/deleteproduct",
    name: "DeleteProduct",
    component: DeleteProduct
  },
  {
    path: "/listproduct",
    name: "ListProduct",
    component: ListProduct
  },
  {
    path: "/gallery",
    name: "GalleryView",
    component: GalleryView
  },
  {
    path: "/aboutus",
    name: "AboutUs",
    component: AboutUs
  },
  {
    path: "/shop",
    name: "ShopView",
    component: ShopView
  },
  {
    path: "/contactus",
    name: "ContactUs",
    component: ContactUs
  },
  {
    path: "/deleteclientmessages",
    name: "DeleteClientMessages",
    component: DeleteClientMessages
  }
];

const router = new VueRouter({
  routes
});

export default router;
