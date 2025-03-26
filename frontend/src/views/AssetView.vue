<template>
    <div class="flex w-full)]">
        <!-- Datos del activo -->
        <div class="w-2/3">
            <div>Fidelity S&P 500 Index Fund EUR P Acc</div>
            <div class="flex">
                <div>234,23$</div>
                <PercentageChange :value="changeValue" />
            </div>
            <TradingViewChart />
        </div>

        <!-- Compra venta -->
        <div class="w-1/3">
            <div>Mi Total:</div>
            <div>$12.234,34</div>
            <div class="flex">
                <div>+$4233.23</div>
                <PercentageChange :value="changeValue" />
            </div>
            <div class="flex">
                <Button>Comprar</Button>
                <Button>Vender</Button>
            </div>
            <FloatLabel variant="on">
                <InputNumber v-model="value" inputId="on_label" mode="currency" currency="USD" locale="en-US" />
                <label for="on-label">Introduce cantidad...</label>
            </FloatLabel>
            <Button>Confirmar</Button>
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