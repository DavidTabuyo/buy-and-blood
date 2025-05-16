<template>
    <div>
        <div class="flex h-1000">
            <div class="w-1/2 flex flex-col h-[40em] ">
                <DolarValue :value=123453.234 class="text-center text-5xl font-bold" />
                <div class="flex justify-center items-center gap-2">
                    <ChangeValue :value=2142.324 class="text-2xl" />
                    <PercentageChange :value=23.34 />
                </div>
                <HoldingChart :holdings="holdings" class="grow"/>
            </div>
            <div class="w-1/2 ">
                <div class="w-2/3 ml-auto text-center bg-white shadow-lg rounded-xl p-4">
                    <div>Plan de inversion</div>
                    <DayPlanComponent :labels="labels" :values="values" :planName="name"/>
                </div>
            </div>
        </div>
        <div class="mt-8">
            <DataTable :value="holdings" showGridlines removableSort class="min-w-[50rem] rounded-xl overflow-hidden"
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
import HoldingChart from '@/components/profile/HoldingChart.vue';
import axios from '../axios.js';

const holdings = ref(null);
const labels = ref([]);
const values = ref([]);
const name = ref('');

const getHoldings = () => {
    axios.get('/user/holdings/')
        .then(response => {
            holdings.value = response.data;
        })
        .catch(error => {
            console.error('Error fetching products:', error);
        });
};
getHoldings();

const getInvestingPlan = () => {
    axios.get('/user/investing-plan/')
        .then(response => {
            labels.value = response.data.labels;
            values.value = response.data.values;
            name.value = response.data.name;
        })
        .catch(error => {
            console.error('Error fetching products:', error);
        });
};
getInvestingPlan();

const onRowClick = (event) => {
    window.location.href = `/asset/${event.data.id}`;
};

</script>
