let nome = prompt("Nome do piloto: ")
let velocidadeInicial = 0

let velocidade = parseFloat(prompt("Você deseja acelerar até quantos km/h? Exemplo: 75.5"))
let confirmacao = confirm(`Você realmente quer acelerar até ${velocidade}km/h`)

if (confirmacao == true) {
    velocidadeInicial += velocidade
    alert(`${nome}, você acelerou até ${velocidadeInicial}km/h`)
} else {
    alert(`${nome}, você decidiu não acelerar! 😉`)
}