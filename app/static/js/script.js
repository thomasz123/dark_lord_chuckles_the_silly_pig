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

function displayResults() {
  var files = document.querySelector('#file').files;

  if (files.length > 0) {
    var file = files[0];
    console.log(file);

    var reader = new FileReader(); 
    reader.readAsText(file);

    reader.onload = function(event) {
      var csvdata = event.target.result;
      console.log(csvdata);

      var rowData = csvdata.split('\n');
      var tbodyEl = document.getElementById('tblcsvdata').getElementsByTagName('tbody')[0];
      tbodyEl.innerHTML = "";

      for (var row = 1; row < rowData.length; row++) {
        var newRow = tbodyEl.insertRow();
        rowColData = rowData[row].split(',');

        for (var col = 0; col < rowColData.length; col++) {
              var newCell = newRow.insertCell();
              newCell.innerHTML = rowColData[col];
        }
      }
    };
  } else {
    alert("Please select a file.");
  }

}