// src/router/index.js
import { createRouter, createWebHistory } from 'vue-router'
import HomeView             from '@/views/HomeView.vue'
import InvestingPlansView   from '@/views/InvestingPlansView.vue'
import AssetView            from '@/views/AssetView.vue'
import ContactView          from '@/views/ContactView.vue'
import ProfileView          from '@/views/ProfileView.vue'

const routes = [
  { path: '/',               component: HomeView },
  { path: '/investing-plans',component: InvestingPlansView },
  { path: '/contact',        component: ContactView },
  { path: '/asset/:ticker',  component: AssetView },
  { path: '/profile',        component: ProfileView },
  { path: '/:catchAll(.*)',  redirect: '/' }
]

const router = createRouter({
  history: createWebHistory('/buy-and-blood/'),
  routes
})

export default router
