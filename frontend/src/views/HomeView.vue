<template>
    <div>
        <div class="flex gap-8">
            <MainComponent class="w-2/3" />
            <div class="bg-white shadow-lg rounded-xl w-1/3 ">
                <div class="pt-8 flex flex-col items-center">
                    <DayPlanComponent  />
                </div>

            </div>
        </div>
    </div>
</template>


<script setup>

import { ref } from 'vue';
import MainComponent from '@/components/home/MainComponent.vue';
import DayPlanComponent from '@/components/utils/DayPlanComponent.vue';
import Tag from 'primevue/tag';
const value = ref(null);
</script>
