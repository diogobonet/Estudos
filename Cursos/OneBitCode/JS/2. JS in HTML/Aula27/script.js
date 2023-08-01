/* O DO WHILE A PRIMEIRA VERIFICAÇÃO ACONTECE SOMENTE APÓS QUE O BLOCO FOR EXECUTADO UMA VEZ */
let velocidade = 0

do {
    alert("A velocidade do veiculo " + velocidade + "km/h")
    velocidade -= 20
} while (velocidade > 0)

alert("Velocidade final " + velocidade + "km/h")