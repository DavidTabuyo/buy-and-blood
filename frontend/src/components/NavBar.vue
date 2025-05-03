<template>
    <div class="fixed w-full top-0 z-50 shadow-md h-[70px] flex items-center bg-white">
        <div class="w-full h-full flex items-center">
            <Menubar :model="items" class="px-4 lg:px-8 w-full h-full">
                <template #start>
                    <p class="text-2xl font-bold text-indigo-600">BUY-LOGO</p>
                </template>
                <template #end>
                    <Button @click="loginWithGoogle"
                        class="flex items-center gap-2 bg-white border border-gray-300 hover:shadow-lg transition rounded-full px-4 py-2">
                        <!-- Google “G” icon -->
                         <i class="pi pi-google"></i>
                        <span class="text-gray-700 font-medium">Iniciar sesión con Google</span>
                    </Button>
                </template>
            </Menubar>
        </div>
    </div>
</template>

<script setup>
import { ref } from 'vue'
import { useRouter } from 'vue-router'
import Menubar from 'primevue/menubar'
import Button from 'primevue/button'

const router = useRouter()

function loginWithGoogle() {
    window.location.href = 'http://localhost:8000/auth/google/login/'
}

const items = ref([
    {
        label: 'Home',
        icon: 'pi pi-home',
        command: () => router.push('/')
    },
    {
        label: 'Planes de inversión',
        icon: 'pi pi-star',
        command: () => router.push('/investing-plans')
    },
    {
        label: 'Contacto',
        icon: 'pi pi-envelope',
        command: () => router.push('/contact')
    }
])

mounted() {
  const url = new URL(window.location.href);
  if (url.searchParams.get('logged_in') === '1') {
    // MANEJAMOS
  }
}

</script>