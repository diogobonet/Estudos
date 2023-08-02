let opt = "Iniciando"
let paciente = []
let nome = ""

while (opt != 3) {
    for (a = 0; a < paciente.length; a++) {
        let name = paciente[a]
        alert(a + "° Paciente: " + name + "\n")
    }
    opt = parseFloat(prompt("Selecione uma opção: \n 1) Novo paciente \n 2) Consultar paciente \n 3) Sair"))
    switch (opt) {
        case 1:
            nome = prompt("Digite o nome do novo paciente: ")
            paciente.push(nome)
            break
        case 2:
            let consultando = paciente.shift()
            alert("Atendendo o cliente: " + consultando)
            break
        case 3:
            alert("Finalizando")
            break
    }
} 