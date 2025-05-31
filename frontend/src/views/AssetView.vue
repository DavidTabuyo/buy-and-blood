<!-- src/views/AssetView.vue -->
<template>

  <div class="flex w-full gap-8">
    <ConfirmDialog />
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
        <DataTable :value="transactions" stripedRows emptyMessage="No hay transacciones disponibles" scrollable
          scrollHeight="100%">
          <template #empty>
            <div class="p-4 text-center text-gray-500">
              Todavía no ha realizado ninguna transacción
            </div>
          </template>

          <!-- Columna Fecha con formato YYYY-MM-DD -->
          <Column field="date" header="Fecha">
            <template #body="{ data }">
              {{ formatDate(data.date) }}
            </template>
          </Column>

          <!-- Columna Precio de compra con 2 decimales -->
          <Column field="buyPrice" header="Precio de compra">
            <template #body="{ data }">
              {{ formatNumber(data.buyPrice) }}
            </template>
          </Column>

          <!-- Columna Cantidad con 2 decimales -->
          <Column field="quantity" header="Cantidad">
            <template #body="{ data }">
              {{ formatNumber(data.quantity) }}
            </template>
          </Column>

          <!-- Columna Total con 2 decimales -->
          <Column field="total" header="Total">
            <template #body="{ data }">
              {{ formatNumber(data.total) }}
            </template>
          </Column>
        </DataTable>
      </div>

      <!-- Formulario simple de compra / venta -->
      <div class="w-full flex flex-col gap-4 pb-8">
        <FloatLabel variant="on" class="w-full">
          <InputNumber class="w-full text-center" ref="amountInput" v-model="amount" mode="currency" currency="USD"
            locale="en-US" />
          <label>Introduce cantidad…</label>
        </FloatLabel>
        <div class="flex gap-2 mt-8">
          <Button label="Comprar" @click="confirmBuy" class="flex-1 px-6 py-3 text-lg" severity="success" />
          <Button label="Vender" @click="confirmSell" class="flex-1 px-6 py-3 text-lg" :disabled="myTotal === 0" />
        </div>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
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
import Toast from 'primevue/toast'
import { useToast } from 'primevue/usetoast'
import ConfirmDialog from 'primevue/confirmdialog'
import { useConfirm } from 'primevue/useconfirm'

const confirm = useConfirm()
const route = useRoute()
const router = useRouter()
const auth = useAuthStore()
const ui = useUiStore()
const toast = useToast()
const amountInput = ref<InstanceType<typeof InputNumber> | null>(null)
const ticker = route.params.ticker
const assetData = ref<any>(null)
const transactions = ref<any[]>([])
const amount = ref<number | null>(null)

const percentageChange = ref<number>(0)
const changeValue = ref<number>(0)
const myTotal = ref<number>(0)

let intervalId: ReturnType<typeof setInterval> | null = null

async function fetchAssetData() {
  try {
    const { data } = await axios.get(`asset/${ticker}/`)
    assetData.value = data
  } catch (error: any) {
    const status = error.response?.status
    if (status === 401 || status === 403) {
      if (intervalId) clearInterval(intervalId)
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
    transactions.value = data
  } catch (err) {
    console.error('Error al obtener transacciones:', err)
  }
}

async function loadAssetUserData() {
  try {
    const response = await axios.get(`user/holding/${ticker}/`)
    const data = response.data

    percentageChange.value = data.percentage_change ?? 0
    changeValue.value = data.change_value ?? 0
    myTotal.value = data.total_value ?? 0
  } catch (error) {
    percentageChange.value = 0
    changeValue.value = 0
    myTotal.value = 0
  }
}

const buy = () => {
  axios
    .post(`user/transaction/${ticker}/`, {
      transaction_money: amount.value
    })
    .then(() => {
      toast.add({
        severity: 'success',
        summary: 'Compra realizada',
        detail: 'La compra se ha realizado con éxito',
        life: 3000
      })
      if (amount.value != null) {
        auth.user_data.balance -= amount.value
      }
      amount.value = 0
      loadTransactions()
      loadAssetUserData()
    })
    .catch((error) => {
      toast.add({
        severity: 'warn',
        summary: 'Error',
        detail: 'No se ha podido completar la transacción',
        life: 3000
      })
    })
}

const sell = () => {
  axios
    .post(`user/transaction/${ticker}/`, {
      transaction_money: amount.value != null ? -amount.value : null
    })
    .then(() => {
      toast.add({
        severity: 'success',
        summary: 'Venta realizada',
        detail: 'La venta se ha realizado con éxito',
        life: 3000
      })
      if (amount.value != null) {
        auth.user_data.balance += amount.value
      }
      amount.value = 0

      loadTransactions()
      loadAssetUserData()
    })
    .catch(() => {
      toast.add({
        severity: 'warn',
        summary: 'Error',
        detail: 'No se ha podido completar la transacción',
        life: 3000
      })
    })
}

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

/**
 * Devuelve la fecha en formato "YYYY-MM-DD". 
 * Si el valor es nulo o undefined, devuelve "-".
 */
function formatDate(value: string | null | undefined): string {
  if (!value) return '-'
  return value.substring(0, 10)
}

/**
 * Devuelve un número con 2 decimales. 
 * Si el valor es nulo o no es un número, devuelve "-".
 */
function formatNumber(value: number | string | null | undefined): string {
  if (value == null || value === '' || isNaN(Number(value))) {
    return '-'
  }
  return Number(value).toFixed(2)
}

// Nuevas funciones añadidas al <script setup>:

function confirmBuy() {
  if (amount.value == null || isNaN(amount.value) || amount.value <= 0) {
    toast.add({
      severity: 'warn',
      summary: 'Cantidad no válida',
      detail: 'Introduce una cantidad mayor que 0',

      life: 3000
    })
    return
  }
  if (amount.value > auth.user_data.balance) {
    toast.add({
      severity: 'warn',
      summary: 'Cantidad no válida',
      detail: 'No tienes saldo suficiente para realizar la transaccion',

      life: 3000
    })
    return
  }

  confirm.require({
    message: `¿Estás seguro de que quieres COMPRAR $${formatNumber(amount.value)}?`,
    header: 'Confirmar compra',
    icon: 'pi pi-exclamation-triangle',

    accept: () => {
      buy()
    }
  })
}

function confirmSell() {
  if (amount.value == null || isNaN(amount.value) || amount.value <= 0) {
    toast.add({
      severity: 'warn',
      summary: 'Cantidad no válida',
      detail: 'Introduce una cantidad mayor que 0',
      life: 3000
    })
    return
  }
  
  if (amount.value > myTotal.value) {
    toast.add({
      severity: 'warn',
      summary: 'Cantidad no válida',
      detail: 'No tienes saldo suficiente para realizar la transaccion',

      life: 3000
    })
    return
  }

  confirm.require({
    message: `¿Estás seguro de que quieres VENDER $${formatNumber(amount.value)}?`,
    header: 'Confirmar venta',
    icon: 'pi pi-exclamation-triangle',
    accept: () => {
      sell()
    }
  })
}

</script>
