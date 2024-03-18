function calcularMedia(a, b) {
    const media = (a + b) / 2
    return media
}

const resultado = calcularMedia(5, 7)

console.log(resultado)

function criarProduto(nome, preco) {
    const produto = {
        nome,
        preco,
        estoque: 1
    }

    return produto
}

console.log(criarProduto("Dell", 1200.50))

function  areaRetangular(base, altura) {
    return base * altura
}

console.log(areaRetangular(3, 5))
