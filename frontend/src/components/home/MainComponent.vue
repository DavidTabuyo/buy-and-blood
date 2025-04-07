<template>
    <div class="card flex flex-col justify-center">
        <!-- Contenedor para InputText y SelectButton en una fila -->
        <div class="flex space-x-4 mb-4">
            <!-- FloatLabel con más espacio -->
            <div class="flex-[3]">
                <FloatLabel variant="on" class="w-full">
                    <IconField>
                        <InputIcon class="pi pi-search" />
                        <InputText id="in_label" v-model="value2" autocomplete="off" variant="filled" class="w-full" />
                    </IconField>
                    <label for="in_label">Buscar activo</label>
                </FloatLabel>
            </div>
            <!-- SelectButton con menos espacio -->
            <div class="flex-[1]">
                <ButtonGroup>
                    <Button label="Todas" :class="getButtonClass('opcion1')" @click="selectOption('opcion1')" />
                    <Button label="Fondos" :class="getButtonClass('opcion2')" @click="selectOption('opcion2')" />
                    <Button label="Cryptos" :class="getButtonClass('opcion3')" @click="selectOption('opcion3')" />
                </ButtonGroup>
            </div>
        </div>

        <div class="flex justify-center bg-white shadow-lg rounded-xl p-2">
            <ScrollPanel style="width: 100%; height: calc(100vh - 250px)">
                <div class="flex flex-wrap gap-4 justify-center pt-8 pb-8">
                    <div class="w-64 min-w-64 h-64 border border-black rounded-xl">
                    <MiniAsset></MiniAsset>
                    </div>
                    <div class="w-64 min-w-64 h-64 border border-black rounded-xl"></div>
                    <div class="w-64 min-w-64 h-64 border border-black rounded-xl"></div>
                    <div class="w-64 min-w-64 h-64 border border-black rounded-xl"></div>
                    <div class="w-64 min-w-64 h-64 border border-black rounded-xl"></div>
                    <div class="w-64 min-w-64 h-64 border border-black rounded-xl"></div>
                    <div class="w-64 min-w-64 h-64 border border-black rounded-xl"></div>
                    <div class="w-64 min-w-64 h-64 border border-black rounded-xl"></div>
                    <div class="w-64 min-w-64 h-64 border border-black rounded-xl"></div>
                    <div class="w-64 min-w-64 h-64 border border-black rounded-xl"></div>
                    <div class="w-64 min-w-64 h-64 border border-black rounded-xl"></div>
                    <div class="w-64 min-w-64 h-64 border border-black rounded-xl"></div>
                </div>
            </ScrollPanel>
        </div>
    </div>
</template>

<script setup>
import { ref } from 'vue';
import InputText from 'primevue/inputtext';
import FloatLabel from 'primevue/floatlabel';
import IconField from 'primevue/iconfield';
import InputIcon from 'primevue/inputicon';
import ScrollPanel from 'primevue/scrollpanel';
import Button from 'primevue/button';
import ButtonGroup from 'primevue/buttongroup';

import MiniAsset from '@/components/home/MiniAsset.vue'

const selected = ref('opcion1'); // Opción por defecto seleccionada

const selectOption = (option) => {
    selected.value = option;
};

// Función para asignar clases dinámicamente
const getButtonClass = (option) => {
    return {
        'p-button-primary': selected.value === option, // Color cuando está seleccionado
        'p-button-outlined': selected.value !== option // Color por defecto
    };
};
</script>
