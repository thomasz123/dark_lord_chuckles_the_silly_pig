// function myFunc() {
//     console.log("js");
//     console.log(Object.keys(keys));
// }

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
                labelString: 'Age',
                font: {
                    size: 24,
                    weight: 'bold' // NOT WORKING
                }
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
                labelString: 'Age',
                font: {
                    size: 24,
                }
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

const submit1 = document.getElementById("form1");
const x = document.getElementById("sex1");
const y = document.getElementById("bmi1");
console.log(x);

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
    lungChart.data.datasets[0].data = y.value.split(",");
    lungChart.data.labels = a.value.split(",");
    lungChart.update();
};

submit1.addEventListener('click', strokeFunc());

const lungChart = new Chart(ctx2, {
    type: 'line',
    data: lungData,
    options: lungConfig
});

const submit2 = document.getElementById("form2");
const a = document.getElementById("sex2")


submit2.addEventListener('click', lungFunc())
// var checkboxes = document.querySelectorAll("input[type=checkbox][name=settings]");
// console.log(checkboxes);
// let enabledSettings = [];

// let strokeform = document.forms["strokeform"];
// strokeform.addEventListener("strokesubmit", strokeVals);

// function getVals(event){
//     event.preventDefault();
//     let idk = document.querySelectorAll(".stroke");
//     let idk2 = [];
//     for (let settings of idk){
//         if(settings.checked == true){
//             idk2.push(settings.value);
//         }
//     }
// }

// const sex = document.getElementById("sex1");
// const heartdisease = document.getElementById("heartdiseaseC");
// const bmi = document.getElementById("bmi1");
// const smokingstatus = document.getElementById("smokingstatus1");
// const stroke = document.getElementById("heartdisease1");

// checkboxes.forEach(function(checkbox) {
//     checkbox.addEventListener('change', function() {
//         enabledSettings = 
//             Array.from(checkboxes)
//             .filter(i => i.checked)
//             .map(i => i.value)
            
//         console.log(enabledSettings)

//         // 4 (ALL) OPTIONS
//         if (enabledSettings[0] == "sex1" && enabledSettings[1] == "bmi1" && enabledSettings[2] == "smokingstatus1" && enabledSettings[3] == "heartdisease1") {
//             console.log("All Stroke - Checked");
//             strokeChart.data.datasets[0].data = [0, 0, 0, 1, 0, 0]; //PUT TABLE VALUES HERE?
//             strokeChart.update();
//         }

//         // 3 OPTIONS
//         else if (enabledSettings[0] == "bmi1" && enabledSettings[1] == "smokingstatus1" && enabledSettings[2] == "heartdisease1") {
//             console.log("BMI, Smoking Status, Heart Disease - Checked");
//             strokeChart.data.datasets[0].data = [0, 0, 4, 0, 0, 0]; //PUT TABLE VALUES HERE?
//             strokeChart.update();
//         }
//         else if (enabledSettings[0] == "sex1" && enabledSettings[1] == "smokingstatus1" && enabledSettings[2] == "heartdisease1") {
//             console.log("Sex, Smoking Status, Heart Disease - Checked");
//             strokeChart.data.datasets[0].data = [0, 0, 3, 0, 0, 0]; //PUT TABLE VALUES HERE?
//             strokeChart.update();
//         }
//         else if (enabledSettings[0] == "sex1" && enabledSettings[1] == "bmi1" && enabledSettings[2] == "heartdisease1") {
//             console.log("Sex, BMI, Heart Disease - Checked");
//             strokeChart.data.datasets[0].data = [0, 0, 2, 0, 0, 0]; //PUT TABLE VALUES HERE?
//             strokeChart.update();
//         }
//         else if (enabledSettings[0] == "sex1" && enabledSettings[1] == "bmi1" && enabledSettings[2] == "smokingstatus1") {
//             console.log("Sex, BMI, Smoking Status - Checked");
//             strokeChart.data.datasets[0].data = [0, 0, 1, 0, 0, 0]; //PUT TABLE VALUES HERE?
//             strokeChart.update();
//         }

//         // 2 OPTIONS
//         else if (enabledSettings[0] == "smokingstatus1" && enabledSettings[1] == "heartdisease1") {
//             console.log("Smoking Status, Heart Disease - Checked");
//             strokeChart.data.datasets[0].data = [0, 6, 0, 0, 0, 0]; //PUT TABLE VALUES HERE?
//             strokeChart.update();
//         }
//         else if (enabledSettings[0] == "bmi1" && enabledSettings[1] == "heartdisease1") {
//             console.log("BMI, Heart Disease - Checked");
//             strokeChart.data.datasets[0].data = [0, 5, 0, 0, 0, 0]; //PUT TABLE VALUES HERE?
//             strokeChart.update();
//         }
//         else if (enabledSettings[0] == "bmi1" && enabledSettings[1] == "smokingstatus1") {
//             console.log("BMI, Smoking Status - Checked");
//             strokeChart.data.datasets[0].data = [0, 4, 0, 0, 0, 0]; //PUT TABLE VALUES HERE?
//             strokeChart.update();
//         }
//         else if (enabledSettings[0] == "sex1" && enabledSettings[1] == "heartdisease1" ) {
//             console.log("Sex, Heart Disease - Checked");
//             strokeChart.data.datasets[0].data = [0, 3, 0, 0, 0, 0]; //PUT TABLE VALUES HERE?
//             strokeChart.update();
//         }
//         else if (enabledSettings[0] == "sex1" && enabledSettings[1] == "smokingstatus1") {
//             console.log("Sex, Smoking Status - Checked");
//             strokeChart.data.datasets[0].data = [0, 2, 0, 0, 0, 0]; //PUT TABLE VALUES HERE?
//             strokeChart.update();
//         }
//         else if (enabledSettings[0] == "sex1" && enabledSettings[1] == "bmi1") {
//             console.log("Sex, BMI - Checked");
//             strokeChart.data.datasets[0].data = [0, 1, 0, 0, 0, 0]; //PUT TABLE VALUES HERE?
//             strokeChart.update();
//         }
        
//         // 1 OPTION
//         else if (enabledSettings[0] == "heartdisease1") {
//             console.log("Heart Disease - Checked");
//             strokeChart.data.datasets[0].data = [4, 0, 0, 0, 0, 0]; //PUT TABLE VALUES HERE?
//             strokeChart.update();
//         }
//         else if (enabledSettings[0] == "smokingstatus1") {
//             console.log("Smoking Status - Checked");
//             strokeChart.data.datasets[0].data = [3, 0, 0, 0, 0, 0]; //PUT TABLE VALUES HERE?
//             strokeChart.update();
//         }
//         else if (enabledSettings[0] == "bmi1") {
//             console.log("BMI - Checked");
//             strokeChart.data.datasets[0].data = [2, 0, 0, 0, 0, 0]; //PUT TABLE VALUES HERE?
//             strokeChart.update();
//         }
//         else if (enabledSettings[0] == "sex1") {
//             console.log("Sex - Checked");
//             strokeChart.data.datasets[0].data = [1, 0, 0, 0, 0, 0]; //PUT TABLE VALUES HERE?
//             strokeChart.update();
//         }
//         else {
//             console.log("All - Unchecked");
//             strokeChart.data.datasets[0].data = [null, null, null, null, null, null];
//             strokeChart.update();
//         }
//     })
// });

// var db = openDatabase('heart.db', '1.0', 'my first database', 5000*7);
// console.log(db);
// db.transaction(function (tx) {
//     tx.executeSql('CREATE TABLE IF NOT EXISTS heart (id INTEGER, gender TEXT, age INTEGER, disease INTEGER, bmi INTEGER, status TEXT, stroke INTEGER)');
//     // tx.executeSql('SELECT * FROM heart', [], function (tx, results) {
//     //     var len = results.rows.length, i;
//     //     for (i = 0; i < len; i++) {
//     //         console.log(results.rows.item(i).text);
//     //     }
//     //     });
// });

// db.transaction(function (tx) { 
//     tx.executeSql('SELECT * FROM heart', [], function (tx, results) {
//         var len = results.rows.length, i;
//         for (i = 0; i < len; i++) {
//             console.log(results.rows.item(i).text);
//         }
//         });
//     // tx.executeSql('SELECT * FROM LOGS', [], function (tx, results) { 
//     //    var len = results.rows.length, i; 
//     //    msg = "<p>Found rows: " + len + "</p>"; 
//     //    document.querySelector('#status').innerHTML +=  msg; 
   
//     //    for (i = 0; i < len; i++) { 
//     //       console.log(results.rows.item(i).log ); 
//     //    } 
   
//     // }, null); 
//  });

// // //write me a function that will display all elements in my databse in the console
// // db.transaction(function (tx) {
// //     tx.executeSql('SELECT * FROM heart', [], function (tx, results) {
// //         var len = results.rows.length, i;
// //         for (i = 0; i < len; i++) {
// //             console.log(results.rows.item(i));
// //         }
// //         });
// // }
