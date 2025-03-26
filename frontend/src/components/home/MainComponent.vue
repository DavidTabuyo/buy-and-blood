<template>
    <div class="card flex justify-center">
        <FloatLabel variant="in">
            <IconField>
                <InputIcon class="pi pi-search" />
                <InputText id="in_label" v-model="value2" autocomplete="off" variant="filled" />
            </IconField>
            <label for="in_label">Buscar activo</label>
        </FloatLabel>
        <div class="card flex justify-center">
        <SelectButton 
            v-model="value" 
            :options="options" 
            optionLabel="name" 
            aria-labelledby="single" 
        />
    </div>
    </div>
</template>


<script setup>

import { ref, watch } from 'vue';
import InputText from 'primevue/inputtext';
import FloatLabel from 'primevue/floatlabel';
import IconField from 'primevue/iconfield';
import InputIcon from 'primevue/inputicon';
import SelectButton from 'primevue/selectbutton';

//opciones del selector 
const options = ref([
    { name: 'Crypto', value: 1 },
    { name: 'Activos', value: 2 }
]);

// Inicializar con la opción "todas por defeco"
const value = ref(options.value[0]);
const searchText = ref(null);


</script>
