<template>
    <div class="wrapper">
        <Card style="width: 30rem; height: auto; overflow: hidden;">
            <template #header>
                <img alt="user header" src="/src/assets/future.jpg" />
            </template>
            <template #title>Segundo cuadro info</template>
            <template #content>
                <p class="m-0" style="text-align: justify;">
                    <br />"Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.<br />
                    Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.<br />
                    Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur.<br />
                    Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."<br />
                </p>
            </template>
            <template #footer>
                <div class="flex gap-4 mt-1">
                    <Button label="Cancel" severity="secondary" outlined class="w-full" />
                    <Button label="Save" class="w-full" />
                </div>
            </template>
        </Card>
    </div>
</template>


<script setup>
import Card from 'primevue/card';
</script>

