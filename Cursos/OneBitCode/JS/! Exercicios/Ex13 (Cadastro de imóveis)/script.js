let opt = ""
let imoveis = 0
let obj = {  }
let imovel =  []

while (opt != 3) {
    opt = parseInt(prompt("Total de imóveis: "+ imoveis + "\nEscolha uma opção: \n1) Salvar imóvel \n2) Objeto \n3) Sair"))
    switch (opt) {
        case 1:
            console.log(obj)
            obj.nomeProp = prompt("Digite o nome do proprietário: ") 
            obj.quantQ = parseInt(prompt("Digite a quantidade de quartos: "))
            obj.quantB = parseInt(prompt("Digite a quantidade de banheiros: "))
            obj.garage = prompt("Possui garagem? OK = Sim | Cancelar = Não")

            const confirmacao = confirm("Salvar esse imovel?")

            if (confirmacao) {
                imovel.push(obj)
                imoveis += 1
            }
            break
        case 2:
            for (i = 0; i <= imovel.length; i++) {
                alert(imovel[i].nomeProp)
                alert(imovel[i].quantQ)
                alert(imovel[i].quantB)
                alert(imovel[i].garage)
            }
            break
        case 3:
            alert("Saindo...")
            break
        default:
            ("Opção inválida! Tente novamente!")
            break
    }
}