/*
"For" também é uma estrutura de repetição só que, para abreviar o código em casos que seguem essas estrutura especifica

Possui três: 
Inicialização: expressão executada antes de tudo
Condição: condção semelhante ao while, é testada antes do bloco de repetição
Finalização: expressão executada após o bloco de repetição

PARA inicialização; finalização FAÇA alguma coisa

for (inicialização; condição; finalização;)
*/

let nome = "Diogo"
for (let indice = 0; indice < nome.length; indice--) {
    console.log(nome[indice])
}

/*/for (let i = 1; i <= 10; i++) {
    alert(i)
}
*/
