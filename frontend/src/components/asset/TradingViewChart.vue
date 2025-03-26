<template>
    <div class="tradingview-widget-container" style="height:100%; width:100%">
        <div class="tradingview-widget-container__widget" style="height:calc(100% - 32px); width:100%"></div>
    </div>
</template>

<script setup>
import { onMounted } from 'vue';

onMounted(() => {
    // Crear el script de TradingView dinámicamente
    const script = document.createElement('script');
    script.src = 'https://s3.tradingview.com/external-embedding/embed-widget-advanced-chart.js';
    script.async = true;
    script.innerHTML = JSON.stringify({
        autosize: true,
        symbol: "AMEX:VOO",
        interval: "D",
        timezone: "Europe/Madrid",
        theme: "light",
        style: "2",
        locale: "es",
        allow_symbol_change: false,
        hide_volume: true,
        support_host: "https://www.tradingview.com"
    });

    // Agregar el script al DOM
    document.querySelector('.tradingview-widget-container').appendChild(script);
});
</script>