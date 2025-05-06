// stores/auth.ts
import { defineStore } from 'pinia'
import axios from 'axios'

export const useAuthStore = defineStore('auth', {
  state: () => ({
    isLoggedIn: false,
    user_data: null
  }),

  actions: {
    async checkSession() {
      console.log("Comprobando sesión...");
      try {
        const response = await axios.get('/check/auth/');
        if (response && response.data.user_balance) {
          this.isLoggedIn = true;
          this.user_data = response.data.user_balance;
          console.log("Sesión verificada con éxito.");
        }
      } catch (error) {
        console.log("user baaad");
        this.isLoggedIn = false;
        this.user_data = null;
        console.error("Error al verificar la sesión:", error);
      }
    },
    
    redirectToGoogle() {
      window.location.href = 'http://localhost:8000/auth/google/login/';
    },
    
    async logout() {
      try {
        await axios.post('/auth/logout/');
        this.isLoggedIn = false;
        this.user_data = null;
      } catch (error) {
        console.error("Error al cerrar sesión:", error);
      }
    }
  }
});
