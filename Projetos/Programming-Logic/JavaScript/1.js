function dadosUser() {
    alert("Bem-vindo! A seguir pediremos que informe alguns dados!")

    let nome = prompt("Digite o seu nome: ")
    let idade = parseInt(prompt("Digite a sua idade:"))
    let confirmacao = confirm(`Essa ("${idade}") é realmente sua idade?`)
    
    alert(`Nome: ${nome} \nIdade: ${idade} \nConfirmação idade: ${confirmacao}`)

}

dadosUser()