<template>
  <Card
    class="absolute w-[30rem] right-[10rem] overflow-hidden transition-all duration-300"
    :class="{ 'h-[37.7rem]': expanded, 'h-[50rem]': !expanded }"
  >
    <template #header>
      <img alt="user header" src="/src/assets/cartera_inversion.jpg" />
    </template>

    <template #title>Desde planes de inversión...</template>

    <template #content>
      <p class="m-0 text-justify">
        <p>Podrás visualizar los planes de inversión de la aplicación.</p>
        <p>Además, se podrá asignar el que más te guste.</p>
        <p>Cada plan incluye información detallada sobre su composición (acciones, ETFs y criptomonedas).</p>
        <p>Gracias a nuestras gráficas, podrás comparar rendimientos históricos y filtraros en función del tiempo.</p>
        <p>Además, podrás crear planes, con una combinación equilibrada entre grandes tecnologías o criptomonedas asociadas como Bitcoin o Ethereum, entre otros muchos.</p>
        <p>Las posibilidades son ilimitadas.</p>
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
