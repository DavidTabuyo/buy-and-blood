import { createRouter, createWebHistory } from "vue-router";
import HomeView from "../views/HomeView.vue";
import InvestingPlansView from "../views/InvestingPlansView.vue";
import AssetView from "../views/AssetView.vue"
import ContactView from "../views/ContactView.vue"
import ProfileView from "../views/ProfileView.vue";

// Definición de las rutas de la aplicación
const routes = [
  { path: "/", component: HomeView },        // Ruta de Inicio
  { path: "/investing-plans", component: InvestingPlansView },  // Ruta de Acerca de
  { path: "/contact", component: ContactView }, // Ruta de Contacto
  { path: "/asset/:ticker", component: AssetView }, // Ruta de Asset
  { path: "/profile", component: ProfileView }, // Ruta de Perfil
  { path: "/:catchAll(.*)", redirect: "/" } // Ruta para manejar rutas no encontradas
];

const router = createRouter({
  history: createWebHistory(),
  routes
});

export default router;
