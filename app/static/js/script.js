const ctx = document.getElementById('strokeChart').getContext('2d');

const data = {
    labels: [0, 1, 2, 3, 4, 5],
        datasets: [{
            label: 'Stroke',
            data: [null, null, null, null, null, null],
            fill: false,
            borderColor: 'rgb(75, 192, 192)',
            tension: 0.1
        }]
};

const config = {
    scales: {
        xAxes: [{
            ticks: {
                stepSize: 1,
                min: 0,
                max: 100
            },
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
            ticks: {
                stepSize: 1,
                min: 0,
                max: 100
            },
            scaleLabel: {
                display: true,
                labelString: 'Likelihood of Heart Disease (%)'
            }
        }]
    }
};

const strokeChart = new Chart(ctx, {
    type: 'line',
    data: data,
    options: config
});

var checkboxes = document.querySelectorAll("input[type=checkbox][name=settings]");
console.log(checkboxes);
let enabledSettings = [];

const sex = document.getElementById("sex1");
const heartdisease = document.getElementById("heartdiseaseC");
const bmi = document.getElementById("bmi1");
const smokingstatus = document.getElementById("smokingstatus1");
const stroke = document.getElementById("heartdisease1");

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
            strokeChart.data.datasets[0].data = [0, 0, 0, 1, 0, 0]; //PUT TABLE VALUES HERE?
            strokeChart.update();
        }

        // 3 OPTIONS
        else if (enabledSettings[0] == "bmi1" && enabledSettings[1] == "smokingstatus1" && enabledSettings[2] == "heartdisease1") {
            console.log("BMI, Smoking Status, Heart Disease - Checked");
            strokeChart.data.datasets[0].data = [0, 0, 4, 0, 0, 0]; //PUT TABLE VALUES HERE?
            strokeChart.update();
        }
        else if (enabledSettings[0] == "sex1" && enabledSettings[1] == "smokingstatus1" && enabledSettings[2] == "heartdisease1") {
            console.log("Sex, Smoking Status, Heart Disease - Checked");
            strokeChart.data.datasets[0].data = [0, 0, 3, 0, 0, 0]; //PUT TABLE VALUES HERE?
            strokeChart.update();
        }
        else if (enabledSettings[0] == "sex1" && enabledSettings[1] == "bmi1" && enabledSettings[2] == "heartdisease1") {
            console.log("Sex, BMI, Heart Disease - Checked");
            strokeChart.data.datasets[0].data = [0, 0, 2, 0, 0, 0]; //PUT TABLE VALUES HERE?
            strokeChart.update();
        }
        else if (enabledSettings[0] == "sex1" && enabledSettings[1] == "bmi1" && enabledSettings[2] == "smokingstatus1") {
            console.log("Sex, BMI, Smoking Status - Checked");
            strokeChart.data.datasets[0].data = [0, 0, 1, 0, 0, 0]; //PUT TABLE VALUES HERE?
            strokeChart.update();
        }

        // 2 OPTIONS
        else if (enabledSettings[0] == "smokingstatus1" && enabledSettings[1] == "heartdisease1") {
            console.log("Smoking Status, Heart Disease - Checked");
            strokeChart.data.datasets[0].data = [0, 6, 0, 0, 0, 0]; //PUT TABLE VALUES HERE?
            strokeChart.update();
        }
        else if (enabledSettings[0] == "bmi1" && enabledSettings[1] == "heartdisease1") {
            console.log("BMI, Heart Disease - Checked");
            strokeChart.data.datasets[0].data = [0, 5, 0, 0, 0, 0]; //PUT TABLE VALUES HERE?
            strokeChart.update();
        }
        else if (enabledSettings[0] == "bmi1" && enabledSettings[1] == "smokingstatus1") {
            console.log("BMI, Smoking Status - Checked");
            strokeChart.data.datasets[0].data = [0, 4, 0, 0, 0, 0]; //PUT TABLE VALUES HERE?
            strokeChart.update();
        }
        else if (enabledSettings[0] == "sex1" && enabledSettings[1] == "heartdisease1" ) {
            console.log("Sex, Heart Disease - Checked");
            strokeChart.data.datasets[0].data = [0, 3, 0, 0, 0, 0]; //PUT TABLE VALUES HERE?
            strokeChart.update();
        }
        else if (enabledSettings[0] == "sex1" && enabledSettings[1] == "smokingstatus1") {
            console.log("Sex, Smoking Status - Checked");
            strokeChart.data.datasets[0].data = [0, 2, 0, 0, 0, 0]; //PUT TABLE VALUES HERE?
            strokeChart.update();
        }
        else if (enabledSettings[0] == "sex1" && enabledSettings[1] == "bmi1") {
            console.log("Sex, BMI - Checked");
            strokeChart.data.datasets[0].data = [0, 1, 0, 0, 0, 0]; //PUT TABLE VALUES HERE?
            strokeChart.update();
        }
        
        // 1 OPTION
        else if (enabledSettings[0] == "heartdisease1") {
            console.log("Heart Disease - Checked");
            strokeChart.data.datasets[0].data = [4, 0, 0, 0, 0, 0]; //PUT TABLE VALUES HERE?
            strokeChart.update();
        }
        else if (enabledSettings[0] == "smokingstatus1") {
            console.log("Smoking Status - Checked");
            strokeChart.data.datasets[0].data = [3, 0, 0, 0, 0, 0]; //PUT TABLE VALUES HERE?
            strokeChart.update();
        }
        else if (enabledSettings[0] == "bmi1") {
            console.log("BMI - Checked");
            strokeChart.data.datasets[0].data = [2, 0, 0, 0, 0, 0]; //PUT TABLE VALUES HERE?
            strokeChart.update();
        }
        else if (enabledSettings[0] == "sex1") {
            console.log("Sex - Checked");
            strokeChart.data.datasets[0].data = [1, 0, 0, 0, 0, 0]; //PUT TABLE VALUES HERE?
            strokeChart.update();
        }
        else {
            console.log("All - Unchecked");
            strokeChart.data.datasets[0].data = [null, null, null, null, null, null];
            strokeChart.update();
        }
    })
});

var db = openDatabase('heart.db', '1.0', 'my first database', 5000*7);
console.log(db);
db.transaction(function (tx) {
    tx.executeSql('CREATE TABLE IF NOT EXISTS heart (id INTEGER, gender TEXT, age INTEGER, disease INTEGER, bmi INTEGER, status TEXT, stroke INTEGER)');
    // tx.executeSql('SELECT * FROM heart', [], function (tx, results) {
    //     var len = results.rows.length, i;
    //     for (i = 0; i < len; i++) {
    //         console.log(results.rows.item(i).text);
    //     }
    //     });
});

db.transaction(function (tx) { 
    tx.executeSql('SELECT * FROM heart', [], function (tx, results) {
        var len = results.rows.length, i;
        for (i = 0; i < len; i++) {
            console.log(results.rows.item(i).text);
        }
        });
    // tx.executeSql('SELECT * FROM LOGS', [], function (tx, results) { 
    //    var len = results.rows.length, i; 
    //    msg = "<p>Found rows: " + len + "</p>"; 
    //    document.querySelector('#status').innerHTML +=  msg; 
   
    //    for (i = 0; i < len; i++) { 
    //       console.log(results.rows.item(i).log ); 
    //    } 
   
    // }, null); 
 });

// //write me a function that will display all elements in my databse in the console
// db.transaction(function (tx) {
//     tx.executeSql('SELECT * FROM heart', [], function (tx, results) {
//         var len = results.rows.length, i;
//         for (i = 0; i < len; i++) {
//             console.log(results.rows.item(i));
//         }
//         });
// }
