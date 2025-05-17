<template>
    <div>
        <div class="flex gap-8">
            <MainComponent class="w-2/3" />
            <div class="bg-white shadow-lg rounded-xl w-1/3 ">
                <div class="pt-8 flex flex-col items-center">
                    <DayPlanComponent :percentage_change="plan_percentage_change" :description="plan_description" :labels="plan_labels" :values="plan_percentages" :planName="plan_name
                        " />
                </div>

            </div>
        </div>
    </div>
</template>


<script setup>

import { onMounted, ref } from 'vue';
import MainComponent from '@/components/home/MainComponent.vue';
import DayPlanComponent from '@/components/utils/DayPlanComponent.vue';
import axios from '@/axios.js';
const plan_description = ref("");
const plan_labels = ref([]);
const plan_percentages = ref([]);
const plan_percentage_change = ref(0);
const plan_name = ref("");


const loadDayPlanData = () => {
    axios.get("invplan/details/1/")
        .then((response) => {
            if (response.data) {
                plan_description.value = response.data.description;
                plan_labels.value = response.data.labels;
                plan_percentages.value = response.data.percentages;
                plan_percentage_change.value = response.data.planPercentageChange;
                plan_name.value = response.data.name;
            };
        })
        .catch((error) => {
            console.error('Error al obtener datos:', error);
        });
};

onMounted(() => {
    loadDayPlanData()
});

</script>
