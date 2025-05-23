<template>
  <Card
    class="absolute w-[30rem] overflow-hidden transition-all duration-300"
    :class="{ 'h-auto': expanded, 'h-[50rem]': !expanded }"
  >
    <template #header>
      <img alt="user header" src="/src/assets/criptos.jpg" />
    </template>

    <template #title>Segundo cuadro info</template>

    <template #content>
      <p class="m-0 text-justify">
        <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.</p>
        <p>Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.</p>
        <p>Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur.</p>
        <p>Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.</p>
        <p>Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.</p>
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
