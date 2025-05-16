<template>
    <div class="flex justify-center mt-8">
      <ContactCard class="mx-2 w-120 h-80 overflow-hidden"></ContactCard>
      <FormCard class="mx-2 w-120 h-80 overflow-hidden"></FormCard>
      <ThirdCard class="mx-2 w-120 h-80 overflow-hidden"></ThirdCard>
    </div>
  </template>
  
  <script setup>
  import ContactCard from '@/components/contact/InfoCard.vue';
  import FormCard from '@/components/contact/FormCard.vue';
  import ThirdCard from '@/components/contact/ThirdCard.vue';
  </script>