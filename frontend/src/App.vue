<script setup>
import NavBar from '@/components/NavBar.vue';
</script>

<template>
  <div>
    <div>
    <NavBar></NavBar>
  </div>
  <div class="h-full pt-24 px-16 pb-16">
      <router-view></router-view>
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
