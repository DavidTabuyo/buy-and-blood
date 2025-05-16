<template>
    <div class="flex flex-col h-full">

    </div>
</template>


<script setup>
import { ref, defineProps, watch } from 'vue';
import axios from '@/axios.js';
import 'primeicons/primeicons.css'

// Recibimos solo el ID del plan
const props = defineProps({
    planId: Number 
});


const asset = ref(null);

// Función para cargar los datos del asset por ID
const loadData = () => {
    axios.get(`asset/mini/${props.assetId}/`)
        .then((response) => {
            if (response.data) {
                console.log(response.data);
                asset.value = response.data;  // Asignamos los datos recibidos a `asset`
                if (response.data.last_values) {
                    const isPositive = response.data.percentage_change >= 0;
                    const borderColor = isPositive ? "rgba(75, 192, 192, 1)" : "rgba(255, 99, 132, 1)"; // verde o rojo
                    const backgroundColor = isPositive ? "rgba(75, 192, 192, 0.2)" : "rgba(255, 99, 132, 0.2)";

                    chartData.value.datasets[0] = {
                        data: response.data.last_values,
                        borderColor,
                        backgroundColor,
                        fill: true,
                        tension: 0.4
                    };
                }
                if (response.data.type === "crypto") {
                    icon.value = "pi pi-bitcoin";
                } else if (response.data.type === "stock") {
                    icon.value = "pi pi-chart-line";

                }
            }
        })
        .catch((error) => {
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