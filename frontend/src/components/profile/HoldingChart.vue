<template>

    <Chart
      type="pie"
      :data="chartData"
      :options="chartOptions"
      class="w-full h-full "
    />
</template>


<script setup>
import { ref, watch, onMounted, defineProps } from 'vue';
import Chart from 'primevue/chart';

import { Chart as ChartJS, ArcElement, Tooltip, Legend } from 'chart.js';
import ChartDataLabels from 'chartjs-plugin-datalabels';

ChartJS.register(ArcElement, Tooltip, Legend, ChartDataLabels);
import { PALETTE } from '@/constants.js'; 

const props = defineProps({
  planName: String,
  holdings: {
    type: Array,
    default: () => []
  },
  percentage_change: Number,
  description: String
});

const chartData = ref({ labels: [], datasets: [] });
const chartOptions = ref({});


const setChartData = () => {
  // 1. Hacemos una copia y la ordenamos de mayor a menor según change_value
  const sorted = [...props.holdings].sort(
    (a, b) => b.change_value - a.change_value
  );

  // 2. Mapear sobre el array ya ordenado
  const labels = sorted.map(
    h => `${h.asset_name} \n ${h.percentage_change.toFixed(2)}%`
  );
  const values = sorted.map(h => h.change_value);

  // 3. Aplicar la paleta a los valores ordenados
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
};

const setChartOptions = () => {
  const textColor = getComputedStyle(document.documentElement)
    .getPropertyValue('--p-text-color')
    .trim() || '#374151';

  return {
    maintainAspectRatio: false,
    layout: {
      padding: { top: 16, bottom: 16, left: 16, right: 16 }
    },
    plugins: {
      datalabels: {
        clip: false,
        anchor: 'center',
        align: 'center',
        offset: 20,
        color: '#fff',
        font: { family: 'Inter, sans-serif', size: 12, weight: '500' },
        backgroundColor: 'rgba(0, 0, 0, 0.7)',
        borderRadius: 8,
        borderColor: '#fff',
        borderWidth: 1,
        padding: 4,
        textStrokeColor: 'rgba(0,0,0,0.3)',
        textStrokeWidth: 1,
        // **Aquí** la clave: ocultar si representan < 5%
        display: ctx => {
          const data = ctx.chart.data.datasets[0].data;
          const total = data.reduce((sum, v) => sum + v, 0);
          const percent = (data[ctx.dataIndex] / total) * 100;
          return percent >= 5;
        },
        formatter: (value, ctx) => ctx.chart.data.labels[ctx.dataIndex]
      },
      legend: { display: false }
    }
  };
};





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
