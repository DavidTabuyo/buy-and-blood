<template>
    <div class="flex justify-center bg-white shadow-lg rounded-xl p-2">
        <ScrollPanel style="width: 100%; height: calc(100vh - 250px)">
            <div>
                <div>
                <DayPlanComponent></DayPlanComponent>
            </div>
            <div>
                <DayPlanComponent></DayPlanComponent>
            </div>
            <div>
                <DayPlanComponent></DayPlanComponent>
            </div>
            <div>
                <DayPlanComponent></DayPlanComponent>
            </div>
            <div>
                <DayPlanComponent></DayPlanComponent>
            </div>
            </div>

          
        </ScrollPanel>
    </div>
</template>


<script setup>
import ScrollPanel from 'primevue/scrollpanel';
import DayPlanComponent from '@/components/utils/DayPlanComponent.vue';

</script>