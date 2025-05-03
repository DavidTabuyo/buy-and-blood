// src/plugins/axios.js
import axios from 'axios'
import router from '@/router'          // 🚩 importa la instancia de Vue Router
import { useUiStore } from '@/stores/ui'
import { useAuthStore } from '@/stores/auth'

axios.defaults.baseURL = 'http://localhost:8000/api/'
axios.defaults.headers.common['Content-Type'] = 'application/json'
axios.defaults.withCredentials = true  // si usas cookies de sesión

axios.interceptors.response.use(
  res => res,
  err => {
    const status = err.response?.status
    if (status === 401 || status === 403) {
      // 1) Limpia el estado de auth
      const auth = useAuthStore()
      auth.isLoggedIn = false
      auth.user_data  = null

      // 2) Navega internamente a "/" sin recargar
      router.push({ path: '/',})

    }
    return Promise.reject(err)
  }
)

export default axios
