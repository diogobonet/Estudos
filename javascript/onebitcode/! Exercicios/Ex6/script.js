const turista = prompt("Qual o sei nome?")
let cidade = ""
let contagem = 0

let continuar = prompt("Você já visitou alguma cidade?")
while (continuar === "Sim") {
    let cidade = prompt("Qual é o nome da cidade visitada?")
    cidade += "- " + cidade + "\n"
    contagem++
    continuar = prompt("Você já visitou alguma outra cidade?")
}

alert("O turista " + turista + " \n Quantidade de cidades visitadas: " + contagem + "\n Cidades visitadas: \n" + cidade)