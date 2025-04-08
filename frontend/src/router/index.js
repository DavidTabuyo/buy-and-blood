import { createRouter, createWebHistory } from "vue-router";
import HomeView from "../views/HomeView.vue";
import AboutView from "../views/AboutView.vue";
import ContactView from "../views/ContactView.vue";
import AssetView from "../views/AssetView.vue"
import 'primeicons/primeicons.css';

const routes = [
  { path: "/", component: HomeView },        // Ruta de Inicio
  { path: "/about", component: AboutView },  // Ruta de Acerca de
  { path: "/contact", component: ContactView }, // Ruta de Contacto
  { path: "/asset/:ticker", component: AssetView } // Ruta de Asset
];

const router = createRouter({
  history: createWebHistory(),
  routes
});

export default router;
