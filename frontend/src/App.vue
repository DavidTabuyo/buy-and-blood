<script setup>
import NavBar from '@/components/NavBar.vue';
</script>

<template>
  <div class="flex flex-col h-screen">
    <!-- Barra de navegación -->
    <div>
      <NavBar></NavBar>
    </div>

    <!-- Contenido principal -->
    <div class="flex-1  pt-24 px-16 pb-16">
      <router-view class="h-full"></router-view>
    </div>
  </div>
</template>


<style scoped>
.logo {
  height: 6em;
  padding: 1.5em;
  will-change: filter;
  transition: filter 300ms;
}

.logo:hover {
  filter: drop-shadow(0 0 2em #646cffaa);
}

.logo.vue:hover {
  filter: drop-shadow(0 0 2em #42b883aa);
}
</style>
