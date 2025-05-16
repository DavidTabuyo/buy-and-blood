<template>
    <Card
      style="width: 30rem; overflow: hidden;"
      class="absolute transition-all duration-300"
      :style="{ height: expanded ? 'auto' : '50rem' }"
    >
      <template #header>
        <img alt="user header" src="/src/assets/future.jpg" />
      </template>
      <template #title>Segundo cuadro info</template>
      <template #content>
        <p class="m-0" style="text-align: justify;">
          <br />
          Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.<br />
          Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.<br />
          Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur.<br />
          Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.<br />
          Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.<br />
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
  