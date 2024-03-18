pi = 3.14
function menu() {
    let opt = ""
    
    do {
        opt = parseInt(prompt("Escolha uma opção: \n1) Área do Triangulo \n2) Área do Retangulo \n3) Área do Quadrado \n4) Área do Trapézio \n5) Área do Circulo \n6) Sair"))

        switch (opt) {
            case 1:
                areaTriangulo()
                break
            case 2:
                areaRetangulo()
                break
            case 3:
                areaQuadrado()
                break
            case 4:
                areaTrapezio()
                break
            case 5:
                let raio = prompt("Digite o raio do circulo: ")
                alert(areaCirculo(raio))
                break
            case 6:
                alert("Saindo...")
                break
            default:
                alert("Algo deu errado! Tente novamente!")
        }
    } while(opt != 6)
}

function areaTriangulo() {
    let base = parseFloat(prompt("Digite a base do Triangulo"))
    let altura = parseFloat(prompt("Digite a altura do Triangulo"))
    alert("A área do triangulo é: " + (base + altura) / 2)
}

function areaRetangulo() {
    let base = parseFloat(prompt("Digite a base do retangulo"))
    let altura = parseFloat(prompt("Digite a altura do retangulo"))
    alert("A área do triangulo é: " + (base * altura))
}

function areaQuadrado() {
    let lado = parseFloat(prompt("Digite o lado do quadrado"))
    return lado * 2
}

function areaTrapezio() {
    let baseMaior = parseFloat(prompt("Digite a base maior"))
    let baseMenor = parseFloat(prompt("Digite a base menor"))
    let altura = parseFloat(prompt("Digite a altura"))
    alert("A área do trapézio é: " + (baseMaior + baseMenor) * altura / 2) 
}

function areaCirculo(raio) {
    return  pi * (raio * 2)
}

menu()