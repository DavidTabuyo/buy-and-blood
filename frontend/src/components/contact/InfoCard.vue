<template>
    <Card
        style="width: 30rem; left: 10rem; overflow: hidden;"
        class="absolute transition-all duration-300"
        :style="{ height: expanded ? 'auto' : '50rem' }"
    >
    <template #header>
    <img alt="user header" src="/src/assets/future.jpg" />
    </template>
    <template #title>Sobre nosotros</template>
    <template #content>
    <p class="m-0" style="text-align: justify;">
        <br />Buy&Blood es una aplicación de inversión que permite comprar y vender activos financieros, gestionar carteras y acceder a planes de inversión personalizados.<br />
        Su objetivo es simplificar el proceso de inversión, ofreciendo una plataforma accesible y eficiente.<br />
        Dirigida a cualquier persona interesada en invertir, desde principiantes hasta inversores experimentados.<br />
        Buy&Blood soluciona la complejidad de la inversión tradicional mediante una interfaz intuitiva y herramientas que permiten monitorear y optimizar las inversiones de manera sencilla.
    </p>
    </template>
    <template #footer>
    <div
        class="flex justify-center"
        style="position: absolute; bottom: 0; left: 0; right: 0; padding-top: 1rem; padding-bottom: 1rem; background: white;"
    >
    <Button 
        :label="expanded ? 'Leer más' : 'Leer menos'"
        @click="toggleExpanded"
    />
    </div>
    </template>
    </Card>
  </template>
  
  <script setup>
  import { ref } from 'vue';
  import Card from 'primevue/card';
  import Button from 'primevue/button';
  
  const expanded = ref(true);
  
  function toggleExpanded() {
    expanded.value = !expanded.value;
  }
  </script>
  