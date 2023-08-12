let vagas = [{
    nome: "",
    dataLimite: ""
}]
let opt = "" 
function menu() {
    while (opt != 6) {
        opt = parseInt(prompt("Sistema de Vagas \n1) Listar vagas disponiveis \n2) Criar uma nova vaga \n3) Visualizar uma vaga \n4) Inscrever um candidato em uma vaga \n5) Excluir uma vaga \n6) Sair"))
        switch (opt) {
            case 1:
                listarVagas()
                break
            case 2:
                let nome = prompt("Digite o nome: ")
                let dataLimite = prompt("Digite a data limite: ")
                vagas.push(nome)
                vagas.push(dataLimite)
                console.log(vagas)
                break
            case 3:
                break
            case 4:
                break
            case 5:
                break
            case 6:
                print("Oi")
                break
        }
    } 
}


function listarVagas() {
    return vagas.forEach(exibirElemento)
}

function exibirElemento(indice, elemento, array) {
    alert(
        indice,
        elemento,
        array
    )
}
menu()
