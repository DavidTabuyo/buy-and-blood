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
                </div>
            </div>
        </div>
        <div class="mt-8">
            <DataTable :value="products" showGridlines scroll class="min-w-[50rem] rounded-xl overflow-hidden">
                <Column field="activo" header="Activo" sorteable></Column>
                <Column field="cantidad" header="Cantidad" sorteble></Column>
                <Column field="valor" header="Valor" sorteble></Column>
                <Column field="ganancias" header="Ganancias"sorteable></Column>
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

const products = ref([
    { activo: 'Bitcoin', cantidad: 2, valor: 50000, ganancias: 10000 },
    { activo: 'Ethereum', cantidad: 5, valor: 3000, ganancias: 1500 },
    { activo: 'Cardano', cantidad: 100, valor: 2.5, ganancias: 50 },
    { activo: 'Solana', cantidad: 10, valor: 35, ganancias: 100 },
    { activo: 'Apple', cantidad: 15, valor: 150, ganancias: 300 },
    { activo: 'Tesla', cantidad: 8, valor: 700, ganancias: 560 },
    { activo: 'Amazon', cantidad: 5, valor: 3200, ganancias: 800 },
    { activo: 'Microsoft', cantidad: 10, valor: 280, ganancias: 400 },
]);

</script>
