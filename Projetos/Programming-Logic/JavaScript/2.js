let nomeVelha = prompt("O nome da pessoa mais velha: ")
let idadeVelha = parseInt(prompt("A idade da pessoa mais velha: "))

let nomeNova = prompt("O nome da pessoa mais nova: ")
let idadeNova = parseInt(prompt("A idade da pessoa mais nova:"))

let diferenca = idadeVelha - idadeNova


alert(`A ${nomeVelha} é mais velha, possui ${idadeVelha}.\nDiferença de idade ${diferenca}`)