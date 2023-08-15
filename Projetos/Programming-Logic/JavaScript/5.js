let nome = prompt("Qual é o nome da nave?")

let dobra = prompt("Deseja realizar a dobra? (Sim | Não)")

var numDobras = 0

while (dobra != "Não") {
    numDobras += 1
    dobra = prompt("Deseja realizar outra dobra? (Sim | Não)")
}

alert(`A nave ${nome}, realizou ${numDobras} dobras!`)