<template>
    <div class="card flex flex-col justify-center">
        <!-- Contenedor para InputText y SelectButton en una fila -->
        <div class="flex space-x-4 mb-4">
            <!-- FloatLabel con más espacio -->
            <div class="flex-[3]">
                <FloatLabel variant="on" class="w-full">
                    <IconField>
                        <InputIcon class="pi pi-search" />
                        <InputText id="in_label" v-model="search" autocomplete="off" variant="filled" class="w-full" />
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
                    <div v-for="asset in assets" :key="asset.pk"
                        class="w-48 min-w-48 h-48 border border-black rounded-xl cursor-pointer" @click="clickAsset">
                        <MiniAsset :asset="asset" />
                    </div>
                </div>

            </ScrollPanel>
        </div>
    </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import InputText from 'primevue/inputtext';
import FloatLabel from 'primevue/floatlabel';
import IconField from 'primevue/iconfield';
import InputIcon from 'primevue/inputicon';
import ScrollPanel from 'primevue/scrollpanel';
import Button from 'primevue/button';
import ButtonGroup from 'primevue/buttongroup';
import MiniAsset from '@/components/home/MiniAsset.vue'
import jsonData from '@/dummy.json'
import { useRouter } from 'vue-router'

const selected = ref('opcion1'); // Opción por defecto seleccionada
const search = ref('');
const assets = ref([]);
const router = useRouter()

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

onMounted(() => {
    assets.value = jsonData.filter(item => item.model === 'app.asset')

})

const clickAsset  = () => {
    router.push('/sp500')

}

</script>
