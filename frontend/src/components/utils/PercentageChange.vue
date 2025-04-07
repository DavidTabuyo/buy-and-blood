<template>
    <div :class="color">
        {{ str }}
    </div>
</template>

<script setup>
import { ref, defineProps, watch } from 'vue'

const color = ref("");
const str = ref("");

const props = defineProps({
    value: Number
});

watch(props, () => {
    str.value = '';
    if (props.value === 0) {
        str.value += '-';
        color.value = 'text-gray-500';
    } else if (props.value > 0) {
        str.value += '▲';
        color.value = 'text-green-500';
    } else {
        str.value += '▼';
        color.value = 'text-red-500';
    }

    str.value += props.value.toFixed(2);

    str.value += '%';
}, { deep: true, immediate: true });

</script>