<template>
  <div class="flex flex-col h-full">
    <div class="flex justify-between px-4 pt-4">
      <h1 class="text-2xl text-gray-500" v-if="asset && asset.fields">
        {{ asset.fields.symbol }}
      </h1>
    </div>

    <div class="px-4">
      <h1 v-if="asset && asset.fields" class="text-2xl">${{ asset.fields.price }}</h1>
    </div>

    <div class="px-4" v-if="asset && asset.fields">
      <PercentageChange :value="asset.fields.day_variation" />
    </div>

    <div class="flex-grow p-4">
      <Chart type="line" :data="chartData" :options="chartOptions" class="w-full h-full" />
    </div>
  </div>
</template>

  
<script setup>
import { ref, defineProps, watch } from 'vue';
import Chart from 'primevue/chart';
import PercentageChange from '@/components/utils/PercentageChange.vue'
import axios from '@/axios.js';

// Recibimos solo el ID del asset
const props = defineProps({
  assetId: Number // Cambia el nombre del prop a assetId
});

const asset = ref(null);

const chartData = ref({
  labels: ["", "", "", "", "", "", ""],
  datasets: [
    {
      data: [10, 20, 15, 25, 30, 22, 18],
      borderColor: "rgba(75, 192, 192, 1)",
      backgroundColor: "rgba(75, 192, 192, 0.2)",
      fill: true,
      tension: 0.4
    }
  ]
});

const chartOptions = ref({
  responsive: true,
  plugins: {
    legend: {
      display: false
    }
  },
  scales: {
    x: {
      ticks: { display: false },
      grid: { display: false },
      border: { display: false }
    },
    y: {
      ticks: { display: false },
      grid: { display: false },
      border: { display: false }
    }
  }
});

// Función para cargar los datos del asset por ID
const loadData = () => {
  // Utilizamos `props.assetId` para hacer la solicitud GET
  axios.get(`asset/mini/${props.assetId}`)
    .then((response) => {
      if (response.data) {
        asset.value = response.data;  // Asignamos los datos recibidos a `asset`
      }
    })
    .catch((error) => {
      console.error('Error al obtener datos:', error);
    });
};

// Realizamos el seguimiento del cambio en `assetId` y cargamos los datos
watch(
  () => props.assetId,
  (newAssetId) => {
    loadData();  // Cargamos los datos cada vez que cambia el `assetId`
  },
  { immediate: true } // Llamamos a `loadData` inmediatamente al montar
);
</script>
