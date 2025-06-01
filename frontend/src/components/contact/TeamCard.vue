<template>
  <div class="flex justify-between p-16">
    <div class="flex flex-col border border-primary-200 shadow-lg
               justify-center items-center w-80 h-100 rounded-2xl p-8 gap-4">
      <img src="/src/assets/david.jpg" alt="Foto de perfil" class="w-40 h-40 rounded-full object-cover">
      <span class="text-2xl font-medium">David Tabuyo</span>
      <span class="text-muted-color text-center">
        FullStack Developer especializado en frontend &amp; Software Architect
      </span>
    </div>

    <div class="flex flex-col border border-primary-200 shadow-lg
               justify-center items-center w-80 h-100 rounded-2xl p-8 gap-4">
      <img src="/src/assets/dario.jpg" alt="Foto de perfil" class="w-40 h-40 rounded-full object-cover">
      <span class="text-2xl font-medium">Darío Martín</span>
      <span class="text-muted-color text-center">
        FullStack Developer especializado en backend &amp; Database Modeler
      </span>
    </div>

    <div class="flex flex-col border border-primary-200 shadow-lg
               justify-center items-center w-80 h-100 rounded-2xl p-8 gap-4">
      <img src="/src/assets/dani.jpg" alt="Foto de perfil" class="w-40 h-40 rounded-full object-cover">
      <span class="text-2xl font-medium">Daniel Gregori</span>
      <span class="text-muted-color text-center">
        Project Mannager &amp; QA
      </span>
    </div>
  </div>
</template>

<script>
import { defineComponent } from 'vue';
import Avatar from 'primevue/avatar';
</script>
