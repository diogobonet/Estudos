let quant = parseFloat(prompt("Qual a quantidade inicial de dinheiro disponivel?"))
let opt = ""

do {
    opt = prompt("Bem vindo ao Banco Bonet! \n 1) Adicionar dinheiro \n 2) Remover dinheiro \n 3) Sair")
    switch(opt) {
        case "1":
            quant += parseFloat(prompt("Quando dinheiro deseja adicionar?"))
            alert("Você agora tem: R$" + quant )
            break
         case "2":
            quant -= parseFloat(prompt("Quando dinheiro deseja remover?"))
            alert("Você agora tem: R$" + quant )
            break
        case "3":
            alert("Saindo...")
            break
        default:
            alert("Opção inválida!")
    }
} while(opt != "3")