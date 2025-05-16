<template>
  <div class="flex flex-col h-full">
    <div class="flex justify-between px-4 pt-4">
      <h1 class="text-2xl text-gray-500" v-if="asset">
        {{ asset.name }}
      </h1>
      <i :class="icon" style="font-size: 2rem"></i>

    </div>

    <div class="px-4">
      <DolarValue v-if="asset" :value="asset.price" class="text-2xl" />
    </div>

    <div class="px-4" v-if="asset">
      <PercentageChange :value="asset.percentage_change" />
    </div>

    <div class="flex-grow p-4">
      <Chart type="line" :data="chartData" :options="chartOptions" class="w-full h-full" />
    </div>
  </div>
</template>


<script setup>
import { ref, defineProps, watch } from 'vue';
import Chart from 'primevue/chart';
import PercentageChange from '@/components/utils/PercentageChange.vue';
import DolarValue from '@/components/utils/DolarValue.vue';
import axios from '@/axios.js';
import 'primeicons/primeicons.css'

// Recibimos solo el ID del asset
const props = defineProps({
  assetId: Number
});

const asset = ref(null);
const icon = ref("");
const chartData = ref({
  labels: [],
  datasets: [
    {
      data: [],
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
    },
    datalabels: {
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
  axios.get(`asset/mini/${props.assetId}/`)
    .then((response) => {
      if (response.data) {
        asset.value = response.data;  // Asignamos los datos recibidos a `asset`
        if (response.data.last_values) {
          const isPositive = response.data.percentage_change >= 0;
          const borderColor = isPositive ? "rgba(75, 192, 192, 1)" : "rgba(255, 99, 132, 1)"; // verde o rojo
          const backgroundColor = isPositive ? "rgba(75, 192, 192, 0.2)" : "rgba(255, 99, 132, 0.2)";

          chartData.value.datasets[0] = {
            data: response.data.last_values,
            borderColor,
            backgroundColor,
            fill: true,
            tension: 0.4
          };
        }
        if (response.data.type === "crypto") {
          icon.value = "pi pi-bitcoin";
          chartData.value.labels = new Array(24).fill('');
        } else if (response.data.type === "stock") {
          icon.value = "pi pi-chart-line";
          // TODO: Cambiar a 7 o 6 días?
          chartData.value.labels = new Array(7).fill('');
        }
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
