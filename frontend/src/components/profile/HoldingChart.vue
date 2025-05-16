<template>
    <Chart
      ref="myChart"
      type="pie"
      :data="chartData"
      :options="chartOptions"
    />
</template>
  
  <script setup>
  import { ref, watch, onMounted, onBeforeUnmount, defineProps } from 'vue';
  import Chart from 'primevue/chart';
  import PercentageChange from '@/components/utils/PercentageChange.vue';
  
  const props = defineProps({
    planName: String,
    holdings: {
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
    let labels = props.holdings.map(holding => holding.label);
    let values = props.holdings.map(holding => holding.percentage);
    return {
      labels: labels,
      datasets: [
        {
          data: values,
          backgroundColor: PALETTE.slice(0, props.holdings.length),
          hoverBackgroundColor: PALETTE.slice(0, props.holdings.length)
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

  // Inicialización
  onMounted(() => {
    chartData.value = setChartData();
    chartOptions.value = setChartOptions();
  });
  
  // Watchers para actualizar datos si cambian los props
  watch(
    () => props.holdings,
    () => {
      chartData.value = setChartData();
      // Forzar actualización del chart
      if (myChart.value?.chart) {
        myChart.value.chart.data = chartData.value;
        myChart.value.chart.update();
      }
    }
  );
  </script>
  