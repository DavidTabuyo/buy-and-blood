<template>
    <div  :key="key" class="fixed w-full top-0 z-50 shadow-md h-[70px] flex items-center bg-white">
        <div class="w-full h-full flex items-center">
            <Menubar :model="items" class="px-4 lg:px-8 w-full h-full">
                <template #start>
                    <p class="text-2xl font-bold text-indigo-600">BUY-LOGO</p>
                </template>
                <template #end>
                    <div v-if="!auth.isLoggedIn">
                        <Button @click="loginWithGoogle"
                            class="flex items-center gap-2 bg-white border border-gray-300 hover:shadow-lg transition rounded-full px-4 py-2">
                            <!-- Google “G” icon -->
                            <i class="pi pi-google"></i>
                            <span class="text-gray-700 font-medium">Iniciar sesión con Google</span>
                        </Button>
                    </div>

                    <div v-if="auth.isLoggedIn" class="flex items-center space-x-4">
                        <Tag severity="info" :value="`Saldo disponible: ${auth.user_data.balance}$`" />
                        <Avatar @click="toggle" icon="pi pi-user" class="ml-auto cursor-pointer" size="large"
                            style="background-color: #ece9fc; color: #2a1261" shape="circle" />
                    </div>
                    <Popover ref="op">
                        <div class="flex flex-col space-y-2">
                            <Button @click="wallet" label="Mi cartera" severity="secondary" icon="pi pi-wallet" />
                            <Button @click="logout" label="Cerrar sesión" severity="secondary" icon="pi pi-sign-out" />
                        </div>
                    </Popover>


                </template>
            </Menubar>
        </div>
    </div>
    <Toast />
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { useRouter } from 'vue-router'
import { defineEmits } from 'vue'
import Menubar from 'primevue/menubar'
import Button from 'primevue/button'
import Avatar from 'primevue/avatar';
import Tag from 'primevue/tag';
import Popover from 'primevue/popover';
import Toast from 'primevue/toast';
import { useToast } from 'primevue/usetoast';
import axios from '@/axios.js';
import { useAuthStore } from '@/stores/auth'

//accedemos al valor booleano del log in del usuario
const auth = useAuthStore()
const router = useRouter()
const op = ref();
const toast = useToast();
const emit = defineEmits(['reset-app'])
const key = ref(0)

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

const toggle = (event) => {
    op.value.toggle(event);
}

const wallet = () => {
    router.push('/profile')
};


const logout = () => {
    //llamamos al logout del backend
    axios.post('user/logout/')
    .then((response) => {
        toast.add({ severity: 'success', summary: 'La sesión se ha cerrado correctamente', life: 3000 });
        emit('reset-app') ;
        key.value++;
        auth.logout()
    })
    .catch((error) => {
        toast.add({ severity: 'error', summary: 'Error', detail: 'Ha ocurrido un error cerrando la sesión', life: 3000 });
      console.error('Error al obtener datos:', error);
      key.value++;
    });
};


onMounted(() => {
    const url = new URL(window.location.href)
    if (url.searchParams.get('logged_in') === '1') {
        url.searchParams.delete('logged_in')
        window.history.replaceState(null, '', url.toString())
    } else {
        //el usuario no ha conseguido autenticarse

    }
})


</script>