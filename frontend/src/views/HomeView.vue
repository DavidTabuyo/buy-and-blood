<template>
    <div>
        <h1>Bienvenido a la Página de Inicio</h1>
        <div style="margin-top: 100px;">
            <MainComponent></MainComponent>
        </div>
    </div>
</template>

<script setup>

import { ref } from 'vue';
import MainComponent from '@/components/home/MainComponent.vue';

const value = ref(null);
</script>
