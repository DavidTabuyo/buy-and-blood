<template>
    <Card
    style="width: 30rem; height: 20rem; overflow: hidden;"
    class="absolute transition-all duration-300"
    :style="{ height: expanded ? 'auto' : '20rem' }"
    >
        <template #title>Simple Card</template>
        <template #content>
            <p class="m-0">
                Lorem ipsum dolor sit amet, consectetur adipisicing elit. Inventore sed consequuntur error repudiandae numquam deserunt quisquam repellat libero asperiores earum nam nobis, culpa ratione quam perferendis esse, cupiditate neque
                quas!
            </p>
        </template>
    </Card>
</template>

<script setup>
    import Card from 'primevue/card';
</script>