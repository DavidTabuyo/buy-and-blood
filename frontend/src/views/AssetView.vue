<!-- src/views/AssetView.vue -->
<template>
  <div class="flex w-full gap-8">
    <!-- ---------------- Datos del activo ---------------- -->
    <div v-if="assetData && !assetData.error" class="w-2/3 flex flex-col h-full">
      <div class="text-3xl text-gray-500">{{ assetData.longName }}</div>

      <div class="flex items-center gap-2 mt-2 mb-3">
        <DolarValue :value="assetData.regularMarketPrice" class="text-3xl font-bold" />
        <PercentageChange :value="assetData.regularMarketChangePercent" class="text-xl" />
      </div>
      <Toast />

      <div class="flex-1">
        <TradingViewChart class="h-full" :ticker="assetData.symbol" />
      </div>
    </div>

    <!-- Si devolvió error -->
    <div v-else-if="assetData?.error" class="w-full text-center text-red-500 self-center">
      {{ assetData.error }}
    </div>

    <div v-if="assetData && !assetData.error"
      class="w-1/3 flex flex-col justify-between items-center space-y-4 p-4 bg-white shadow-lg rounded-xl">
      <div>
        <div class="text-center text-3xl mb-4 text-gray-500">Mi Total:</div>
        <DolarValue :value="myTotal" class="text-center text-4xl font-bold" />
        <div class="flex justify-center items-center gap-2">
          <ChangeValue :value="changeValue" class="text-2xl" />
          <PercentageChange :value="percentageChange" />
        </div>
      </div>

  <div class="max-h-80 max-w-full overflow-auto">
    <DataTable
      :value="transactions"
      stripedRows
      emptyMessage="No hay transacciones disponibles"
      scrollable
      scrollHeight="100%"      
    >
      <template #empty>
        <div class="p-4 text-center text-gray-500">
          Todavía no ha realizado ninguna transacción
        </div>
      </template>
      <Column field="date"      header="Fecha"              />
      <Column field="buyPrice"  header="Precio de compra"   />
      <Column field="quantity"  header="Cantidad"           />
      <Column field="total"     header="Total"              />
    </DataTable>
  </div>

      <!-- Formulario simple de compra / venta -->
      <div class="w-full flex flex-col gap-4 pb-8">

        <FloatLabel variant="on" class="w-full">
          <InputNumber class="w-full text-center" v-model="amount" mode="currency" currency="USD" locale="en-US" />
          <label>Introduce cantidad…</label>
        </FloatLabel>
        <div class="flex gap-2 mt-8">
          <Button label="Comprar" @click="buy" class="flex-1 px-6 py-3 text-lg" severity="success" />
          <Button label="Vender" @click="sell" class="flex-1 px-6 py-3 text-lg" :disabled="myTotal === 0" 
            />
        </div>

      </div>
    </div>
  </div>

</template>

<script setup>

import { ref, onMounted, onBeforeUnmount } from 'vue'
import { useRoute, useRouter } from 'vue-router'
import axios from '@/axios'
import { useAuthStore } from '@/stores/auth'
import { useUiStore } from '@/stores/ui'

import TradingViewChart from '@/components/asset/TradingViewChart.vue'
import PercentageChange from '@/components/utils/PercentageChange.vue'
import ChangeValue from '@/components/utils/ChangeValue.vue'
import DolarValue from '@/components/utils/DolarValue.vue'
import InputNumber from 'primevue/inputnumber'
import FloatLabel from 'primevue/floatlabel'
import Button from 'primevue/button'
import DataTable from 'primevue/datatable'
import Column from 'primevue/column'
import Toast from 'primevue/toast';
import { useToast } from 'primevue/usetoast';


const route = useRoute()
const router = useRouter()
const auth = useAuthStore()
const ui = useUiStore()
const toast = useToast();

const ticker = route.params.ticker
const assetData = ref(null)
const transactions = ref([])
const amount = ref(null)

const percentageChange = ref(0)
const changeValue = ref(0)
const myTotal = ref(0)

let intervalId = null

async function fetchAssetData() {
  try {
    const { data } = await axios.get(`asset/${ticker}/`)
    assetData.value = data
  } catch (error) {
    const status = error.response?.status
    if (status === 401 || status === 403) {
      clearInterval(intervalId)
      auth.isLoggedIn = false
      auth.user_data = null
      ui.openAuthDialog()
      router.replace({ path: '/', query: { sessionExpired: '1' } })
    } else {
      console.error('Error al obtener asset:', error)
      assetData.value = { error: 'No se pudo obtener el asset' }
    }
  }
}

async function loadTransactions() {
  try {
    const { data } = await axios.get(`asset/transactions/${ticker}/`)
    console.log()
    transactions.value = data
    console.log(transactions.value);
  } catch (err) {
    console.error('Error al obtener transacciones:', err)
  }
}

async function loadAssetUserData() {
  try {
    const response = await axios.get(`user/holding/${ticker}/`);
    const data = response.data;

    percentageChange.value = data.percentage_change ?? 0;
    changeValue.value = data.change_value ?? 0;
    myTotal.value = data.total_value ?? 0;
  } catch (error) {
    percentageChange.value = 0;
    changeValue.value = 0;
    myTotal.value = 0;
  }
}

const buy = () => {

  axios.post(`user/transaction/${ticker}/`, {
    transaction_money: amount.value
  })
    .then(() => {
      toast.add({ severity: 'success', summary: 'Compra realizada', detail: 'La compra se ha realizado con éxito', life: 3000 });
      //quitamos el saldo al usuario
      if (amount.value != null){
      auth.user_data-=amount.value;
      }
      amount.value = null
      loadTransactions()
      loadAssetUserData()
    })
    .catch((error) => {
      toast.add({ severity: 'danger', summary: 'Error', detail: 'No se ha podido completar la transacción', life: 3000 });
    })
};

const sell = () => {

};


onMounted(async () => {
  await auth.checkSession()
  if (auth.isLoggedIn) {
    await fetchAssetData()
    await loadTransactions()
    await loadAssetUserData()
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
