<template>
    <div>
        <div class="flex">
            <MainComponent class="w-2/3" />
            <DayPlanComponent class="w-1/3" />
        </div>
    </div>
</template>


<script setup>

import { ref } from 'vue';
import MainComponent from '@/components/home/MainComponent.vue';
import DayPlanComponent from '@/components/home/DayPlanComponent.vue';

const value = ref(null);
</script>
