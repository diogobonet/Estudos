let vagas = []
let opt = "" 
function menu() {
    while (opt != 6) {
        opt = parseInt(prompt("Sistema de Vagas \n1) Listar vagas disponiveis \n2) Criar uma nova vaga \n3) Visualizar uma vaga \n4) Inscrever um candidato em uma vaga \n5) Excluir uma vaga \n6) Sair"))
        switch (opt) {
            case 1:
                listarVagas()
                break
            case 2:
                novaVaga()
                break
            case 3:
                exibirVaga()
                break
            case 4:
                inscreverCandidato()
                break
            case 5:
                excluirVaga()
                break
            case 6:
                alert("Saindo da aplicação...")
                break
        }
    } 
}

function listarVagas() {
    const vagasEmTexto = vagas.reduce(function (textoFinal, vaga, indice) {
        textoFinal += indice + ". "
        textoFinal += vaga.nome + ". "
        textoFinal += " (" + vaga.candidatos.length + " candidatos)"
    }, "")

    alert(vagasEmTexto)
}

function novaVaga() {
    const nome = prompt("Informe um nome para a vaga:")
    const descricao = prompt("Informe uma descrição para a vaga")
    const dataLimite = prompt("Informe uma data limite (dd/mm/aaaa)")
    
    const confirmacao = confirm("Você deseja salvar essa vaga? \n Nome: " + nome + "\nDescrição:" + descricao + "Data limite: " + dataLimite)

    if (confirmacao) {
        const novaVaga = { nome, descricao, dataLimite, candidatos: [] }
        vagas.push(novaVaga)
        alert("Vaga criada!")
    } else {
        alert("Não foi possivel criar a vaga.")
    }
}

function exibirVaga() {
    const indice = parseInt(prompt("Informe o indice da vaga que deseja exibir:"))
    const vaga = vagas[indice]

    const candidatosEmTexto = vaga.candidatos.reduce(function (textoFinal, candidato) {
        return textoFinal + "\n - " + candidato
    })

    alert("Vaga número: " + indice + "\nNome: " + vaga.nome + "\n Descrição: " + vaga.descricao + "\n Data limite:" + vaga.dataLimite + "\nQuantidade de candidatos: " + vaga.candidatos.length + "\nCandidatos inscritos: " + candidatosEmTexto)
}

function inscreverCandidato() {
    const candidato = prompt("Informe o nome do candidato: ")
    const indice = prompt("Informe o indice da vaga para qual o candidato quer se inscrever: ")
    const vaga = vagas[indice]

    const confirmacao = confirm(`Deseja confirmar a inscrição do candidato ${candidato} a essa vaga?`)

    if (confirmacao ==  true) {
        vaga.candidatos.push(candidato)
        alert("Inscrição realizada!")
    }
}

function excluirVaga() {
    const indice  = prompt("Informe o indice da vaga que deseja excluir:")
    const vaga = vagas[indice]

    const confirmacao = confirm(`Tem certeza que deseja excluir a vaga: ${vaga}`)

    if (confirmacao) {
        vagas.splice(indice, 1)
        alert("Vaga excluída")
    }
}

menu()