<template>
  <Card>
    <template #header>
      <img alt="user header" src="/src/assets/cartera_inversion.jpg" />
    </template>

    <template #title>Desde planes de inversión...</template>

    <template #content>
      <p class="m-0 text-justify">
        <span class="block mt-4">Podrás visualizar los planes de inversión de la aplicación.</span>
        <span class="block mt-4">Además, se podrá asignar el que más te guste.</span>
        <span class="block mt-4">Cada plan incluye información detallada sobre su composición (acciones, ETFs y criptomonedas).</span>
        <span class="block mt-4">Gracias a nuestras gráficas, podrás comparar rendimientos históricos y filtrarlos en función del tiempo.</span>
        <span class="block mt-4">Además, podrás crear planes, con una combinación equilibrada entre grandes tecnologías o criptomonedas asociadas como Bitcoin o Ethereum, entre otros muchos.</span>
        <span class="block mt-4">Las posibilidades son ilimitadas.</span>
      </p>
    </template>
  </Card>
</template>

<script setup>
import Card from 'primevue/card'
</script>
