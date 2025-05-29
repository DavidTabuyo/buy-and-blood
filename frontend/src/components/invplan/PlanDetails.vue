<template>
    <div class="flex flex-col px-4 pt-4 pb-4">
      <div class="flex">
        <div class="w-1/2">
          <DayPlanComponent
            :percentage_change="plan_percentage_change"
            :labels="plan_labels"
            :values="plan_percentages"
            :planName="plan_name"
          />
        </div>
        <div class="w-1/2 flex flex-col gap-6">
          <div>
            <p class="text-justify">
              {{ plan_description }}
            </p>
          </div>
          <div>
            <Chart
              type="line"
              :data="chartData"
              :options="chartOptions"
              class="w-full h-full"
            />
          </div>
          <div v-if="auth.isLoggedIn" class="flex justify-end">
            <!-- Solo mostramos "Elegir Plan" si el usuario tiene otro plan -->
            <Button
              v-if="Number(auth.user_data.plan_id) !== planId"
              label="Elegir Plan"
              @click="selectPlan"
            />
            <!-- Si ya es ese plan, mostramos mensaje deshabilitado -->
            <Button
              v-else
              label="Plan seleccionado"
              disabled
            />
          </div>
        </div>
      </div>
    </div>
    <Toast />
  </template>
  
  <script setup>
  import { ref, watch } from 'vue';
  import axios from '@/axios.js';
  import 'primeicons/primeicons.css';
  import DayPlanComponent from '@/components/utils/DayPlanComponent.vue';
  import Button from 'primevue/button';
  import Chart from 'primevue/chart';
  import Toast from 'primevue/toast';
  import { useToast } from 'primevue/usetoast';
  import { useAuthStore } from '@/stores/auth';
  
  const auth = useAuthStore();
  const toast = useToast();
  
  // Desestructuramos el prop para poder usar planId directamente
  const { planId } = defineProps({
    planId: { type: Number, required: true }
  });
  
  // Datos del plan
  const plan_description = ref('');
  const plan_labels = ref([]);
  const plan_percentages = ref([]);
  const plan_percentage_change = ref(0);
  const plan_name = ref('');
  
  // Configuración del gráfico
  const chartData = ref({
    labels: new Array(12).fill(''),
    datasets: [
      {
        data: [1,2,3,4,5,6,7,8,3,2,3,5],
        borderColor: 'rgba(75, 192, 192, 1)',
        backgroundColor: 'rgba(75, 192, 192, 0.2)',
        fill: true,
        tension: 0.4
      }
    ]
  });
  const chartOptions = ref({
    responsive: true,
    plugins: {
      legend: { display: false },
      datalabels: { display: false }
    },
    scales: {
      x: { grid: { display: false } },
      y: { grid: { display: false } }
    }
  });
  
  // Carga los datos del plan por ID
  function loadData() {
    axios.get(`invplan/details/${planId}/`)
      .then(response => {
        const data = response.data;
        plan_description.value = data.description;
        plan_labels.value = data.labels;
        plan_percentages.value = data.percentages;
        plan_percentage_change.value = data.planPercentageChange;
        plan_name.value = data.name;
      })
      .catch(err => {
        console.error('Error al obtener datos:', err);
      });
  }
  
  // Seleccionar el plan
  function selectPlan() {
    axios.put(`user/set-investing-plan/${planId}/`)
      .then(() => {
        auth.user_data.plan_id=planId;
        toast.add({
          severity: 'success',
          summary: 'Cambio realizado correctamente',
          detail: 'Plan de inversión actualizado',
          life: 3000
        });
      })
      .catch(err => {
        toast.add({
          severity: 'error',
          summary: 'Error',
          detail: 'Ya has seleccionado este plan',
          life: 3000
        });
        console.error('Error al seleccionar plan:', err);
      });
  }
  
  // Recarga los datos cuando cambie planId (e inmediatamente al montar)
  watch(
    () => planId,
    loadData,
    { immediate: true }
  );
  </script>
  
  <style scoped>
  .tradingview-widget-container {
    width: 100%;
    height: 100%;
  }
  </style>
  