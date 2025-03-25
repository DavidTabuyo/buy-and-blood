<template>
  <div>
    <h1>
      Plan del día
    </h1>
  </div>
  <div class="card flex justify-center">
    <Chart
      type="doughnut"
      :data="chartData"
      :options="chartOptions"
      :plugins="[centerTextPlugin, dataLabelsPlugin]"
      class="w-full md:w-[30rem]"
    />
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import Chart from 'primevue/chart';
import dataLabelsPlugin from 'chartjs-plugin-datalabels';

// Plugin personalizado para texto en el centro
const centerTextPlugin = {
  id: 'centerText',
  afterDatasetsDraw(chart) {
    const { ctx, chartArea: { top, bottom, left, right } } = chart;
    const options = chart.config.options.plugins.centerText || {};
    if (!options.text) return;

    const centerX = (left + right) / 2;
    const centerY = (top + bottom) / 2;

    ctx.save();
    ctx.fillStyle = options.color || '#fff';
    ctx.font = options.font || 'bold 20px sans-serif';
    ctx.textAlign = 'center';
    ctx.textBaseline = 'middle';
    ctx.fillText(options.text, centerX, centerY);
    ctx.restore();
  }
};

const chartData = ref(null);
const chartOptions = ref(null);

onMounted(() => {
  chartData.value = setChartData();
  chartOptions.value = setChartOptions();
});

function setChartData() {
  return {
    labels: ['China', 'Emerging', 'MSCI World'],
    datasets: [
      {
        data: [20, 30, 50],
        backgroundColor: ['#0099cc', '#ff9900', '#999999'],
        borderColor: '#fff',
        borderWidth: 2
      }
    ]
  };
}

function setChartOptions() {
  return {
    // Reduce el valor para hacer el hueco más pequeño
    cutout: '40%',
    plugins: {
      title: {
        display: true,
        text: 'Plan del día',
        color: '#fff',
        font: { size: 18 }
      },
      legend: { 
        display: false 
      },
      centerText: {
        text: '▲ 0.4%',
        color: '#fff',
        font: 'bold 30px sans-serif'
      },
      datalabels: {
        color: '#fff',
        font: { size: 16, weight: 'bold' },
        textAlign: 'center',
        // Poner el porcentaje debajo del nombre
        formatter: (value, ctx) => {
          const label = ctx.chart.data.labels[ctx.dataIndex];
          return `${label}\n${value}%`;
        }
      }
    }
  };
}
</script>
