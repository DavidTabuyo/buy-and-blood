<template>
  <Card>
    <template #header>
      <img alt="user header" src="/src/assets/criptos.jpg" />
    </template>

    <template #title>Desde Home...</template>

    <template #content>
      <p class="m-0 text-justify">
        <span class="block mt-4">Encontrarás la posibilidad de ver los distintos activos y filtrarlos en función de Fondos o Cryptos.</span>
        <span class="block mt-4">Cada uno de los activos dispone de su propia gráfica, con su valor de mercado y su crecimiento o decrecimiento.</span>
        <span class="block mt-4">Además, se acompaña con una gráfica circular de una combinación equilibrada para asegurar diversificación y estabilidad.</span>
        <span class="block mt-4">Para poder realizar una compra o venta de activos es necesario iniciar sesión.</span>
        <span class="block mt-4">Cada cuenta tiene asociada una cartera propia con cada uno de los activos comprados.</span>
      </p>
    </template>
  </Card>
</template>

<script setup>
import Card from 'primevue/card'
</script>
