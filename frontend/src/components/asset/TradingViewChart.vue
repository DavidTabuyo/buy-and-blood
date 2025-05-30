<!-- TradingViewWidget.vue -->
<template>
    <div class="tradingview-widget-container" ref="container">
        <div class="tradingview-widget-container__widget"></div>
        <div class="tradingview-widget-copyright">
            <a href="https://www.tradingview.com/" rel="noopener nofollow" target="_blank">
                <span class="blue-text">Track all markets on TradingView</span>
            </a>
        </div>
    </div>
</template>

<script setup>
import { onMounted, ref, defineProps } from 'vue';

const props = defineProps({
    ticker: String
});

const container = ref(null);

onMounted(() => {

    const script = document.createElement('script');
    script.src = 'https://s3.tradingview.com/external-embedding/embed-widget-symbol-overview.js';
    script.type = 'text/javascript';
    script.async = true;
    script.innerHTML = `
    {
      "symbols": [
        [
          "${props.ticker}|12m"
        ]
      ],
      "chartOnly": true,
      "width": "100%",
      "height": "100%",
      "locale": "es",
      "colorTheme": "light",
      "autosize": true,
      "showVolume": false,
      "showMA": false,
      "hideDateRanges": false,
      "hideMarketStatus": false,
      "hideSymbolLogo": false,
      "scalePosition": "right",
      "scaleMode": "Normal",
      "fontFamily": "-apple-system, BlinkMacSystemFont, Trebuchet MS, Roboto, Ubuntu, sans-serif",
      "fontSize": "10",
      "noTimeScale": false,
      "valuesTracking": "1",
      "changeMode": "price-and-percent",
      "chartType": "area",
      "maLineColor": "#2962FF",
      "maLineWidth": 1,
      "maLength": 9,
      "headerFontSize": "medium",
      "lineWidth": 2,
      "lineType": 0,
      "dateRanges": [
        "12m|1D",
        "1d|1",
        "1w|15",
        "1m|30",
        "3m|60",
        "60m|1W",
        "all|1M"
      ]
    }`;
    container.value.appendChild(script);
});
</script>

<style scoped>
.tradingview-widget-container {
    width: 100%;
    height: 100%;
}
</style>
