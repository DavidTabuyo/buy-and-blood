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
            <DataTable :value="products" showGridlines removableSort class="min-w-[50rem] rounded-xl overflow-hidden"
                @row-click="onRowClick" :pt="{
                    bodyRow: () => ({
                        role: 'button',
                        tabindex: 0,
                        class: 'cursor-pointer hover:bg-gray-200'
                    })
                }">
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

const products = ref(null);

const getProducts = () => {
    axios.get('/user/holdings')
        .then(response => {
            products.value = response.data;
        })
        .catch(error => {
            console.error('Error fetching products:', error);
        });
};
getProducts();

const onRowClick = (event) => {
    window.location.href = `/asset/${event.data.id}`;
};

</script>
