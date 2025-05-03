<template>
    <div>
        <div class="flex">
            <div class="w-1/2">
                <DolarValue :value=123453.234 class="text-center text-5xl font-bold" />
                <div class="flex justify-center items-center gap-2">
                    <ChangeValue :value=2142.324 class="text-2xl" />
                    <PercentageChange :value=23.34 />
                </div>
            </div>
            <div class="w-1/2">
                <div class="w-2/3 ml-auto text-center bg-white shadow-lg rounded-xl p-4">
                    <div>Plan de inversion</div>
                    <DayPlanComponent />
                </div>
            </div>
        </div>
        <div class="mt-8">
            <DataTable :value="products" showGridlines class="min-w-[50rem] rounded-xl overflow-hidden">
                <Column field="activo" header="Activo"></Column>
                <Column field="cantidad" header="Cantidad"></Column>
                <Column field="valor" header="Valor"></Column>
                <Column field="ganancias" header="Ganancias"></Column>
            </DataTable>
        </div>
    </div>
</template>


<script setup>
import { ref } from 'vue';
import DataTable from 'primevue/datatable';
import Column from 'primevue/column';
import DayPlanComponent from '@/components/utils/DayPlanComponent.vue';
import DolarValue from '@/components/utils/DolarValue.vue';
import ChangeValue from '@/components/utils/ChangeValue.vue';
import PercentageChange from '@/components/utils/PercentageChange.vue';
import axios from '../axios.js';



</script>
