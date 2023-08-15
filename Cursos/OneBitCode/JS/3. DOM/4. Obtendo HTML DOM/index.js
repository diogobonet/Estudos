function show() {
    // Apenas um elemento
    let contactList = document.getElementById('contact-list') // Selecionar apenas pelo ID (único)
    console.log(contactList)

    // HTML Collecion
    let listElements = document.getElementsByTagName("li") // Selecionar pelas tags do HTML (HTML COLLECTION)
    console.log(listElements)

    let contactInputs = document.getElementsByClassName('contact-input') // Selecionar pelo nome da classe
    console.log(contactInputs)

    // NodeList
    let names = document.getElementsByName('contact1') // Retorna uma NODELIST?, mas seleciona pelo nome
    console.log(names)

    let contacts = document.querySelectorAll('#contact-list > li > label') // Seletor usando queries, sendo possivel referenciar todos os elementos dentro de outros elementos
    console.log(contacts)

    // Outra forma de usar o queryselector
    let firstContact = document.querySelector('#contact-list > li > label') // Ele vai retornar somente a primeira aparição do seletor
    console.log(firstContact) 
}