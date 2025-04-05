<template>
    <div class="flex w-full gap-8">
        <!-- Datos del activo -->
        <div class="w-2/3 flex flex-col h-full">
            <div>Fidelity S&P 500 Index Fund EUR P Acc</div>
            <div class="flex">
                <div>234,23$</div>
                <PercentageChange :value="changeValue" />
            </div>
            <div class="flex-1">
                <TradingViewChart class="h-full" />
            </div>
        </div>

        <!-- Compra venta -->
        <div class="w-1/3 flex flex-col items-center space-y-4 p-4 bg-white shadow-lg rounded-xl">
            <div class="text-center">Mi Total:</div>
            <div class="text-center">$12.234,34</div>
            <div class="flex justify-center items-center gap-2">
                <div>+$4233.23</div>
                <PercentageChange :value="changeValue" />
            </div>
            <div class="flex justify-center gap-2">
                <Button>Comprar</Button>
                <Button>Vender</Button>
            </div>
            <FloatLabel variant="on" class="w-full flex flex-col items-center">
                <div class="w-full flex justify-center">
                    <InputNumber class="w-full text-center" v-model="value" inputId="on_label" mode="currency"
                        currency="USD" locale="en-US" />
                </div>
                <label for="on-label" class="text-center">Introduce cantidad...</label>
            </FloatLabel>
            <div>
                <Button>Confirmar</Button>
            </div>
        </div>

    </div>
</template>

<script setup>
import { ref } from 'vue';
import InputNumber from 'primevue/inputnumber';
import FloatLabel from 'primevue/floatlabel';
import Button from 'primevue/button';
import TradingViewChart from '@/components/asset/TradingViewChart.vue';
import PercentageChange from '@/components/utils/PercentageChange.vue';

const value = ref(null);
const changeValue = ref(-0.39876974);
</script>