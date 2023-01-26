// Par nome/valor | identificador/valor
const saudacao = "Olá!" // Contexto léxico 1

function exec() {
    const saudacao = "Oi!" // Contexto léxico 2
    return saudacao
}

const cliente = {
    nome: "Diogo",
    idade: "18",
    sexo: "Masculino",
    endereço: {
        rua: "Rua Cascavel",
        numero: "93",
        sobrado: "2"
    }
}

console.log(saudacao)
console.log(exec())
console.log(cliente)