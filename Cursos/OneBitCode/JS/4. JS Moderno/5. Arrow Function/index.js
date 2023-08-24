function normalSum(a, b) {
    return a + b
}

console.log(`Função normal = ${normalSum(2, 5)}`)

const anonSum = function (a, b) {
    return a + b
}

console.log(`Função anonima = ${anonSum(20, 5)}`)

const arrowFunc = (a, b) => {
    return a + b
}

console.log(`Função anonima = ${arrowFunc(30, 30)}`)

const arrowFuncMinus = (a, b) => a - b

console.log(arrowFuncMinus(5,2))

const towns = ['Prontera', 'Izlude', 'Payon', 'Alberta', 'Geffen', 'Morroc']

const startingP = towns.filter(town => town[0] === 'P')
console.log(startingP)