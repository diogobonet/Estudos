function addPlayer() {
    const nome = document.getElementById('nome').value
    const posicao = document.getElementById('position').value
    var numero = document.getElementById('number').value

    console.log(nome, posicao, numero)

    let opt = confirm(`Você confirma que quer adicionar o jogador ${nome}?`)

    if (opt){
        const nomeli = document.createElement('li')
        const posicaoli = document.createElement('li')
        const numeroli = document.createElement('li')
        nomeli.innerText = `Nome do jogador: ${nome}`
        posicaoli.innerText = `Posição do jogador: ${posicao}`
        numeroli.innerText = `Número da camisa: ${numero}`
        
        const ul = document.getElementById('players-list')
        ul.appendChild(nomeli)
        ul.appendChild(posicaoli)
        ul.appendChild(numeroli)
        ul.appendChild(document.createElement('br'))

        nome.value = ""
        posicao.value = ""
        numero.value = ""
    } else {
        alert("Não foi possivel cadastrar um novo jogador!")
    }
}


function removerPlayer() {
    const playertoRemove = document.getElementById('number-remove').value
    const playerNumber = document.getElementById("Número da camisa: " + numero)

    let opt = confirm(`Você confirma que quer adicionar o jogador ${playerNumber}?`)

    if (opt) {
        document.getElementById('players-list').removeChild(playertoRemove)
        document.getElementById('number-remove').value = ""
    } else {
        alert("Não foi possivel realizar essa operação!")
    }
}