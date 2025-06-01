import axios from 'axios'
import router from '@/router'          
import { useUiStore } from '@/stores/ui'
import { useAuthStore } from '@/stores/auth'

axios.defaults.baseURL = 'https://buyandblood.onrender.com/api/'
axios.defaults.headers.common['Content-Type'] = 'application/json'
axios.defaults.withCredentials = true  // para enviar cookies de sesión y CSRF

function getCookie(name) {
  const value = `; ${document.cookie}`;
  const parts = value.split(`; ${name}=`);
  if (parts.length === 2) return parts.pop().split(';').shift();
}

// Interceptor para añadir token CSRF a métodos que lo requieren
axios.interceptors.request.use(config => {
  if (!['get', 'head', 'options'].includes(config.method)) {
    const csrftoken = getCookie('csrftoken');
    if (csrftoken) {
      config.headers['X-CSRFToken'] = csrftoken;
    }
  }
  return config;
}, error => Promise.reject(error));

axios.interceptors.response.use(
  res => res,
  err => {
    const status = err.response?.status
    if (status === 401 || status === 403) {
      // Limpia estado auth y redirige
      const auth = useAuthStore()
      auth.isLoggedIn = false
      auth.user_data  = null

      router.push({ path: '/', })
    }
    return Promise.reject(err)
  }
)

export default axios
