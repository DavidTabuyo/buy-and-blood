import { createRouter, createWebHistory } from "vue-router";
import HomeView from "../views/HomeView.vue";
import InvestingPlansView from "../views/InvestingPlansView.vue";
import AssetView from "../views/AssetView.vue"
import ContactView from "../views/ContactView.vue"
const routes = [
  { path: "/", component: HomeView },        // Ruta de Inicio
  { path: "/investing-plans", component: InvestingPlansView },  // Ruta de Acerca de
  { path: "/contact", component: ContactView }, // Ruta de Contacto
  { path: "/asset/:ticker", component: AssetView } // Ruta de Asset
];

const router = createRouter({
  history: createWebHistory(),
  routes
});

export default router;
