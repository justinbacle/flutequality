var echarts = require("echarts");

console.log("nfkdl");

var echartsDiv1 = document.createElement("div");
echartsDiv1.id = "echartsDiv1";
document.body.appendChild(echartsDiv1);

var fftChart = echarts.init(echartsDiv1);
var fftChartOptions = {
    title: {
        text: "FFT"
    },
    xAxis: {
        type: 'log',
        min: 20,
        max: 20000
    },
    yAxis: {
        type: 'value',
        min: -120
    },
    series: [
        {
            data: [],
            type: 'line',
            showSymbol: false,
        }
    ],
    animation: false
}
fftChart.setOption(fftChartOptions);