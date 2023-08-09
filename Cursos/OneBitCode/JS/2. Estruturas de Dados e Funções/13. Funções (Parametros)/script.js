function dobro(x) {
    console.log("O dobro de " + x + " é " + (x*2))
}
dobro(5)
dobro(7)
dobro()

function dizerOla(nome = "usuário") {
    console.log(`Olá ${nome}!`)
}

dizerOla("Diogo")
dizerOla()

function criarUsuario(nome, email, senha, tipo = "Usuário comum") {
    let user = {
        nome,
        email,
        senha,
        tipo
    }

    console.log(user)
}

criarUsuario("Diogo", "diogosobezak@gmail.com", "1234567")

function muitosParam(user) {
    user.nome,
    user.email,
    user.telefone
}

const dados = {
    nome: "",
    email: "",
    telefone: ""
}

muitosParam(dados)
