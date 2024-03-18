var persname1 = window.prompt("Digite o nome do personagem 1:")
var perspower1 = parseFloat(window.prompt("Digite o poder de ataque:"))

let persname2 = window.prompt("Digite o nome do personagem 2:")
let perslifepoints = parseFloat(window.prompt("Qual a quantidade de ponto de vida do" + persname2 + "?"))
let perspowerdefence = parseFloat(window.prompt("Qual o poder de defesa dele?"))
let escudo = confirm("O personagem possui escudo?")

if (perspower1 > perspowerdefence && escudo == false) {
    var dano = perspower1 - perspowerdefence
}

else if (perspower1 > perspowerdefence && escudo == true) {
    var dano = (perspower1 - perspowerdefence) / 2
}

else if (perspower1 < perspowerdefence) {
    var dano = 0
}

perslifepoints -= dano

console.log(persname1 + "Poder de ataque:" + perspower1)

console.log(persname2 + "Pontos de vida: " + perslifepoints + "Poder de defesa: " + perspowerdefence + "Possui escudo?" + escudo)