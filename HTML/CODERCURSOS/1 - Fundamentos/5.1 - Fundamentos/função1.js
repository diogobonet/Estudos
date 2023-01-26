// Função sem retorno (Com parametros)
function imprimirSoma(a, b) {
    console.log(a + b)
}
imprimirSoma(2, 3)
// Função com retorno
function soma (a,b = 3) {
    return a + b
}
console.log(soma(2,9))