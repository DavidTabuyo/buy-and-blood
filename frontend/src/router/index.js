import { createRouter, createWebHistory } from "vue-router";
import HomeView from "../views/HomeView.vue";
import AboutView from "../views/AboutView.vue";
import ContactView from "../views/ContactView.vue";

const routes = [
  { path: "/", component: HomeView },        // Ruta de Inicio
  { path: "/about", component: AboutView },  // Ruta de Acerca de
  { path: "/contact", component: ContactView } // Ruta de Contacto
];

const router = createRouter({
  history: createWebHistory(),
  routes
});

export default router;
