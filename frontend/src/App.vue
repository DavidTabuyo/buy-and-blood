<template>
  <div class="flex flex-col h-screen">
    <!-- Barra de navegación -->
    <div>
      <NavBar></NavBar>
    </div>

    <!-- Contenido principal -->
    <div class="flex-1  pt-24 px-16 pb-16">
      <router-view class="h-full"></router-view>
    </div>

    <div>
      <Dialog header="Sesión expirada" :visible="ui.showAuthDialog" modal closable @hide="ui.closeAuthDialog">
        <p>Tu sesión ha expirado. ¿Quieres volver a iniciar sesión?</p>
        <template #footer>
          <Button label="Login" @click="goToLogin" />
        </template>
      </Dialog>
    </div>
  </div>
</template>

<script setup>
import NavBar from '@/components/NavBar.vue';
import { onMounted, watch } from 'vue'
import { useRoute, useRouter } from 'vue-router'
import { useAuthStore } from '@/stores/auth'
import Dialog from 'primevue/dialog';
import { storeToRefs } from 'pinia'
import { useUiStore } from '@/stores/ui'
import Button from 'primevue/button'

const ui = useUiStore()
const route = useRoute()
const router = useRouter()
const auth = useAuthStore()
const { isLoggedIn, user_data } = storeToRefs(auth)

onMounted(async () => {
  await auth.checkSession();
  console.log(isLoggedIn.value);
});

// 2) Observa cambios en el query param `logged_in`
watch(
  () => route.query.logged_in,
  async (val) => {
    if (val === '1') {
      // llegó de Google; refresca la sesión y marca isLoggedIn=true si todo OK
      await auth.checkSession()
      // 3) Limpia la URL
      const q = { ...route.query }
      delete q.logged_in
      router.replace({ query: q })
    }
  },
  { immediate: true }
);
function goHome() {
  ui.closeAuthDialog()
}

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
