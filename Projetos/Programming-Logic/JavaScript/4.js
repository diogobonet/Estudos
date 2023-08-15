let distanciaAnosLuz = parseFloat(prompt("Digite os anos luz a ser convertido:"))

let opt = prompt("Selecione uma opção: \n1) Parsec(pc)\n2) Unidade astrônomia(AU)\n3) Quilomêtros (KM)")

switch(opt) {
    case "1":
        let parsec = distanciaAnosLuz * 0.306601
        alert(`Distancia em anos luz: ${distanciaAnosLuz}\nParsec(pc): ${parsec}`)
        break
    case "2":
        let au = distanciaAnosLuz * 63241.1
        alert(`Distancia em anos luz: ${distanciaAnosLuz}\nUnidade astronomica (AU): ${au}`)
        break
    case "3":
        let km = distanciaAnosLuz * (9.5 * Math.pow(10, 12))
        alert(`Distancia em anos luz: ${distanciaAnosLuz}\nQuilometros (KM): ${km}`)
        break
}