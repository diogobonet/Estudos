const form = document.getElementById('form')
const addTech = document.getElementById('addTech')



addTech.addEventListener('click', function (ev) {
    ev.preventDefault()

    
    const ul = document.querySelector("#techForm")
    const li = document.createElement("li")
    const liRadio = document.createElement("li")
    const inputTech = document.createElement("input")
    const inputRadio = document.createElement("input")
    // Input - Text (Tecnologia)
    li.textContent = 'Nome da tecnologia: '
    inputTech.type = 'text'
    
    // Input - Radio
    inputRadio.type = 'radio'
    liRadio.textContent = 'Tempo de experiencia: ' 
    li.appendChild(inputTech)
    liRadio.appendChild(inputRadio)
    ul.appendChild(li)
    ul.appendChild(liRadio)
})