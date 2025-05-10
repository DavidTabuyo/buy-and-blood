<template>
    <Card style="width: 30rem; height: auto; overflow: hidden; left: 10rem;" class="absolute">
        <template #header>
            <img alt="user header" src="/src/assets/future.jpg" />
        </template>
        <template #title>Sobre nosotros</template>
        <template #content>
            <p class="m-0" style="text-align: justify;">
                <br />Buy&Blood es una aplicación de inversión que permite comprar y vender activos financieros, gestionar carteras y acceder a planes de inversión personalizados.<br />
                Su objetivo es simplificar el proceso de inversión, ofreciendo una plataforma accesible y eficiente.<br />
                Dirigida a cualquier persona interesada en invertir, desde principiantes hasta inversores experimentados.<br />
                Buy&Blood soluciona la complejidad de la inversión tradicional mediante una interfaz intuitiva y herramientas que permiten monitorear y optimizar las inversiones de manera sencilla.
            </p>
        </template>
        <template #footer>
            <div class="flex gap-4 mt-1">
                <Button label="Cancel" severity="secondary" outlined class="w-full" />
                <Button label="Save" class="w-full" />
            </div>
        </template>
    </Card>
</template>


<script setup>
import Card from 'primevue/card';
</script>

