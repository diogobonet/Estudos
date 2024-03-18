var resultado = prompt("Escolha uma alternativa: \n A) \n B) \n C) \n")
switch (resultado) {
    case "a" || "A": 
        alert("O resultado é 'A'")
        break
    case "b" || "B":
        alert("O resultado é 'B'")
        break
    case "c" || "C":
        alert("O resultado é 'C'")
        break
    default:
        alert("default!")
}

/* PODE SER VÁRIOS VALORES E TER OPERAÇÕES DENTRO DO SWITCH! */