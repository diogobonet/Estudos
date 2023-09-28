let media = (...numbers) => {
    let valores = numbers.length
    let soma =  numbers.reduce((accum, num) => accum + num, 0)
    return soma / valores
}

let mediaPonderada = (...{number, peso}) => {
    let valores = number
    let media = number.reduce((num, peso) => num * peso, 0)
    return media / valores
}

console.log(media(12, 5, 9, 3, 4, 12, 3, 55))
console.log(mediaPonderada({}))