let obj = {
    nome: "Diogo",
    idade: 18
    // propriedade: valor (string, número, bool)
}

console.log(obj.nome)

/* OUTRA FORMA DE CRIAR UM OBJETO */
let nome = "prop"
let objeto = {}

objeto.prop = "Olá, mundo"

console.log(objeto.prop)

console.log(objeto[nome]) // Referenciar uma váriavel que contém o nome de uma propriedade do objeto

/* Função */
let funcao = "log"
console[funcao]("Estou executando a função LOG")