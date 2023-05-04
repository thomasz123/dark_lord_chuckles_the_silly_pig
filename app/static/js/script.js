function fact(n) {
    if (n < 2) {
        return 1;
    } return (n * fact(n - 1));
}

console.log("RETURNING FACT...");
console.log(fact(1));
console.log(fact(3));
console.log(fact(5));