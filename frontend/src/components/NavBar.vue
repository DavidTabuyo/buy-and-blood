<template>
    <div :key="key" class="fixed w-full top-0 z-50 shadow-md h-[90px] flex items-center bg-white">
        <div class="w-full h-full flex items-center">
            <Menubar :model="items" class="w-full h-full px-8 lg:px-8 text-lg">
                <template #start>
                    <router-link to="/">
                        <img :src="Logo" alt="Mi Logo" class="h-17 w-auto mr-8 ml-8 cursor-pointer" />
                    </router-link>
                </template>

                <!-- BOTONES A LA DERECHA -->
                <template #end>
                    <div v-if="!auth.isLoggedIn">
                        <Button @click="loginWithGoogle"
                            class="flex items-center gap-2 bg-white border border-gray-300 hover:shadow-lg transition rounded-full px-4 py-2">
                            <i class="pi pi-google"></i>
                            <span class="text-gray-700 font-medium">Iniciar sesión con Google</span>
                        </Button>
                    </div>

                    <div v-else class="flex items-center space-x-4">
                        <Tag severity="info">
                            Saldo disponible:
                            <DolarValue :value="auth.user_data.balance" />
                        </Tag>
                        <Avatar @click="toggle" icon="pi pi-user" class="ml-auto cursor-pointer" size="large"
                            style="background-color: #ece9fc; color: #2a1261" shape="circle" />
                    </div>

                    <Popover ref="op">
                        <div class="flex flex-col space-y-2">
                            <Button @click="wallet" label="Mi cartera" severity="secondary" icon="pi pi-wallet" />
                            <Button @click="showDialog = true" label="Agregar saldo" severity="secondary"
                                icon="pi pi-dollar" />
                            <Button @click="logout" label="Cerrar sesión" severity="secondary" icon="pi pi-sign-out" />
                        </div>
                    </Popover>
                </template>
            </Menubar>
        </div>
    </div>
    <Toast />

    <Dialog header="Agregar saldo" v-model:visible="showDialog" modal closable>

        <FloatLabel variant="on" class="w-full mt-4 mb-4">
            <InputNumber class="w-full text-center" v-model="amount" mode="currency" currency="USD" locale="en-US" />
            <label>Introduce cantidad…</label>
        </FloatLabel>
        <template #footer>
            <div class="flex gap-2 justify-between">
                <Button label="Cancelar" @click="showDialog = false" />
                <Button  label="Aceptar" severity="success"
                    @click="addBalanceButton" />
            </div>
        </template>
    </Dialog>

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
import DolarValue from '@/components/utils/DolarValue.vue'
import Logo from '@/assets/big_b.svg';
import Dialog from 'primevue/dialog'
import InputNumber from 'primevue/inputnumber'
import FloatLabel from 'primevue/floatlabel'

//accedemos al valor booleano del log in del usuario
const auth = useAuthStore()
const router = useRouter()
const op = ref();
const toast = useToast();
const emit = defineEmits(['reset-app'])
const key = ref(0)
const showDialog = ref(false);
const amount = ref(0);

function loginWithGoogle() {
    window.location.href = 'https://buyandblood.onrender.com/auth/google/login/'
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


const addBalanceButton = (event) => {
    if(amount.value==0) {
        toast.add({ severity: 'error', summary: 'Error', detail: 'El valor no puede ser 0', life: 3000 });
        showDialog.value = false;
    }else{
        let amountStr = amount.value+"";

        axios.put(`user/add-balance/${amountStr}/`)
        .then(() => {

            toast.add({
                severity: 'success',
                summary: 'Operación aceptada',
                detail: `Su saldo ha sido añadido: +${amount.value}`,
                life: 3000
            });
            //cambiamos el valor en auth.
            auth.user_data.balance+= amount.value;
        })
        .catch(err => {
            toast.add({
                severity: 'error',
                summary: 'Error',
                detail: 'Ha ocurrido un error',
                life: 3000
            });
            console.error('Error al seleccionar plan:', err);
        });

    showDialog.value = false;
    }


};

const logout = () => {
    //llamamos al logout del backend
    axios.post('user/logout/')
        .then((response) => {
            toast.add({ severity: 'success', summary: 'La sesión se ha cerrado correctamente', life: 3000 });
            emit('reset-app');
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

<style scoped>
/* Aumenta el tamaño base del texto de los items */
.p-menubar .p-menuitem-text {
    font-size: 2rem;
    /* ~18px */
}
</style>