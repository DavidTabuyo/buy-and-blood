<template>
    <div class="card flex justify-center">
        <FloatLabel variant="in">
            <IconField>
                <InputIcon class="pi pi-search" />
                <InputText id="in_label" v-model="value2" autocomplete="off" variant="filled" />
            </IconField>
            <label for="in_label">Buscar activo</label>
        </FloatLabel>
    </div>
</template>


<script setup>

import { ref } from 'vue';
import InputText from 'primevue/inputtext';
import FloatLabel from 'primevue/floatlabel';
import IconField from 'primevue/iconfield';
import InputIcon from 'primevue/inputicon';
const searchText = ref(null);

</script>
