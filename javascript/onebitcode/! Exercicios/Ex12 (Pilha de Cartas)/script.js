let opt = "Iniciando o baralho"
let carta = ""
let baralho = []

do {
    alert("Cartas que estão no seu baralho: " + baralho)
    opt = parseFloat(prompt("Escolha uma opção: \n 1) Adicionar carta \n 2) Puxar uma carta \n 3) Sair"))

    switch (opt) {
        case 1:
            carta = prompt("Nome da carta: ")
            baralho.push(carta)
            alert(carta + " carta adicionada ao baralho.")
            break
        case 2:
            let cartaPuxada = baralho.pop(carta)
            alert("Você puxou a carta: " + cartaPuxada)
            break
        case 3:
            alert("Finalizando...")
            break
    }

} while (opt != 3)