<template>
    <div class="flex justify-center ">
            <div class="grid grid-cols-1 sm:grid-cols-2 gap-8 w-full   justify-items-stretch">
                <div
  v-for="invplanId in invPlanList"
  :key="invplanId"
  class="w-full bg-white shadow-lg rounded-xl"
>
  <PlanDetails :planId="invplanId" />
</div>
            </div>
    </div>
</template>


<script setup>
import { onMounted, ref } from 'vue';
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