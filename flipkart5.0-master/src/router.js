import { createRouter, createWebHistory } from "vue-router";

import login from './components/LoginPageForm.vue';
import signup from "./components/Signup.vue";
import notFound from "./components/notFound.vue";
import DisplayScreen from './components/DisplayScreen.vue'

const routes = [
  {
    path: "/",
    component: login,
  },
  {
    path: "/signup",
    component: signup,
  },
  {
    path:'/home',
    component: DisplayScreen
  },
  {
    path: "/notFound",
    component: notFound,
  },
//   {
//     path: "/:catchAll(.*)",
//     redirect: "/notFound",
//   },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
