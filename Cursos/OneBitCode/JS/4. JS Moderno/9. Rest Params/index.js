function sum(...numbers) {
    return numbers.reduce((accum, num) => accum + num, 0)
}

console.log(sum(25, 25))