const ctx1 = document.getElementById('strokeChart').getContext('2d');
const ctx2 = document.getElementById('lungCancerChart').getContext('2d');

const strokeData = {
    labels: [0, 1, 2, 3, 4, 5],
        datasets: [{
            label: 'Stroke',
            data: [null, null, null, null, null, null],
            fill: false,
            borderColor: 'rgb(75, 192, 192)',
            tension: 0.1
        }]
};

const lungData = {
    labels: [0, 1, 2, 3, 4, 5],
        datasets: [{
            label: 'Lung Cancer',
            data: [null, null, null, null, null, null],
            fill: false,
            borderColor: 'rgb(75, 192, 192)',
            tension: 0.1
        }]
};

const strokeConfig = {
    scales: {
        xAxes: [{
            ticks: {
                stepSize: 5,
                min: 10,
                max: 90
            },
            scaleLabel: {
                display: true,
                labelString: 'Age'
            },
        }],
        yAxes: [{
            ticks: {
                stepSize: 5,
                min: 0,
                max: 70
            },
            scaleLabel: {
                display: true,
                labelString: 'Likelihood of Stroke (%)'
            }
        }]
    }
};

const lungConfig = {
    scales: {
        xAxes: [{
            ticks: {
                stepSize: 5,
                min: 10,
                max: 90
            },
            scaleLabel: {
                display: true,
                labelString: 'Age'
            },
        }],
        yAxes: [{
            ticks: {
                stepSize: 5,
                min: 0,
                max: 110
            },
            scaleLabel: {
                display: true,
                labelString: 'Likelihood of Lung Cancer (%)'
            }
        }]
    }
};

const strokeChart = new Chart(ctx1, {
    type: 'line',
    data: strokeData,
    options: strokeConfig
});

const lungChart = new Chart(ctx2, {
    type: 'line',
    data: lungData,
    options: lungConfig
});

const submit1 = document.getElementById("form1");
const x = document.getElementById("sex1");
const y = document.getElementById("bmi1");
console.log(x);

const submit2 = document.getElementById("form2");
const a = document.getElementById("sex2")
const b = document.getElementById("airpollution2")

function strokeFunc() {
    console.log("Stroke - Checked");
    console.log(x.value.split(","));
    strokeChart.data.datasets[0].data = y.value.split(",");
    strokeChart.data.labels = x.value.split(",");
    strokeChart.update();
};

function lungFunc() {
    console.log("Lung - Checked");
    console.log(a.value.split(","));
    lungChart.data.datasets[0].data = b.value.split(",");
    lungChart.data.labels = a.value.split(",");
    lungChart.update();
};

submit1.addEventListener('click', strokeFunc());
submit2.addEventListener('click', lungFunc())