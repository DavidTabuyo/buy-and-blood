// stores/auth.js
import { defineStore } from 'pinia'

import axios from 'axios'
export const useAuthStore = defineStore('auth', {
  state: () => ({
    isLoggedIn: false,
    user: null
  }),

  actions: {
    async checkSession() {
      try {
        const { data } = await axios.get('/auth/me/')
        this.isLoggedIn = true
        this.user       = data
      } catch {
        this.isLoggedIn = false
        this.user       = null
      }
    },
    redirectToGoogle() {
      window.location.href = 'http://localhost:8000/auth/google/login/'
    },
    async logout() {
      await axios.post('/auth/logout/')
      this.isLoggedIn = false
      this.user       = null
    }
  }
})
