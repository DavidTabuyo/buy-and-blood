<template>
    <div class="card flex flex-col justify-center">
        <!-- Contenedor para InputText y SelectButton en una fila -->
        <div class="flex space-x-4 mb-4">
            <div class="flex-1">
                <FloatLabel variant="in">
                    <IconField>
                        <InputIcon class="pi pi-search" />
                        <InputText id="in_label" v-model="value2" autocomplete="off" variant="filled" />
                    </IconField>
                    <label for="in_label">Buscar activo</label>
                </FloatLabel>
            </div>
            <div class="flex-1">
                <SelectButton v-model="value" :options="options" optionLabel="name" aria-labelledby="single" />
            </div>
        </div>

        <!-- ScrollPanel con un tamaño dinámico -->
        <div>
            <Panel>
                <ScrollPanel style="width: 100%; height: 100%;">
    <div class="flex flex-wrap space-x-4">
        <div class="w-64 min-w-64 h-64 border border-black rounded-xl mb-4"></div>
        <div class="w-64 min-w-64 h-64 border border-black rounded-xl mb-4"></div>
        <div class="w-64 min-w-64 h-64 border border-black rounded-xl mb-4"></div>
        <div class="w-64 min-w-64 h-64 border border-black rounded-xl mb-4"></div>
        <div class="w-64 min-w-64 h-64 border border-black rounded-xl mb-4"></div>
        <div class="w-64 min-w-64 h-64 border border-black rounded-xl mb-4"></div>
        <div class="w-64 min-w-64 h-64 border border-black rounded-xl mb-4"></div>
        <div class="w-64 min-w-64 h-64 border border-black rounded-xl mb-4"></div>
        <div class="w-64 min-w-64 h-64 border border-black rounded-xl mb-4"></div>
        <div class="w-64 min-w-64 h-64 border border-black rounded-xl mb-4"></div>
        <div class="w-64 min-w-64 h-64 border border-black rounded-xl mb-4"></div>
        <div class="w-64 min-w-64 h-64 border border-black rounded-xl mb-4"></div>
        <div class="w-64 min-w-64 h-64 border border-black rounded-xl mb-4"></div>
        <div class="w-64 min-w-64 h-64 border border-black rounded-xl mb-4"></div>
        <!-- Agrega más divs si lo necesitas -->
    </div>
</ScrollPanel>
            </Panel>


        </div>
    </div>
</template>

<script setup>

import { ref, watch } from 'vue';
import InputText from 'primevue/inputtext';
import FloatLabel from 'primevue/floatlabel';
import IconField from 'primevue/iconfield';
import InputIcon from 'primevue/inputicon';
import SelectButton from 'primevue/selectbutton';
import ScrollPanel from 'primevue/scrollpanel';

//opciones del selector 
const options = ref([
    { name: 'Crypto', value: 1 },
    { name: 'Activos', value: 2 }
]);

// Inicializar con la opción "todas por defeco"
const value = ref(options.value[0]);
const searchText = ref(null);


</script>
