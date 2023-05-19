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
              weight: 'bold' // NOT WORKING
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

var checkboxes = document.querySelectorAll("input[type=checkbox][name=settings]");
console.log(checkboxes);
let enabledSettings = [];

const sex = document.getElementById("sexC");
const heartdisease = document.getElementById("heartdiseaseC");
const bmi = document.getElementById("bmiC");
const smokingstatus = document.getElementById("smokingstatusC");
const stroke = document.getElementById("strokeC");

checkboxes.forEach(function(checkbox) {
    checkbox.addEventListener('change', function() {
        enabledSettings = 
            Array.from(checkboxes) // Convert checkboxes to an array to use filter and map.
            .filter(i => i.checked) // Use Array.filter to remove unchecked checkboxes.
            .map(i => i.value) // Use Array.map to extract only the checkbox values from the array of objects.
            
        console.log(enabledSettings)

        // 4 (ALL) OPTIONS
        if (enabledSettings.length == 4) {
            console.log("All - Checked");
            myChart.data.datasets[0].data = [0, 0, 0, 1, 0, 0]; //PUT TABLE VALUES HERE?
            myChart.update();
        }

        // 3 OPTIONS
        else if (enabledSettings[0] == "bmiC" && enabledSettings[1] == "smokingstatusC" && enabledSettings[2] == "strokeC") {
            console.log("BMI, Smoking Status, Stroke - Checked");
            myChart.data.datasets[0].data = [0, 0, 4, 0, 0, 0]; //PUT TABLE VALUES HERE?
            myChart.update();
        }
        else if (enabledSettings[0] == "sexC" && enabledSettings[1] == "smokingstatusC" && enabledSettings[2] == "strokeC") {
            console.log("Sex, Smoking Status, Stroke - Checked");
            myChart.data.datasets[0].data = [0, 0, 3, 0, 0, 0]; //PUT TABLE VALUES HERE?
            myChart.update();
        }
        else if (enabledSettings[0] == "sexC" && enabledSettings[1] == "bmiC" && enabledSettings[2] == "strokeC") {
            console.log("Sex, BMI, Stroke - Checked");
            myChart.data.datasets[0].data = [0, 0, 2, 0, 0, 0]; //PUT TABLE VALUES HERE?
            myChart.update();
        }
        else if (enabledSettings[0] == "sexC" && enabledSettings[1] == "bmiC" && enabledSettings[2] == "smokingstatusC") {
            console.log("Sex, BMI, Smoking Status - Checked");
            myChart.data.datasets[0].data = [0, 0, 1, 0, 0, 0]; //PUT TABLE VALUES HERE?
            myChart.update();
        }

        // 2 OPTIONS
        else if (enabledSettings[0] == "smokingstatusC" && enabledSettings[1] == "strokeC") {
            console.log("Smoking Status, Stroke - Checked");
            myChart.data.datasets[0].data = [0, 6, 0, 0, 0, 0]; //PUT TABLE VALUES HERE?
            myChart.update();
        }
        else if (enabledSettings[0] == "bmiC" && enabledSettings[1] == "strokeC") {
            console.log("BMI, Stroke - Checked");
            myChart.data.datasets[0].data = [0, 5, 0, 0, 0, 0]; //PUT TABLE VALUES HERE?
            myChart.update();
        }
        else if (enabledSettings[0] == "bmiC" && enabledSettings[1] == "smokingstatusC") {
            console.log("BMI, Smoking Status - Checked");
            myChart.data.datasets[0].data = [0, 4, 0, 0, 0, 0]; //PUT TABLE VALUES HERE?
            myChart.update();
        }
        else if (enabledSettings[0] == "sexC" && enabledSettings[1] == "strokeC" ) {
            console.log("Sex, Stroke - Checked");
            myChart.data.datasets[0].data = [0, 3, 0, 0, 0, 0]; //PUT TABLE VALUES HERE?
            myChart.update();
        }
        else if (enabledSettings[0] == "sexC" && enabledSettings[1] == "smokingstatusC") {
            console.log("Sex, Smoking Status - Checked");
            myChart.data.datasets[0].data = [0, 2, 0, 0, 0, 0]; //PUT TABLE VALUES HERE?
            myChart.update();
        }
        else if (enabledSettings[0] == "sexC" && enabledSettings[1] == "bmiC") {
            console.log("Sex, BMI - Checked");
            myChart.data.datasets[0].data = [0, 1, 0, 0, 0, 0]; //PUT TABLE VALUES HERE?
            myChart.update();
        }
        
        // 1 OPTION
        else if (enabledSettings[0] == "strokeC") {
            console.log("Stroke - Checked");
            myChart.data.datasets[0].data = [4, 0, 0, 0, 0, 0]; //PUT TABLE VALUES HERE?
            myChart.update();
        }
        else if (enabledSettings[0] == "smokingstatusC") {
            console.log("Smoking Status - Checked");
            myChart.data.datasets[0].data = [3, 0, 0, 0, 0, 0]; //PUT TABLE VALUES HERE?
            myChart.update();
        }
        else if (enabledSettings[0] == "bmiC") {
            console.log("BMI - Checked");
            myChart.data.datasets[0].data = [2, 0, 0, 0, 0, 0]; //PUT TABLE VALUES HERE?
            myChart.update();
        }
        else if (enabledSettings[0] == "sexC") {
            console.log("Sex - Checked");
            myChart.data.datasets[0].data = [1, 0, 0, 0, 0, 0]; //PUT TABLE VALUES HERE?
            myChart.update();
        }
        else {
            console.log("All - Unchecked");
            myChart.data.datasets[0].data = [null, null, null, null, null];
            myChart.update();
        }
    })
});