// Armazenando uma função em uma variavel
const imprimirSoma = function (a, b){
    console.log(a + b)
}
imprimirSoma(2,3)

// Armazenando uma função arrow em uma variavel
const soma = (a, b) => {
    return a + b
}

console.log(soma(2,7))

// Retorno Implicito
const subtracao = (a, b) => a - b // Apenas uma sentença
console.log(subtracao(2,3))

// Com um unico parametro
const imprimir2 = a => console.log(a)
imprimir2(22)