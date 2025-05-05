// stores/auth.js
import { defineStore } from 'pinia'

import axios from 'axios'
export const useAuthStore = defineStore('auth', {
  state: () => ({
    isLoggedIn: false,
    user_data: null
  }),

  actions: {
    async checkSession() {
      try {
        const { data } = await axios.get('/check/auth/')
        this.isLoggedIn = true
        this.user_data = data
      } catch {
        this.isLoggedIn = false
        this.user_data = null
      }
    },
    redirectToGoogle() {
      window.location.href = 'http://localhost:8000/auth/google/login/'
    },
    async logout() {
      await axios.post('/auth/logout/')
      this.isLoggedIn = false
      this.user_data = null
    }
  }
})
