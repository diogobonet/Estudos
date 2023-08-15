function addContact() {
    const contactSection = document.getElementById('contacts-list');
    const h3 = document.createElement('h3');
    
    h3.innerText = "Contato:";
    
    const ul = document.createElement('ul');
    const nameli = document.createElement('li');
    const telefoneli = document.createElement('li');
    const enderecoli = document.createElement('li')
    

    nameli.innerText = "Nome: ";
    
    const nameInput = document.createElement('input');
    nameInput.type = "text";
    nameInput.placeholder = "Digite seu nome...";
    nameInput.name = 'fullname';
    nameli.appendChild(nameInput);
    ul.appendChild(nameli);
    
    telefoneli.innerText = "Telefone: "; // Corrigido de "Nome: "
    const phoneInput = document.createElement('input');
    phoneInput.type = "tel";
    phoneInput.placeholder = "Digite seu telefone...";
    phoneInput.name = 'telephone'; // Corrigido de 'telphone' para 'telephone'
    telefoneli.appendChild(phoneInput);
    ul.appendChild(telefoneli);

    const endereçoInput = document.createElement('input')
    endereçoInput.type = 'text'
    endereçoInput.placeholder = 'Digite o endereço'
    enderecoli.innerText = "Endereço: "
    enderecoli.appendChild(endereçoInput)
    ul.appendChild(enderecoli)
    ul.appendChild(document.createElement('br'))
    
    contactSection.appendChild(h3);
    contactSection.appendChild(ul);    
}

function removeContact() {
    const contactSection = document.getElementById('contacts-list');
    const titles = document.getElementsByTagName('h3')
    const contacts = document.getElementsByTagName('ul')

    contactSection.removeChild(titles[titles.length - 1])
    contactSection.removeChild(contacts[contacts.length - 1])
}   