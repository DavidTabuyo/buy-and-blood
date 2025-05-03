<template>

  <div class="text-4xl ">PLAN DEL DÍA</div>
  <div class="card flex flex-col items-center overflow-hidden max-w-full mt-4">
    <div class="relative w-full max-w-[30rem] aspect-square">

      <Chart ref="myChart" type="doughnut" :data="chartData" :options="chartOptions" class="w-full h-full" />

      <div class="absolute inset-0 flex items-center justify-center pointer-events-none">
        <PercentageChange :value="1.5" class="text-3xl " />
      </div>
    </div>


    <p class="mt-4 text-center text-sm text-gray-600 px-8">
      Esta gráfica representa la distribución de recursos entre las distintas categorías.
      Esta gráfica representa la distribución de recursos entre las distintas categorías.
      Esta gráfica representa la distribución de recursos entre las distintas categorías.
      Esta gráfica representa la distribución de recursos entre las distintas categorías.
    </p>
  </div>
</template>




<script setup>
import { onMounted, onBeforeUnmount, ref } from 'vue';
import Chart from 'primevue/chart';
import PercentageChange from './PercentageChange.vue';

const myChart = ref(null);

onMounted(() => {
  chartData.value = setChartData();
  chartOptions.value = setChartOptions();
});

const chartData = ref();
const chartOptions = ref(null);

const setChartData = () => {
  const documentStyle = getComputedStyle(document.body);

  return {
    labels: ['MSCI WORLD', 'B', 'C'],
    datasets: [
      {
        data: [540, 325, 702],
        backgroundColor: [
          '#FFC0CB', // Light Pink
          '#FFB6C1', // Light Pink 2
          '#FF69B4', // Hot Pink
          '#FF1493', // Deep Pink
          '#DB7093'  // Pale Violet Red
        ]
      }
    ]
  };
};

function setChartOptions() {
  const textColor = getComputedStyle(document.documentElement)
    .getPropertyValue('--p-text-color') || '#374151';

  return {
    responsive: true,
    maintainAspectRatio: false,

    hover: {
      mode: null
    },
    events: [],

    elements: {
      arc: {
        hoverOffset: 0
      }
    },

    plugins: {
      legend: { display: false },

      datalabels: {
        color: '#fff',
        font: {
          family: 'Inter, sans-serif',
          size: 16,
          weight: '600'
        },
        backgroundColor: 'rgba(0, 0, 0, 0.7)',
        borderRadius: 10,
        borderColor: '#ffffff',
        borderWidth: 2,
        padding: 8,
        textStrokeColor: 'rgba(0,0,0,0.3)',
        textStrokeWidth: 1,
        align: 'center',
        anchor: 'center',
        formatter: (value, ctx) => {
          const label = ctx.chart.data.labels[ctx.dataIndex].toUpperCase();
          return `${label}\n${value}%`;
        }
      }
    }
  };
}







const handleResize = () => {
  if (myChart.value?.chart) {
    myChart.value.chart.resize(); // Forzar redimensionamiento
  }
};

onMounted(() => {
  window.addEventListener('resize', handleResize);
});

onBeforeUnmount(() => {
  window.removeEventListener('resize', handleResize);
});

</script>
