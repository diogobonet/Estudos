function addInput() {
    const ul = document.getElementById("inputs")

    const newLi = document.createElement("li")
    newLi.innerText = "Novo input:"

    const newInput = document.createElement("input")
    newInput.type = "text"
    newInput.placeholder = "Olá, mundo"

    newLi.appendChild(newInput)
    ul.appendChild(newLi)
}