let media = (...numbers) => {
    let valores = numbers.length
    let soma =  numbers.reduce((accum, num) => accum + num, 0)
    return soma / valores
}

let mediaAritmetica = (...numbers) => {
    
}

console.log(media(12, 5, 9, 3, 4, 12, 3, 55))