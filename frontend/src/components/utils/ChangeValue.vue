<template>
    <div>
        {{ str }}
    </div>
</template>

<script setup>
import { ref, defineProps, watch } from 'vue'

const str = ref("");

const props = defineProps({
    value: Number
});

watch(props, () => {
    // Signo
    const sign = props.value >= 0 ? "+" : "-"

    // Valor
    const absValue = Math.abs(props.value);
    const strValue = absValue.toLocaleString('en-US', {
        style: 'currency',
        currency: 'USD',
        minimumFractionDigits: 2,
        maximumFractionDigits: 2
    });

    // Concatenar todo
    str.value = sign + strValue
}, { deep: true, immediate: true });
</script>