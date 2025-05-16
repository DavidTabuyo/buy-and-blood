<template>
    <div class="flex justify-center bg-white shadow-lg rounded-xl p-2">
        <ScrollPanel style="width: 100%; height: calc(100vh - 250px)">
            <div class="grid grid-cols-1 sm:grid-cols-2 gap-4 w-full pt-8 pb-8 px-4 justify-items-stretch">
                <div v-for="invplanId in invPlanList" :key="invplanId" class="w-full aspect-video bg-slate-200 shadow-lg rounded-xl">
                    <PlanDetails :planId="invplanId" />
                </div>
            </div>
        </ScrollPanel>

    </div>
</template>


<script setup>
import { onMounted, ref } from 'vue';
import ScrollPanel from 'primevue/scrollpanel';
import axios from '@/axios.js';
import PlanDetails from '@/components/invplan/PlanDetails.vue'

const invPlanList = ref([1, 2, 2, 1, 1, 2]);


const fetchInvPlans = () => {
    axios.get('invplan/list/')
        .then((response) => {
            if (response.data) {
                //invPlanList.value = response.data;
            }
        })
        .catch((error) => {
            console.error('Error al obtener datos:', error);
        });
}

onMounted(() => {
    // Llamar a la función  fetch invPlans cuando el componente se monta
    fetchInvPlans();
});

</script>