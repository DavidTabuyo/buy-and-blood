<template>
  <div class="card flex flex-col items-center overflow-hidden pb-8">
    <!-- Header con texto y flecha -->
    <div class="flex flex-col items-center gap-2">
      <span class="text-xl font-medium">Scroll Down</span>
      <span
        class="animate-bounce h-8 w-8 bg-primary text-primary-contrast
               rounded-full inline-flex items-center justify-center -z-10"
      >
        <i class="pi pi-arrow-down"></i>
      </span>
    </div>

    <!-- Espacio para hacer scroll -->
    <div class="h-[10rem]"></div>

    <!-- Tres tarjetas animadas al hacer scroll -->
    <div class="flex flex-wrap justify-center gap-8">
      <div
        v-animateonscroll="{ enterClass: 'animate-enter fade-in-10 slide-in-from-t-20 animate-duration-1000' }"
        class="flex flex-col border border-primary-200 shadow-lg
               justify-center items-center max-w-80 rounded-2xl p-8 gap-4"
      >
        <Avatar
          image="/src/assets/david.jpg"
          shape="circle"
          size="xlarge"
        />
        <span class="text-2xl font-medium">David Tabuyo</span>
        <span class="text-muted-color text-center">
          FullStack Developer especializado en frontend &amp; Software Architect
        </span>
      </div>

      <div
        v-animateonscroll="{ enterClass: 'animate-enter fade-in-10 slide-in-from-b-20 animate-duration-1000' }"
        class="flex flex-col border border-primary-200 shadow-lg
               justify-center items-center max-w-80 rounded-2xl p-8 gap-4"
      >
        <Avatar
          image="/src/assets/dario.jpg"
          shape="circle"
          size="xlarge"
        />
        <span class="text-2xl font-medium">Darío Martín</span>
        <span class="text-muted-color text-center">
          FullStack Developer especializado en backend &amp; Database Modeler
        </span>
      </div>

      <div
        v-animateonscroll="{ enterClass: 'animate-enter fade-in-10 slide-in-from-t-20 animate-duration-1000' }"
        class="flex flex-col border border-primary-200 shadow-lg
               justify-center items-center max-w-80 rounded-2xl p-8 gap-4"
      >
        <Avatar
          image="/src/assets/dani.jpg"
          shape="circle"
          size="xlarge"
        />
        <span class="text-2xl font-medium">Daniel Gregori</span>
        <span class="text-muted-color text-center">
          Project Mannager &amp; QA
        </span>
      </div>
    </div>
  </div>
</template>

<script>
import { defineComponent } from 'vue';
import AnimateOnScroll from 'primevue/animateonscroll';
import Avatar from 'primevue/avatar';

export default defineComponent({
  name: 'ScrollCards',
  directives: {
    animateonscroll: AnimateOnScroll
  },
  components: {
    Avatar
  }
});
</script>
