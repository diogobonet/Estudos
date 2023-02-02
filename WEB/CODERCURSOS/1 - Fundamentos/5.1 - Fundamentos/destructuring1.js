const pessoa = {
    nome: "Diogo",
    idade: "18",
    endereço: {
        rua: "João Blalalal",
        num: 2000
    }
}

const {nome, idade} = pessoa
console.log(nome ,idade)

const {nome:n, idade:i} = pessoa
console.log(n ,i)