<template>
    <div>
        <div class="flex gap-8">
            <MainComponent class="w-2/3" />
            <div class="bg-white shadow-lg rounded-xl w-1/3 ">
                <div class="pt-8 flex flex-col items-center">
                    <DayPlanComponent :description="planDescription" :labels="plan_labels" :values="plan_values" :planName="plan_name
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
const planDescription = ref("");
const plan_labels = ref([]);
const plan_values = ref([]);
const plan_percentage_change = ref();
const plan_name = ref("");


const loadDayPlanData = () => {
    axios.get("invplan/best/")
        .then((response) => {
            if (response.data) {
                console.log(response.data);
                planDescription.value = response.data.description;
                plan_labels.value = response.data.labels;
                plan_values.value = response.data.values;
                plan_percentage_change.value = response.data.percentage_change;
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
