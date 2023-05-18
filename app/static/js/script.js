const ctx = document.getElementById('myChart').getContext('2d');

const data = {
    labels: [0, 1, 2, 3, 4, 5],
        datasets: [{
            label: 'Heart Disease',
            data: [null, null, null, null, null],
            fill: false,
            borderColor: 'rgb(75, 192, 192)',
            tension: 0.1
        }]
};

const config = {
    scales: {
      xAxes: [{
          scaleLabel: {
            display: true,
            labelString: 'Age',
            font: {
              size: 24,
              weight: 'bold' // MOT WORKING
            }
          },
      }],
      yAxes: [{
          scaleLabel: {
            display: true,
            labelString: 'Likelihood of Heart Disease (%)'
          }
      }]
    }
};

const myChart = new Chart(ctx, {
    type: 'line',
    data: data,
    options: config
});

const sex = document.getElementById("sexC");
const heartdisease = document.getElementById("heartdiseaseC");
const bmi = document.getElementById("bmiC");
const smokingstatus = document.getElementById("smokingstatusC");
const stroke = document.getElementById("strokeC");

sex.addEventListener('change', function() {
    if (this.checked) {
        console.log("Sex - Checked");
        console.log(sex.value.split(","));
        myChart.data.datasets[0].data = sex.value.split(",");
        myChart.update();
    } else {
        console.log("Sex - Unchecked");
        myChart.data.datasets[0].data = [null, null, null, null, null];
        myChart.update();
    }
});

heartdisease.addEventListener('change', function() {
    if (this.checked) {
        console.log("Heart Disease - Checked");
        console.log(heartdisease.value.split(","));
        myChart.data.datasets[0].data = heartdisease.value.split(",");
        myChart.update();
    } else {
        console.log("Heart Disease - Unchecked");
        myChart.data.datasets[0].data = [null, null, null, null, null];
        myChart.update();
    }
});

bmi.addEventListener('change', function() {
  if (this.checked) {
      console.log("BMI - Checked");
      console.log(bmi.value.split(","));
      myChart.data.datasets[0].data = bmi.value.split(",");
      myChart.update();
  } else {
      console.log("BMI - Unchecked");
      myChart.data.datasets[0].data = [null, null, null, null, null];
      myChart.update();
  }
});

smokingstatus.addEventListener('change', function() {
  if (this.checked) {
      console.log("Smoking Status - Checked");
      console.log(smokingstatus.value.split(","));
      myChart.data.datasets[0].data = smokingstatus.value.split(",");
      myChart.update();
  } else {
      console.log("Smoking Status - Unchecked");
      myChart.data.datasets[0].data = [null, null, null, null, null];
      myChart.update();
  }
});

stroke.addEventListener('change', function() {
  if (this.checked) {
      console.log("Stroke - Checked");
      console.log(stroke.value.split(","));
      myChart.data.datasets[0].data = stroke.value.split(",");
      myChart.update();
  } else {
      console.log("Stroke - Unchecked");
      myChart.data.datasets[0].data = [null, null, null, null, null];
      myChart.update();
  }
});