<template>
  <div class="flex flex-col h-screen">
    <!-- Barra de navegación -->
    <div>
      <NavBar @reset-app="onResetApp"/>
    </div>

    <!-- Contenido principal -->
    <div class="flex-1 pt-24 px-16 pb-16">
      <router-view :key="appKey" class="h-full" />
    </div>

    <!-- Diálogo de sesión expirada -->
    <div>
      <Dialog header="No tienes acceso a esta función" :visible="ui.showAuthDialog" modal closable
        @hide="ui.closeAuthDialog">
        <p>Para usar esta función necesitas iniciar sesión</p>
        <template #footer>
          <Button label="Aceptar" @click="ui.closeAuthDialog" />
        </template>
      </Dialog>
    </div>
  </div>
</template>

<script setup>
import NavBar from '@/components/NavBar.vue'
import { onMounted, ref } from 'vue'
import { useRoute, useRouter } from 'vue-router'
import { storeToRefs } from 'pinia'

import { useAuthStore } from '@/stores/auth'
import { useUiStore } from '@/stores/ui'

import Dialog from 'primevue/dialog'
import Button from 'primevue/button'

// Pinia stores
const auth = useAuthStore()
const ui = useUiStore()

// Router
const route = useRoute()
const router = useRouter()
const appKey = ref(0)

// Refs (si necesitas mostrar info de auth en la UI)
const { isLoggedIn, user_data } = storeToRefs(auth)

// Al montar, comprobamos sesión
onMounted(async () => {
  await auth.checkSession()
})

// Si venimos con ?sessionExpired=1, abrimos el diálogo y limpiamos la URL
if (route.query.sessionExpired === '1') {
  ui.openAuthDialog()
  // eliminamos el query param para que no vuelva a dispararse
  const q = { ...route.query }
  delete q.sessionExpired
  router.replace({ query: q })
}

function onResetApp() {
  appKey.value++
}

// Acción del botón "Login" del diálogo
</script>

<style scoped>
.logo {
  height: 6em;
  padding: 1.5em;
  will-change: filter;
  transition: filter 300ms;
}

.logo:hover {
  filter: drop-shadow(0 0 2em #646cffaa);
}

.logo.vue:hover {
  filter: drop-shadow(0 0 2em #42b883aa);
}
</style>
