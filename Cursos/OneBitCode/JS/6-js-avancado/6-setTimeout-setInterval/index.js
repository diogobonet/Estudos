console.log("Programa iniciado!")

/* TEMPOS DE ESPERA */

const timeoutId = setTimeout(() => { // é uma HighOrder Function | é um timer
    console.log("2 segundos se passaram para iniciar essa mensagem")
}, 2 * 1000) 

// clearTimeout(timeoutId)

let seconds = 0

const intervalID = setInterval(() => { // Cria um intervalo, é bem parecido, ele executa repetidas vezes
    seconds += 3
    console.log(`Se passaram ${seconds} segundos!`)
    if (seconds > 10) {
        clearInterval(intervalID)
        console.log("Intervalo foi limpo!")
    }
}, 2 * 1000)