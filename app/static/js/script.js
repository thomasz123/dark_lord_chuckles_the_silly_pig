const data = {
  'React': 185134,
  'Vue': 195514,
  'Angular': 80460,
  'Svelte': 57022,
  'Ember.js': 22165,
  'Backbone.js': 27862
};

const ctx = document.getElementById('myChart').getContext('2d');

const myChart = new Chart(ctx, {
  type: 'bar',
  data: {
    labels: Object.keys(data),
    datasets: [
      {
        label: 'Number of GitHub Stars',
        data: Object.values(data),
      },
    ],
  },
});

// function fac(n) {
//     if (n < 2) {
//         return 1;
//     } return (n * fac(n - 1));
// }

// console.log("RETURNING FACT...");
// console.log(fac(1));
// console.log(fac(3));
// console.log(fac(5));

// var facB = document.getElementById("facButton");

// function runFac() {
//   var facT = document.getElementById("facText");
//   facT = facT.value;
//   document.getElementById("facPara").innerHTML = fac(facT);
// }

// facB.addEventListener("click", () => runFac());


// import { createRequire } from 'module';
// const require = createRequire(import.meta.url);

// function displayQuestionnaire() {
//   var sqlite3 = require('sqlite3').verbose();
//   let db = new sqlite3.Database('../../question.db');
//   let sql = `SELECT height FROM questionnaire;`;

//   db.all(sql, [], (err, rows) => {
//     if (err) {
//       throw err;
//     }
//     rows.forEach((row) => {
//       console.log(row.name);
//     });
//   });
//   db.close();
// }


// function displayResults() {
//   var files = document.querySelector('#file').files;

//   if (files.length > 0) {
//     var file = files[0];
//     console.log(file);

//     var reader = new FileReader(); 
//     reader.readAsText(file);

//     reader.onload = function(event) {
//       var csvdata = event.target.result;
//       console.log(csvdata);

//       var rowData = csvdata.split('\n');
//       var tbodyEl = document.getElementById('tblcsvdata').getElementsByTagName('tbody')[0];
//       tbodyEl.innerHTML = "";

//       for (var row = 1; row < rowData.length; row++) {
//         var newRow = tbodyEl.insertRow();
//         rowColData = rowData[row].split(',');

//         for (var col = 0; col < rowColData.length; col++) {
//               var newCell = newRow.insertCell();
//               newCell.innerHTML = rowColData[col];
//         }
//       }
//     };
//   } else {
//     alert("Please select a file.");
//   }
// }