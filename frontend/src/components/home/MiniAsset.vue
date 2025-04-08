<template>
    <div class="flex justify-between px-4 pt-2">
      <h1 class="text-2xl text-gray-500" v-if="asset && asset.fields">
        {{ asset.fields.symbol }}
      </h1>
    </div>
    <div class="px-4">
      <h1 v-if="asset && asset.fields" class="text-2xl">${{ asset.fields.price }}</h1>
    </div>
    <div class="px-4"  v-if="asset && asset.fields">
        <PercentageChange :value="asset.fields.day_variation"></PercentageChange>
    </div>
    <div >
      <Chart type="line" :data="chartData" :options="chartOptions"  />
    </div>
  </template>
  
  <script setup>
  import { ref, defineProps, watch } from 'vue';
  import Chart from 'primevue/chart';
  import PercentageChange from '@/components/utils/PercentageChange.vue'

  const props = defineProps({
    asset: Object
  });
  const asset = ref(null);
  
  watch(
    () => props.asset,
    (newAsset) => {
      asset.value = newAsset;
      console.log(asset.value);
    },
    { deep: true, immediate: true }
  );
  
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
  </script>
  