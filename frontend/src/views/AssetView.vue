<template>
    <div class="flex w-full gap-8">
      <!-- Si hay datos válidos -->
      <div v-if="assetData && !assetData.error" class="w-2/3 flex flex-col h-full">
        <div class="text-3xl text-gray-500">{{ assetData.longName }}</div>
        <!-- … resto del template … -->
      </div>
  
      <!-- Si devolvió error -->
      <div v-else-if="assetData?.error" class="w-full text-center text-red-500">
        {{ assetData.error }}
      </div>
  
      <!-- … tu sección de compra/venta … -->
    </div>
  </template>
  
  <script setup>
  import { ref, onMounted, onBeforeUnmount } from 'vue'
  import { useRoute, useRouter } from 'vue-router'
  // Asegúrate de importar aquí EL axios configurado con tu interceptor:
  //   import apiClient from '@/plugins/apiClient'
  import apiClient from '../axios.js' 
  import { useAuthStore } from '@/stores/auth'
  import { useUiStore } from '@/stores/ui'
  
  const route  = useRoute()
  const router = useRouter()
  const auth   = useAuthStore()
  const ui     = useUiStore()
  const ticker = route.params.ticker
  
  const assetData = ref(null)
  let intervalId = null
  
  async function fetchAssetData() {
    try {
      const { data } = await apiClient.get(`asset/${ticker}/`)
      assetData.value = data
    } catch (error) {
      const status = error.response?.status
      // Si no estás autorizado
      if (status === 401 || status === 403) {
        // 1) Detenemos el polling
        clearInterval(intervalId)
        // 2) Limpiamos el estado de auth
        auth.isLoggedIn = false
        auth.user_data  = null
        // 3) Abrimos el diálogo
        ui.openAuthDialog()
        // 4) Hacemos una navegación interna (SPA) a Home
        router.replace({ path: '/', query: { sessionExpired: '1' } })
      } else {
        console.error('Error al obtener datos:', error)
        assetData.value = { error: 'No se pudo obtener el asset' }
      }
    }
  }
  
  onMounted(async () => {
    // Primero comprobamos sesión
    await auth.checkSession()
    if (auth.isLoggedIn) {
      // Carga inicial y arranque del polling
      await fetchAssetData()
      intervalId = setInterval(fetchAssetData, 5000)
    } else {
      // Si ya no había sesión, hacemos lo mismo que en el catch
      ui.openAuthDialog()
      router.replace({ path: '/', query: { sessionExpired: '1' } })
    }
  })
  
  onBeforeUnmount(() => {
    if (intervalId) clearInterval(intervalId)
  })
  </script>
  