<template>
  <div class="justify-center mt-8">
    <div class="flex w-full gap-16">
      <ContactCard class="w-1/3"></ContactCard>
      <SecondCard class="w-1/3"></SecondCard>
      <ThirdCard class="w-1/3"></ThirdCard>
    </div>
    <TeamCard class="mt-[3rem]"></TeamCard>
  </div>
</template>
  
<script setup>
  import ContactCard from '@/components/contact/InfoCard.vue';
  import SecondCard from '@/components/contact/SecondCard.vue';
  import ThirdCard from '@/components/contact/ThirdCard.vue';
  import TeamCard from '@/components/contact/TeamCard.vue';
</script>