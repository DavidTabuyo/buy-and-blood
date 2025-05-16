<template>
    <div class="flex justify-center bg-white shadow-lg rounded-xl p-2">
        <ScrollPanel style="width: 100%; height: calc(100vh - 250px)">
            <div class="grid gap-4 justify-center pt-8 pb-8 px-4"
                    style="grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); max-width: 1024px; margin: 0 auto;">
                    <div v-for="invplanId in invPlanList" 
                        class="aspect-square bg-slate-200 shadow-lg rounded-xl cursor-pointer transform transition-transform duration-200 hover:scale-105">
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

const invPlanList = ref([]);


const fetchInvPlans = () => {
    axios.get('invplan/list/')
    .then((response) => {
        if (response.data) {
            invPlanList.value = response.data;
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