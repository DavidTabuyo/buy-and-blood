<template>
    <div class="flex flex-col px-4 pt-4 pb-4">
        <div class="flex">
            <div class="w-1/2">
                <DayPlanComponent :labels="plan_labels" :values="plan_percentages" :planName="plan_name" />
            </div>
            <div class="w-1/2 flex flex-col gap-6">
                <div>
                    <p class="text-justify">
                        {{ plan_description }}
                    </p>
                </div>
                <div>
                    <Chart type="line" :data="chartData" :options="chartOptions" class="w-full h-full" />
                </div>
                <div v-if="auth.isLoggedIn"  class="flex justify-end">
                    <Button label="Elegir Plan" @click="selectPlan" />
                </div>
            </div>

        </div>


    </div>
    <Toast />

</template>


<script setup>
import { ref, defineProps, watch } from 'vue';
import axios from '@/axios.js';
import 'primeicons/primeicons.css'
import DayPlanComponent from '@/components/utils/DayPlanComponent.vue';
import Button from 'primevue/button';
import Chart from 'primevue/chart';
import Toast from 'primevue/toast';
import { useToast } from 'primevue/usetoast';
import { useAuthStore } from '@/stores/auth'
const auth = useAuthStore()

const toast = useToast();

//variables para el componente con la chart
const plan_description = ref("");
const plan_labels = ref([]);
const plan_percentages = ref([]);
const plan_percentage_change = ref(0);
const plan_name = ref("");


// Recibimos solo el ID del plan
const props = defineProps({
    planId: Number
});

const chartData = ref({
    labels: new Array(12).fill(''),
    datasets: [
        {
            data: [1, 2, 3, 4, 5, 6, 7, 8, 3, 2, 3, 5],
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
            grid: { display: false },
        },
        y: {
            grid: { display: false },
        }
    }
});

const asset = ref(null);

// Función para cargar los datos del asset por ID
const loadData = () => {
    axios.get(`invplan/details/${props.planId}/`)
        .then((response) => {
            if (response.data) {
                plan_description.value = response.data.description;
                plan_labels.value = response.data.labels;
                plan_percentages.value = response.data.percentages;
                plan_percentage_change.value = response.data.percentage_change;
                plan_name.value = response.data.name;
            }
        })
        .catch((error) => {
            console.error('Error al obtener datos:', error);
        });
};

const selectPlan = () => {

    axios.put(`user/set-investing-plan/${props.planId}/`,)
        .then((response) => {
            toast.add({ severity: 'success', summary: 'Cambio realizado correctamente', detail: 'Plan de inversión actualizado', life: 3000 });
        })
        .catch((error) => {
            toast.add({ severity: 'error', summary: 'Error', detail: 'Ya has seleccionado este plan', life: 3000 });
            console.error('Error al obtener datos:', error);
        });
};

// Realizamos el seguimiento del cambio en `invplan` y cargamos los datos
watch(
    () => props.planId,
    () => {
        loadData();
    },
    { immediate: true }
);

</script>