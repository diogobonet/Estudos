// Passar uma função qualquer como parametro de uma função!

function mult(a, b) {
    return a * b
}

function calcular(mult) {
    mult -= 1
    return mult
}

console.log(calcular(mult(5, 5)))

calcular(9, 4)

function exibirElemento(elemento, indice, array) {
    console.log(
        elemento,
        indice,
        array)
}

let lista = ["Maça", "Banana", "Pera", "Mamao"]

for (i = 0; i < lista.length; i++) {
    exibirElemento(lista[i], i , lista)
}

lista.forEach(exibirElemento)

lista.forEach(function (elemento, indice, array) {
    console.log(
        elemento,
        indice,
        array
    )
})