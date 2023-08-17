const form = document.getElementById('form')
const addTech = document.getElementById('addTech')



addTech.addEventListener('click', function (ev) {
    ev.preventDefault()

    
    const ul = document.querySelector("#techForm")
    const li = document.createElement("li")
    const liRadio = document.createElement("li")
    const inputTech = document.createElement("input")
    const inputRadio1 = document.createElement("input")
    const inputRadio2 = document.createElement("input")
    const inputRadio3 = document.createElement("input")
    // Input - Text (Tecnologia)
    li.textContent = 'Nome da tecnologia: '
    inputTech.type = 'text'
    
    // Input - Radio
    inputRadio1.type = 'radio'
    inputRadio1.textContent = '0-2 anos'
    inputRadio1.value = '0-2 anos'
    inputRadio2.type = 'radio'
    inputRadio3.type = 'radio'
    liRadio.textContent = 'Tempo de experiencia: ' 
    li.appendChild(inputTech)
    liRadio.appendChild(inputRadio1)
    ul.appendChild(li)
    ul.appendChild(liRadio)
})