function fac(n) {
    if (n < 2) {
        return 1;
    } return (n * fac(n - 1));
}

console.log("RETURNING FACT...");
console.log(fac(1));
console.log(fac(3));
console.log(fac(5));

var facB = document.getElementById("facButton");

function runFac() {
  var facT = document.getElementById("facText");
  facT = facT.value;
  document.getElementById("facPara").innerHTML = fac(facT);
}

facB.addEventListener("click", () => runFac());

