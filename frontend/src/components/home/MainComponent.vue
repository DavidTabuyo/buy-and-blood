
<template>
    <div class="card flex justify-center">
        <IftaLabel>
            <InputText id="username" v-model="value" variant="filled" />
            <label for="username">Username</label>
        </IftaLabel>
    </div>
</template>

<script setup>

import { ref } from 'vue';
import InputText from 'primevue/inputtext';
import IftaLabel from 'primevue/iftalabel';

const value = ref(null);
</script>
