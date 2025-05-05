<!-- src/views/AssetView.vue -->
<template>
  <div class="flex w-full gap-8">
    <!-- ---------------- Datos del activo ---------------- -->
    <div v-if="assetData && !assetData.error" class="w-2/3 flex flex-col h-full">
      <div class="text-3xl text-gray-500">{{ assetData.longName }}</div>

      <div class="flex items-center gap-2 mt-2 mb-3">
        <DolarValue
          :value="assetData.regularMarketPrice"
          class="text-3xl font-bold"
        />
        <PercentageChange
          :value="assetData.regularMarketChangePercent"
          class="text-xl"
        />
      </div>

      <div class="flex-1">
        <TradingViewChart class="h-full" :ticker="assetData.symbol" />
      </div>
    </div>

    <!-- Si devolvió error -->
    <div
      v-else-if="assetData?.error"
      class="w-full text-center text-red-500 self-center"
    >
      {{ assetData.error }}
    </div>

    <!-- ---------------- Compra / Venta ---------------- -->
    <div
      v-if="assetData && !assetData.error"
      class="w-1/3 flex flex-col justify-between items-center space-y-4 p-4 bg-white shadow-lg rounded-xl"
    >
      <div>
        <div class="text-center text-3xl mb-4 text-gray-500">Mi Total:</div>
        <DolarValue :value="myTotal" class="text-center text-4xl font-bold" />
        <div class="flex justify-center items-center gap-2">
          <ChangeValue :value="changeValue" class="text-2xl" />
          <PercentageChange :value="percentageChange" />
        </div>
      </div>

      <!-- Tabla de transacciones -->
      <DataTable :value="transactions" stripedRows>
        <Column field="date"         header="Fecha" />
        <Column field="buyPrice"     header="Precio de compra" />
        <Column field="sharesNumber" header="Acciones" />
        <Column field="quantity"     header="Total" />
      </DataTable>

      <!-- Formulario simple de compra / venta -->
      <div class="w-full flex flex-col items-center gap-4">
        <ButtonGroup class="flex justify-center w-full">
          <Button
            label="Comprar"
            class="flex-1"
            :class="getButtonClass('buy')"
            @click="selectOption('buy')"
          />
          <Button
            label="Vender"
            class="flex-1"
            :class="getButtonClass('sell')"
            @click="selectOption('sell')"
          />
        </ButtonGroup>

        <div class="flex gap-2 items-center text-gray-500">
          <span>Disponible:</span>
          <DolarValue :value="availableCash" class="text-xl" />
        </div>

        <FloatLabel variant="on" class="w-full">
          <InputNumber
            class="w-full text-center"
            v-model="amount"
            mode="currency"
            currency="USD"
            locale="en-US"
          />
          <label>Introduce cantidad…</label>
        </FloatLabel>
      </div>

      <Button class="w-full" :disabled="!amount || amount <= 0">
        Confirmar
      </Button>
    </div>
  </div>
</template>

<script setup>
/* -------------------------------------------------------------
 * imports
 * -----------------------------------------------------------*/
import { ref, onMounted, onBeforeUnmount } from 'vue'
import { useRoute, useRouter } from 'vue-router'
import axios from '@/axios'          // instancia con interceptores
import { useAuthStore } from '@/stores/auth'
import { useUiStore }   from '@/stores/ui'

import TradingViewChart  from '@/components/asset/TradingViewChart.vue'
import PercentageChange  from '@/components/utils/PercentageChange.vue'
import ChangeValue       from '@/components/utils/ChangeValue.vue'
import DolarValue        from '@/components/utils/DolarValue.vue'
import InputNumber       from 'primevue/inputnumber'
import FloatLabel        from 'primevue/floatlabel'
import Button            from 'primevue/button'
import ButtonGroup       from 'primevue/buttongroup'
import DataTable         from 'primevue/datatable'
import Column            from 'primevue/column'

/* -------------------------------------------------------------
 * state
 * -----------------------------------------------------------*/
const route  = useRoute()
const router = useRouter()
const auth   = useAuthStore()
const ui     = useUiStore()

const ticker        = route.params.ticker
const assetData     = ref(null)
const transactions  = ref([])
const amount        = ref(null)

const percentageChange = ref(-0.3987)
const changeValue      = ref(8234.34)
const myTotal          = ref(123342.45)
const availableCash    = ref(12)

let intervalId = null
const selectedOp = ref('buy')

/* -------------------------------------------------------------
 * helpers
 * -----------------------------------------------------------*/
function getButtonClass (op) {
  return {
    'p-button-primary' : selectedOp.value === op,
    'p-button-outlined': selectedOp.value !== op
  }
}
function selectOption (op) { selectedOp.value = op }

/* -------------------------------------------------------------
 * API calls
 * -----------------------------------------------------------*/
async function fetchAssetData () {
  try {
    const { data } = await axios.get(`asset/${ticker}/`)
    assetData.value = data
  } catch (error) {
    const status = error.response?.status
    if (status === 401 || status === 403) {
      clearInterval(intervalId)
      auth.isLoggedIn = false
      auth.user_data  = null
      ui.openAuthDialog()
      router.replace({ path: '/', query: { sessionExpired: '1' } })
    } else {
      console.error('Error al obtener asset:', error)
      assetData.value = { error: 'No se pudo obtener el asset' }
    }
  }
}

async function loadTransactions () {
  try {
    const { data } = await axios.get('asset/transactions/', {
      params: { asset_id: ticker }
    })
    transactions.value = data
  } catch (err) {
    console.error('Error al obtener transacciones:', err)
  }
}

/* -------------------------------------------------------------
 * lifecycle
 * -----------------------------------------------------------*/
onMounted(async () => {
  await auth.checkSession()
  if (auth.isLoggedIn) {
    await fetchAssetData()
    await loadTransactions()
    intervalId = setInterval(fetchAssetData, 5000)
  } else {
    ui.openAuthDialog()
    router.replace({ path: '/', query: { sessionExpired: '1' } })
  }
})

onBeforeUnmount(() => {
  if (intervalId) clearInterval(intervalId)
})
</script>
