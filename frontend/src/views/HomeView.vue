<template>
    <div>
        <h1>Bienvenido a la Página de Inicio</h1>
        <div class="mt-24">
            <MainComponent></MainComponent>
            <DayPlanComponent></DayPlanComponent>
        </div>
    </div>
</template>

<script setup>

import { ref } from 'vue';
import MainComponent from '@/components/home/MainComponent.vue';
import DayPlanComponent from '@/components/home/DayPlanComponent.vue';

const value = ref(null);
</script>
