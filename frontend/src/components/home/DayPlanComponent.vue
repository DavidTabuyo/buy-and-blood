<template>
  <div class="card flex justify-center">
    <Chart type="doughnut" :data="chartData" :options="chartOptions" class="w-full md:w-[30rem]" />
  </div>
</template>

<script setup>
import { ref, onMounted } from "vue";
import Chart from 'primevue/chart';

onMounted(() => {
  chartData.value = setChartData();
  chartOptions.value = setChartOptions();
});

const chartData = ref();
const chartOptions = ref(null);

const setChartData = () => {
  const documentStyle = getComputedStyle(document.body);

  return {
    labels: ['A', 'B', 'C'],
    datasets: [
      {
        data: [540, 325, 702],
        backgroundColor: [
          '#f4b2cc', // Rosa pastel
          '#c89eff', // Lila pastel
          '#add8e6', // Verde pastel
          '#fff1b8', // Amarillo pastel
          '#add8e6'  // Azul pastel
        ], hoverBackgroundColor: [
          '#f7c1d5', // Rosa pastel hover (más suave)
          '#d0a8ff', // Lila pastel hover (más suave)
          '#c4e6f1', // Verde pastel hover (más suave)
          '#fff7d1', // Amarillo pastel hover (más suave)
          '#c4e6f1'  // Azul pastel hover (más suave)
        ]
      }
    ]
  };
};

const setChartOptions = () => {
  const documentStyle = getComputedStyle(document.documentElement);
  const textColor = documentStyle.getPropertyValue('--p-text-color');

  return {
    plugins: {
      legend: {
        labels: {
          cutout: '60%',
          color: textColor
        }
      }
    }
  };
};
</script>
