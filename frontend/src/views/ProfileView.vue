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
            <DataTable :value="products" showGridlines removableSort class="min-w-[50rem] rounded-xl overflow-hidden">
                <Column field="asset" header="Activo" sortable style="width: 40%;"></Column>
                <Column field="quantity" header="Cantidad" sortable style="width: 15%;">
                    <template #body="slotProps">
                        <div class="text-center">
                            {{ slotProps.data.quantity }}
                        </div>
                    </template>
                </Column>
                <Column field="value" header="Valor" sortable style="width: 20%;">
                    <template #body="slotProps">
                        <DolarValue :value="slotProps.data.value" class="text-center" />
                    </template>
                </Column>
                <Column header="Ganancias" sortable sortField="percentage_change" style="width: 25%;">
                    <template #body="slotProps">
                        <div class="flex gap-4">
                            <ChangeValue :value="slotProps.data.change_value" class="w-1/2 text-right" />
                            <PercentageChange :value="slotProps.data.percentage_change" class="w-1/2" />
                        </div>
                    </template>
                </Column>
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
    { asset: 'SPDR S&P 500 ETF', quantity: 100.234, value: 45000.56, change_value: 500.12, percentage_change: 1.123 },
    { asset: 'Vanguard Total Stock Market ETF', quantity: 150.567, value: 34500.78, change_value: 300.45, percentage_change: 0.874 },
    { asset: 'iShares MSCI Emerging Markets ETF', quantity: 200.891, value: 11000.34, change_value: 100.23, percentage_change: 0.912 },
    { asset: 'Invesco QQQ Trust', quantity: 50.123, value: 18500.89, change_value: 700.67, percentage_change: 3.934 },
    { asset: 'Schwab U.S. Dividend Equity ETF', quantity: 120.456, value: 9000.12, change_value: 150.34, percentage_change: 1.693 },
    { asset: 'ARK Innovation ETF', quantity: 80.789, value: 9600.45, change_value: 400.56, percentage_change: 4.354 },
    { asset: 'iShares Russell 2000 ETF', quantity: 70.234, value: 14700.67, change_value: 350.78, percentage_change: 2.432 },
    { asset: 'Vanguard FTSE Developed Markets ETF', quantity: 180.567, value: 9000.89, change_value: 80.12, percentage_change: 0.894 },
    { asset: 'Bitcoin (BTC)', quantity: 0.543, value: 30000.34, change_value: 2000.45, percentage_change: 7.143 },
    { asset: 'Ethereum (ETH)', quantity: 2.345, value: 4000.56, change_value: 300.67, percentage_change: 8.114 },
]);

</script>
