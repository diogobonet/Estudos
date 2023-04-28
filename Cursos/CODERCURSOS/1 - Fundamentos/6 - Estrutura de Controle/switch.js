const imprimirResultado = function (nota) {
    switch(Math.ceil(nota)) {
        case 10:
        case 9:
            console.log("Quadro de Honra!")
            break
        case 8: case 7:
            console.log("Aprovado!")
            break
        case 6: case 5: case 4:
            console.log("Recuperação!")
            break
        case 3: case 2: case 1:
            console.log("Reprovado!")
            break
        default:
            console.log("Nota inválida!")
            break
    }
<<<<<<< HEAD
}
dadadadadadad

console.log("Oiii")
=======
    
}

>>>>>>> f0aca83fdb5241faf61e3cdf387a151e31f623ff
imprimirResultado(9)
imprimirResultado(6.5)
imprimirResultado(3)
imprimirResultado(-1)
console.log("Fim!")
