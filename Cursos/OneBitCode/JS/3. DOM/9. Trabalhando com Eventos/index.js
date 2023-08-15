const button = document.getElementById('register-button')

// addEventListener() serve para adicionar um ouvidor de eventos. Adicionar uma funcionalidade par ao botão e executando toda a vez que for executado
button.addEventListener('click', function () { 
    alert("Botão clicado")
})

button.addEventListener('click', register)

function register(ev) {
    console.log(ev)
    const sectionElement = ev.currentTarget.parentNode
    const username = sectionElement.children.username.value
    const password = sectionElement.children.password.value
    const passwordConfirmation = sectionElement.children.passwordConfirmation.value

    if (password == passwordConfirmation) {
        alert(`Usuário ${username} registrado!`)
    } else {
        alert("Senhas não conferem!")
    }
}

function removeEvent() {
    button.removeEventListener('click', register)
    alert("Evento removido!")
}   
