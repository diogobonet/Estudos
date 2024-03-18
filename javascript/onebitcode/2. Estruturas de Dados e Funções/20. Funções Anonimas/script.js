function somar(a,b) {
    return a + b
}

let operacao = somar

console.log(operacao(4, 5))

const subtrair = function (a, b) {
    return a - b
}

// console.log(subtrair(5,2))

operacao = function (a, b) {
    return a - b
}

console.log(operacao(37,16))

/* PERIGO */
olaMundo() 
oiMundo()

function olaMundo() {
    console.log("Olá, mundo")
}

const oiMundo = function () {
    console.log("Oi, mundo")
}