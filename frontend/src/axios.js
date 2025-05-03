// src/plugins/axios.js
import axios from 'axios'
import { useUiStore } from '@/stores/ui'
import { useAuthStore } from '@/stores/auth'

// Configura la instancia global de axios
axios.defaults.baseURL = 'http://localhost:8000/api/'
axios.defaults.headers.common['Content-Type'] = 'application/json'
// Si usas cookies de sesión:
// axios.defaults.withCredentials = true

// Interceptor de respuestas
axios.interceptors.response.use(
  res => res,
  err => {
    if (err.response?.status === 403 || err.response?.status === 401) {
      //redirigimos a la página de home
      window.location.href = '/';
      
      // 1) Abre el diálogo de PrimeVue
      const ui = useUiStore()
      ui.openAuthDialog()

      // 2) Opcional: limpia el estado de autenticación
      const auth = useAuthStore()
      auth.isLoggedIn = false
      auth.user_data  = null
    }
    return Promise.reject(err)
  }
)

export default axios
