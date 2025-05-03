<template>
  <div class="flex flex-col items-center space-y-6">
    <div class="text-4xl">{{ props.planName }}</div>

    <div class="card flex flex-col items-center overflow-hidden max-w-full mt-4">
      <div class="relative w-full max-w-[30rem] aspect-square">
        <Chart
          ref="myChart"
          type="doughnut"
          :data="chartData"
          :options="chartOptions"
          class="w-full h-full"
        />

        <div
          class="absolute inset-0 flex items-center justify-center pointer-events-none"
        >
          <PercentageChange
            :value="1.5"
            class="text-3xl font-bold"
          />
        </div>
      </div>

      <p class="mt-4 text-center text-sm text-gray-600 px-8">
        {{ props.description }}
      </p>
    </div>
  </div>
</template>

<script setup>
import { ref, watch, onMounted, onBeforeUnmount, defineProps } from 'vue';
import Chart from 'primevue/chart';
import PercentageChange from '@/components/utils/PercentageChange.vue';

const props = defineProps({
  planName: String,
  labels: {
    type: Array,
    default: () => []
  },
  values: {
    type: Array,
    default: () => []
  },
  percentage_change: Number,
  description: String
});

const myChart = ref(null);
const chartData = ref({});
const chartOptions = ref({});

const PALETTE = [
  '#FFC0CB', // Light Pink
  '#FFB6C1', // Light Pink 2
  '#FF69B4', // Hot Pink
  '#FF1493', // Deep Pink
  '#DB7093'  // Pale Violet Red
];

function setChartData() {
  return {
    labels: props.labels,
    datasets: [
      {
        data: props.values,
        backgroundColor: PALETTE.slice(0, props.values.length),
        hoverBackgroundColor: PALETTE.slice(0, props.values.length)
      }
    ]
  };
}

function setChartOptions() {
  const textColor =
    getComputedStyle(document.documentElement).getPropertyValue(
      '--p-text-color'
    ) || '#374151';

  return {
    responsive: true,
    maintainAspectRatio: false,
    hover: { mode: null },
    events: [],
    elements: { arc: { hoverOffset: 0 } },
    plugins: {
      legend: { display: false },
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
        formatter: (value, ctx) => {
          const label = ctx.chart.data.labels[ctx.dataIndex].toUpperCase();
          const total = ctx.chart.data.datasets[0].data.reduce(
            (sum, v) => sum + v,
            0
          );
          const pct = ((value / total) * 100).toFixed(1) + '%';
          return `${label}\n${pct}`;
        }
      }
    }
  };
}

function resizeChart() {
  if (myChart.value?.chart) {
    myChart.value.chart.resize();
  }
}

// Inicialización
onMounted(() => {
  chartData.value = setChartData();
  chartOptions.value = setChartOptions();
  window.addEventListener('resize', resizeChart);
});

// Watchers para actualizar datos si cambian los props
watch(
  () => [props.labels, props.values],
  () => {
    chartData.value = setChartData();
    // Forzar actualización del chart
    if (myChart.value?.chart) {
      myChart.value.chart.data = chartData.value;
      myChart.value.chart.update();
    }
  },
  { deep: true }
);

onBeforeUnmount(() => {
  window.removeEventListener('resize', resizeChart);
});
</script>
