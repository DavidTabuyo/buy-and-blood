<template>
    <div class="fixed w-full top-0 z-50 shadow-md h-[70px] flex items-center">
        <div class="w-full h-full flex items-center">
            <Menubar :model="items" class="px-4 lg:px-8 w-full h-full">
                <template #start>
                    <p>BUY-LOGO</p>
                </template>
                <template #end>
                    <p>USUARIO LOGEADO DATA</p>
                </template>
            </Menubar>
        </div>
    </div>
</template>


<script setup>
import { ref } from "vue";
import Menubar from 'primevue/menubar';
import { useRouter } from 'vue-router';
const router = useRouter();

const items = ref([
    {
        label: 'Home',
        icon: 'pi pi-home',
        command: () => {
            router.push('/');
        }
    },
    {
        label: 'Planes de inversión',
        icon: 'pi pi-star',
        command: () => {
            router.push('/investing-plans');
        }
    },
    {
        label: 'Contacto',
        icon: 'pi pi-envelope',
        command: () => {
            window.location.href = 'http://localhost:8000/auth/google/login/';

            //router.push('/contact');
        }
    }
]);
</script>
