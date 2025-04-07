<template>
        <div class="flex justify-between">
            <div>Bitcoin</div>
        </div>
        <p>{{ price }}$</p>
        <p :class="numberColor">{{ arrow }}{{ change }}%</p>
        <div>GRAFICO</div>
</template>

<script setup>
import { ref, defineProps, onMounted, watch } from 'vue';

// const props = defineProps({
//     number: Number
// });

const info = {
    price: 126327.2334,
    change: -0.023,
    graphValues: [10, 20, 30, 20, 10, 30, 20]
}
const price = ref('');
const numberColor = ref('');
const arrow = ref('');
const change = ref('');

onMounted(() => {
    price.value = info.price;
    numberColor.value = (info.change >= 0 ? 'text-green-500' : 'text-red-500');
    arrow.value = (info.change >= 0 ? '▲' : '▼');
    change.value = info.change;
})

// watch(props, (newProps) => {
//     price.value = newProps.price;
//     numberColor.value = (newProps.change >= 0 ? 'text-green-500' : 'text-red-500');
//     arrow.value = (newProps.change >= 0 ? '▲' : '▼');
//     change.value = newProps.change;
// }, { deep: true });

</script>