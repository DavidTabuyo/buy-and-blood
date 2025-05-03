// src/stores/auth.js
import { defineStore } from 'pinia'
import apiClient from '@/services/apiClient'   // tu instancia de axios (withCredentials=true)

export const useAuthStore = defineStore('auth', {
  // ---------- STATE ----------
  state: () => ({
    isLoggedIn: false,
    user: null           // opcional: datos del usuario
  }),

  // ---------- GETTERS ----------
  getters: {
    username: (state) => state.user?.first_name || '',
  },

  // ---------- ACTIONS ----------
  actions: {
    /** Llama tras montar la app para saber si la cookie sessionid es válida */
    async checkSession() {
      try {
        const { data } = await apiClient.get('/auth/me/')   // crea este endpoint en Django
        this.isLoggedIn = true
        this.user = data
      } catch (err) {
        this.isLoggedIn = false
        this.user = null
      }
    },

    /** Redirige al flujo OAuth (backend hará el trabajo) */
    redirectToGoogle() {
      window.location.href = 'http://localhost:8000/auth/google/login/'
    },

    /** Cierra sesión tanto en Django como en la store */
    async logout() {
      await apiClient.post('/auth/logout/')  // endpoint que llame a django.contrib.auth.logout
      this.isLoggedIn = false
      this.user = null
    }
  },

  // ---------- PERSISTENCIA ----------
  persist: {
    storage: sessionStorage,  // o localStorage si quieres durar entre pestañas
    paths: ['isLoggedIn', 'user']
  }
})
