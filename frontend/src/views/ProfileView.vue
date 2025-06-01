<template>
    <div>
        <div class="flex h-1000">
            <div class="w-1/2 flex flex-col h-[40em] ">
                <DolarValue :value=total class="text-center text-5xl font-bold" />
                <div class="flex justify-center items-center gap-2">
                    <ChangeValue :value=totalChange class="text-2xl" />
                    <PercentageChange :value=percentageChange />
                </div>
                <HoldingChart :holdings="pieHoldings" class="grow" />
            </div>
            <div class="w-1/2 ">
                <div class="w-2/3 ml-auto text-center bg-white shadow-lg rounded-xl p-4">

                    <div v-if="!values.length">
                        Cuando selecciones un plan se mostrará aquí!
                    </div>
                    <div  v-show="values.length">
                        <div>Plan de inversion</div>
                        <DayPlanComponent :labels="labels" :values="values" :planName="name" :percentage_change="planPercentageChange"/>
                    </div>
                </div>
            </div>
        </div>
        <div class="mt-8">
            <DataTable :value="tableHoldings" showGridlines removableSort class="min-w-[50rem] rounded-xl overflow-hidden"
                @row-click="onRowClick" :pt="{
                    bodyRow: () => ({
                        role: 'button',
                        tabindex: 0,
                        class: 'cursor-pointer hover:bg-gray-200'
                    })
                }">
                <Column field="asset_name" header="Activo" sortable style="width: 40%;"></Column>
                <Column field="amount" header="Cantidad" sortable style="width: 15%;">
                    <template #body="slotProps">
                        <div class="text-center">
                            {{ slotProps.data.amount }}
                        </div>
                    </template>
                </Column>
                <Column field="total_value" header="Valor" sortable style="width: 20%;">
                    <template #body="slotProps">
                        <DolarValue :value="slotProps.data.total_value" class="text-center" />
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
import { onMounted, ref } from 'vue';
import DataTable from 'primevue/datatable';
import Column from 'primevue/column';
import DayPlanComponent from '@/components/utils/DayPlanComponent.vue';
import DolarValue from '@/components/utils/DolarValue.vue';
import ChangeValue from '@/components/utils/ChangeValue.vue';
import PercentageChange from '@/components/utils/PercentageChange.vue';
import HoldingChart from '@/components/profile/HoldingChart.vue';
import axios from '@/axios'; ;

const tableHoldings = ref(null);
const pieHoldings = ref(null);
const labels = ref([]);
const values = ref([]);
const planPercentageChange = ref(0);
const name = ref('');
const total = ref(0);
const totalChange = ref(0);
const percentageChange = ref(0);


const getHoldings = () => {
    axios.get('/user/holdings/')
        .then(response => {
            tableHoldings.value = response.data;
            pieHoldings.value = response.data;
            tableHoldings.value.forEach(element => {

                total.value += element.total_value;
                totalChange.value += element.change_value;
                percentageChange.value = totalChange.value / total.value * 100;
            });
            console.log(tableHoldings.value);
            tableHoldings.value = tableHoldings.value.filter(el => el.asset_id !== 9);

        })
        .catch(error => {
            console.error('Error fetching products:', error);
        });
};

const getInvestingPlan = () => {
    axios.get('/user/investing-plan/')
        .then(response => {
            labels.value = response.data.labels;
            values.value = response.data.percentages;
            name.value = response.data.name;
            planPercentageChange.value = response.data.planPercentageChange;
        })
        .catch(error => {
            console.error('Error fetching products:', error);
        });
};
onMounted(()=> {
    getHoldings();
    getInvestingPlan();

});

const onRowClick = (event) => {
    window.location.href = `/asset/${event.data.asset_id}`;
};

</script>
