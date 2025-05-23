<template>
  <div class="flex justify-center mt-8">
    <ContactCard></ContactCard>
    <SecondCard></SecondCard>
    <ThirdCard></ThirdCard>
    <!--<FormCard class="mt-[700px]"></FormCard>  -->
  </div>
</template>
  
<script setup>
  import ContactCard from '@/components/contact/InfoCard.vue';
  import SecondCard from '@/components/contact/SecondCard.vue';
  import ThirdCard from '@/components/contact/ThirdCard.vue';
  import FormCard from '@/components/contact/FormCard.vue';
</script>