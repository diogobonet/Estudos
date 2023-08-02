const  arr = ["Harry", "Rony", "Hermione", "Hagrid"]
console.log(arr)

// Adicionar Elementos (PUSH)
arr.push("Dumbledore")
console.log(arr)

// Unshift (Adicionar no começo do Array)
arr.unshift ("Dobby")
console.log(arr)

// Verificar o tamanho do array
const tamanho = arr.unshift ("Voldemort")
console.log("Verificando o tamanho do array: ", tamanho)

// Remover Elementos 
// (POP) (Remover no final do Elemento)
const ultimoElemento = arr.pop()
console.log(arr)
console.log("Removido: " + ultimoElemento)

// Shift (Remover no inicio do Elemento)
const primeiroElemento = arr.shift()
console.log(arr)
console.log(primeiroElemento)

// Pesquisar por um Elemento
// Includes
const inclui = arr.includes("Dobby")
console.log(inclui)

// IndexOf
const indice = arr.indexOf("Harry")
console.log(indice)

// Cortar e Concatenar
// slice 
const hogwarts = arr.slice(0, 2)
const outros = arr.slice(-4)
console.log(hogwarts)
console.log(outros)

// concat 
const ordem = hogwarts.concat(outros, "Severo", "Lupin")
console.log(ordem)

// Substituição dos Elementos
// splice
const a = ordem.splice(indice, 1, "Luna")
console.log(a)
console.log(ordem)

// Iterar sober os Elementos
for (let a = 0; a < ordem.length; a ++) {
    const elemento = ordem[a]
    console.log(elemento + " se encontra na posição " + a)
}