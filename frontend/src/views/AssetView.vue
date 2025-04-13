<template>
    <div class="flex w-full gap-8">
        <!-- Datos del activo -->
        <div class="w-2/3 flex flex-col h-full">
            <div class="text-3xl text-gray-500">{{ assetData.longName }}</div>
            <div class="flex items-center gap-2 mt-2 mb-3">
                <DolarValue :value="assetData.regularMarketPrice" class="text-3xl font-bold" />
                <PercentageChange :value="assetData.regularMarketChangePercent" class="text-xl" />
            </div>
            <div class="flex-1">
                <TradingViewChart class="h-full" :ticker="assetData.symbol" />
            </div>
        </div>

        <!-- Compra venta -->
        <div class="w-1/3 flex flex-col justify-between items-center space-y-4 p-4 bg-white shadow-lg rounded-xl">
            <div>
                <div class="text-center text-3xl mb-4 text-gray-500">Mi Total:</div>
                <DolarValue :value="myTotal" class="text-center text-4xl font-bold" />
                <div class="flex justify-center items-center gap-2">
                    <ChangeValue :value="changeValue" class="text-2xl" />
                    <PercentageChange :value="percentageChange" />
                </div>
            </div>
            <div class="w-full flex flex-col items-center gap-4">
                <ButtonGroup class="flex justify-center">
                    <Button label="Comprar" class="flex-1" :class="getButtonClass('opcion1')"
                        @click="selectOption('opcion1')" />
                    <Button label="Vender" class="flex-1" :class="getButtonClass('opcion2')"
                        @click="selectOption('opcion2')" />
                </ButtonGroup>
                <div class="flex gap-2 items-centeri text-gray-500">
                    <div>Disponible:</div>
                    <div>
                        <DolarValue :value="12" class="text-xl" />
                    </div>
                </div>
                <FloatLabel variant="on" class="w-full flex flex-col items-center">
                    <div class="flex justify-center">
                        <InputNumber class="w-full text-center" v-model="value" @input="value = $event.value"
                            inputId="on_label" mode="currency" currency="USD" locale="en-US" />
                    </div>
                    <label for="on-label" class="text-center">Introduce cantidad...</label>
                </FloatLabel>
            </div>
            <div class="w-full flex flex-col">

                <Button class="w-full" :disabled="!value || value <= 0">Confirmar</Button>
            </div>
        </div>

    </div>
</template>

<script setup>
import axios from '../axios.js';
import { ref, onBeforeMount, onBeforeUnmount} from 'vue';
import InputNumber from 'primevue/inputnumber';
import FloatLabel from 'primevue/floatlabel';
import Button from 'primevue/button';
import TradingViewChart from '@/components/asset/TradingViewChart.vue';
import PercentageChange from '@/components/utils/PercentageChange.vue';
import ChangeValue from '@/components/utils/ChangeValue.vue';
import DolarValue from '@/components/utils/DolarValue.vue';
import ButtonGroup from 'primevue/buttongroup';
import { useRoute } from 'vue-router'

const route = useRoute()
const ticker = route.params.ticker

const assetData = ref(null)

const fetchAssetData = () => {
    axios.get(`asset/${ticker}/`)
        .then((response) => {
            console.log('ok')
            assetData.value = response.data
        })
        .catch((error) => {
            console.log('nook')
            console.error('Error al obtener datos:', error)
            assetData.value = { error: 'No se pudo obtener el asset' }
        })
}


let intervalId = null

onBeforeMount(() => {
    // Llama de inmediato
    fetchAssetData()

    // Luego cada 3 segundos
    intervalId = setInterval(() => {
        fetchAssetData()
    }, 5000)
})

onBeforeUnmount(() => {
    if (intervalId) clearInterval(intervalId)
})


const value = ref(null);
const percentageChange = ref(-0.39876974);
const changeValue = ref(8234.345);
const myTotal = ref(123342.45563);


// Para el boton de comprar/vender
const selected = ref('opcion1'); // Opción por defecto seleccionada

const selectOption = (option) => {
    selected.value = option;
};

// Función para asignar clases dinámicamente
const getButtonClass = (option) => {
    return {
        'p-button-primary': selected.value === option, // Color cuando está seleccionado
        'p-button-outlined': selected.value !== option // Color por defecto
    };
};
</script>