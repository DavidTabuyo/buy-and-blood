<template>
  <Card
    class="absolute w-[30rem] overflow-hidden transition-all duration-300"
    :class="{ 'h-auto': expanded, 'h-[50rem]': !expanded }"
  >
    <template #header>
      <img alt="user header" src="/src/assets/criptos.jpg" />
    </template>

    <template #title>Desde Home...</template>

    <template #content>
      <p class="m-0 text-justify">
        <p>Encontrarás la posibilidad de ver los distintos activos y filtraros en función de Fondos o Cryptos.</p>
        <p>Cada uno de los activos dispone de su propia gráfica, con su valor de mercado y su crecimiento o decrecimiento.</p>
        <p>Además, se acompaña con una gráfica circular de una combinación equilibrada para asegurar diversificación y estabilidad.</p>
        <p>Para poder realizar una compra o venta de activos es necesario iniciar sesión. Cada cuenta tiene asociada una cartera propia con cada uno de los activos comprados. </p>
      </p>
    </template>

    <template #footer>
      <div class="absolute inset-x-0 bottom-0 py-4 flex justify-center bg-white">
        <Button
          :label="expanded ? 'Leer más' : 'Leer menos'"
          @click="toggleExpanded"
        />
      </div>
    </template>
  </Card>
</template>

<script setup>
import { ref } from 'vue'
import Card from 'primevue/card'
import Button from 'primevue/button'

const expanded = ref(true)
function toggleExpanded() {
  expanded.value = !expanded.value
}
</script>
