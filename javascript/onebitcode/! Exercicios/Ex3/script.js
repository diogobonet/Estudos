const nome1 = window.prompt("Insira o modelo do carro 1:")
const xvel1 = window.prompt("Insira a velocidade do carro 1:")

const nome2 = window.prompt("Insira o modelo do carro 2:")
const yvel2 = window.prompt("Insira a velocidade do carro 2:")

const vel1 = parseFloat(xvel1)
const vel2 = parseFloat(yvel2)

if (vel1 > vel2) {
    window.alert("O " + nome1 + " é mais rápido que o " + nome2 + "!")
}

if (vel2 > vel1) {
    window.alert("O " + nome2  + " é mais rápido que o " + nome1 + "!")
}

else {
    window.alert("A velocidade dos dois carros foram iguais!")
}