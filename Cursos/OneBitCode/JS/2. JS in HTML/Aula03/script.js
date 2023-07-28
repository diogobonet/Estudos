/* OPERADORES DE COMPARAÇÃO  */
/* 
NO JS EXISTEM VÁRIOS OPERADORES DE COMPARAÇÃO

== E === // IGUAL E EXTRITAMENTE IGUAL

!= E !== // DIFERENTE E EXTRITAMENTE DIFERENTE

>, >=, <, <=  // MAIOR, MAIOR OU IGUAL, MENOR, MENOR OU IGUAL

*/

// Operadores de Igualdade

let comp1 = 3 == 3
console.log(comp1) // TRUE

comp1 = 4 == 3 // FALSE
console.log(comp1)

comp1 = 3 * 3 + 1 == 10 // TRUE
console.log(comp1)

comp1 = 10 === 10
console.log(comp1) // TRUE

comp1 = 10 === 11
console.log(comp1) // FALSE

comp1 = 10 === "10"
console.log(comp1) // FALSE 

/* O EXTRITAMENTE IGUAL COMPARA TAMBÉM OS TIPOS NA COMPARAÇÃO 
NA MAIORIA DAS VEZES É UTILIZADO PARA REALIZAR COMPARAÇÕES O EXTRITAMENTE IGUAL
*/

// Operadores de Desigualdade (Diferente)
console.log("=========")
comp1 = 10 != 10
console.log(comp1) // False

comp1 = 10 != 11
console.log(comp1) // True