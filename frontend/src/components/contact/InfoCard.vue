<template>
  <Card
    class="absolute w-[30rem] left-[10rem] overflow-hidden transition-all duration-300"
    :class="{ 'h-[37.7rem]': expanded, 'h-[50rem]': !expanded }"
  >
    <template #header>
      <img alt="user header" src="/src/assets/future.jpg" />
    </template>

    <template #title>Sobre nosotros</template>

    <template #content>
      <p class="m-0 text-justify">
        <p>Buy&Blood es una aplicación de inversión que permite comprar y vender activos financieros, gestionar carteras y acceder a planes de inversión personalizados.</p>
        <p>Su objetivo es simplificar el proceso de inversión, ofreciendo una plataforma accesible y eficiente.</p>
        <p>Dirigida a cualquier persona interesada en invertir, desde principiantes hasta inversores experimentados.</p>
        <p>Buy&Blood soluciona la complejidad de la inversión tradicional mediante una interfaz intuitiva y herramientas que permiten monitorear y optimizar las inversiones de manera sencilla.</p>
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
