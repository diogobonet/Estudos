const turista = prompt("Qual o sei nome?")
let cidade = ""
let contagem = 0

let continuar = prompt("Você já visitou alguma cidade?")
while (continuar == "Não" || 'nao' || "não" || "Nao") {
    let cidade = prompt("Qual é o nome da cidade visitada?")
    cidade += contagem
}