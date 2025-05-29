<template>
  <div class="card flex flex-col justify-start">
    <!-- Contenedor para InputText y SelectButton en una fila -->
    <div class="flex items-center mb-4 gap-4">
      <!-- FloatLabel ocupa todo el espacio restante -->
      <div class="flex-1">
        <FloatLabel variant="on" class="w-full">
          <IconField>
            <InputIcon class="pi pi-search" />
            <InputText id="in_label" v-model="search" autocomplete="off" variant="filled" class="w-full" />
          </IconField>
          <label for="in_label">Buscar activo</label>
        </FloatLabel>
      </div>

      <!-- Con ml-auto, este div se pega al extremo derecho -->
      <div class="ml-auto">
        <ButtonGroup>
          <Button label="Todas" :class="getButtonClass('')" @click="selectOption('')" />
          <Button label="Acciones" :class="getButtonClass('stock')" @click="selectOption('stock')" />
          <Button label="Cryptos" :class="getButtonClass('crypto')" @click="selectOption('crypto')" />
        </ButtonGroup>
      </div>
    </div>

    <div class="flex justify-center grow bg-white  shadow-lg rounded-xl p-2">
      <ScrollPanel style="width: 100%; height: calc(100vh - 250px)">
        
        <div class="grid gap-4 justify-center pt-8 pb-8 px-4 bg-red"
          style="grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); max-width: 1024px; margin: 0 auto;">
          <div v-for="asset in assets" :key="asset.pk"
            class="aspect-square bg-slate-200 shadow-lg rounded-xl cursor-pointer transform transition-transform duration-200 hover:scale-105"
            @click="clickAsset(asset)">
            <MiniAsset :assetId="asset" />
          </div>
        </div>
      </ScrollPanel>
    </div>

    
  </div>
</template>

<script setup>
import { ref, onMounted, watch } from 'vue';
import InputText from 'primevue/inputtext';
import FloatLabel from 'primevue/floatlabel';
import IconField from 'primevue/iconfield';
import InputIcon from 'primevue/inputicon';
import ScrollPanel from 'primevue/scrollpanel';
import Button from 'primevue/button';
import ButtonGroup from 'primevue/buttongroup';
import MiniAsset from '@/components/home/MiniAsset.vue'
import { useRouter } from 'vue-router'
import axios from '@/axios.js';

const selected = ref(''); // Opción por defecto seleccionada
const search = ref('');
const assets = ref([]);
const router = useRouter()

const selectOption = (option) => {
  selected.value = option;
  fetchAssets(); // Llamar a la función de búsqueda cuando se cambia la opción seleccionada
};

// Función para asignar clases dinámicamente
const getButtonClass = (option) => {
  return {
    'p-button-primary': selected.value === option, // Color cuando está seleccionado
    'p-button-outlined': selected.value !== option // Color por defecto
  };
};

const clickAsset = (asset_id) => {
  router.push(`/asset/${asset_id}`)
}

// Función para obtener activos según los filtros
const fetchAssets = () => {
  axios.get('asset/list/', {
    params: {
      type: selected.value,
      search: search.value
    }
  })
    .then((response) => {
      if (response.data) {
        assets.value = response.data;
      }
    })
    .catch((error) => {
      console.error('Error al obtener datos:', error);
    });
}

onMounted(() => {
  // Llamar a la función fetchAssets cuando el componente se monta
  fetchAssets();
});

watch(search, () => {
  fetchAssets();
});
</script>
