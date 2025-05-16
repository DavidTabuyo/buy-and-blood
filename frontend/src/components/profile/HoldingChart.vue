<template>
  <!-- Aquí el wrapper cuadrado: ancho 100%, relación 1:1 -->
    <!-- El Chart ocupa todo ese cuadrado -->
    <Chart
      type="pie"
      :data="chartData"
      :options="chartOptions"
      class="w-full h-full"
    />
</template>


<script setup>
import { ref, watch, onMounted, defineProps } from 'vue';
import Chart from 'primevue/chart';

import { Chart as ChartJS, ArcElement, Tooltip, Legend } from 'chart.js';
import ChartDataLabels from 'chartjs-plugin-datalabels';

ChartJS.register(ArcElement, Tooltip, Legend, ChartDataLabels);

// 2. Props
const props = defineProps({
  planName: String,
  holdings: {
    type: Array,
    default: () => []
  },
  percentage_change: Number,
  description: String
});

// 3. Reactivos para datos y opciones
const chartData = ref({ labels: [], datasets: [] });
const chartOptions = ref({});

// 4. Paleta de colores
const PALETTE = [
  '#FFC0CB', // Light Pink
  '#FFB6C1', // Light Pink 2
  '#FF69B4', // Hot Pink
  '#FF1493', // Deep Pink
  '#DB7093'  // Pale Violet Red
];

// 5. setChartData tal como antes, usando labels y values dinámicos
function setChartData() {
  const labels = props.holdings.map(h => h.asset);
  const values = props.holdings.map(h => h.change_value);
  const colors = PALETTE.slice(0, values.length);

  return {
    labels,
    datasets: [
      {
        data: values,
        backgroundColor: colors,
        hoverBackgroundColor: colors
      }
    ]
  };
}

// 6. Tu setChartOptions completo
function setChartOptions() {
  const textColor =
    getComputedStyle(document.documentElement)
      .getPropertyValue('--p-text-color')
      .trim() || '#374151';

  return {
    maintainAspectRatio: false,
    
    plugins: {
      datalabels: {
        color: '#fff',
        font: { family: 'Inter, sans-serif', size: 16, weight: '600' },
        backgroundColor: 'rgba(0, 0, 0, 0.7)',
        borderRadius: 10,
        borderColor: '#ffffff',
        borderWidth: 2,
        padding: 8,
        textStrokeColor: 'rgba(0,0,0,0.3)',
        textStrokeWidth: 1,
        align: 'center',
        anchor: 'center',
      },
      legend: { display: true, position: 'bottom', labels: { color: textColor } }
    }
  };
}

// 7. Iniciar datos y opciones al montar
onMounted(() => {
  chartOptions.value = setChartOptions();
});

// 8. Actualizar datos si cambian las holdings
watch(
  () => props.holdings,
  () => {
    chartData.value = setChartData();
  },
  { deep: true }
);
</script>
