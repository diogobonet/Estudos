const valores = [7.7, 8.9, 6.3, 9.2] // Valores Literais
console.log(valores[0], valores[3])
valores[4] =10
console.log(valores)

valores.push({id: 3}, false. null, "teste") // Adiciona novos valores com tipagem diferente
console.log(valores)
console.log(valores.pop()) // Deleta o ultimo item da lista
delete valores[0] // Deleta o valor pela indexação
console.log(valores)