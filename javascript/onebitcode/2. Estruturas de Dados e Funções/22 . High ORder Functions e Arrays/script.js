const personagens = [
    { nivel: 42, nome: "Thrall", raca: "Orc", classe: "Xamã" },
    { nivel: 28, nome: "Garrosh", raca: "Orc", classe: "Guerreiro" },
    { nivel: 35, nome: "Varok", raca: "Orc", classe: "Guerreiro" },
    { nivel: 35, nome: "Uther", raca: "Humano", classe: "Paladino" },
    { nivel: 26, nome: "Jaina", raca: "Humano", classe: "Maga" },
    { nivel: 39, nome: "Tyrande", raca: "Elfo Noturno", classe: "Sacerdotisa" },
    { nivel: 29, nome: "Muradin", raca: "Anão", classe: "Guerreiro" },
  ]


 // Map
 /* MAPEIA CADA ELEMENTO DE UM ARRAY ANTIGO, E PASSA PARA UM NOVO  */ 
const nomes = personagens.map(function (personagens) {
    return personagens.nome
})

console.log(nomes)

// Filter 
//  Filtrar um determinado valor dentro de um array

const orcs = personagens.filter(function (personagens) {
  return personagens.raca === "Orc"
})

console.log(orcs)

// Reduce
// Transformar um array em um outro elemento

const number = personagens.reduce(function (valor, personagem) {
  return valor + personagem.nivel
}, 0) // É preciso definir um Valor inicial

console.log(number)

const racas = personagens.reduce(function (valor, personagem) {
  if (valor[personagem.raca]) {
    valor[personagem.raca].push(personagem)
  } else {
    valor[personagem.raca] = [personagem]
  }

  return valor
})

console.log(racas)

// Sort
// Ordenar um array

const personagensOrdenados = personagens.slice().sort(function (a, b) {
  return a.nivel - b.nivel
})

console.log(personagensOrdenados)