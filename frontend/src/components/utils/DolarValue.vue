<template>
    <div>
        {{ str }}
    </div>
</template>

<script setup>
import { ref, defineProps, watch, onMounted } from 'vue'

const str = ref("");

const props = defineProps({
    value: Number
});

watch(props, () => {
    str.value = props.value.toLocaleString('en-US', {
        style: 'currency',
        currency: 'USD',
        minimumFractionDigits: 2,
        maximumFractionDigits: 2
    });
}, { deep: true, immediate: true });
</script>