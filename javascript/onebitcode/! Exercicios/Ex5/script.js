let medida = parseFloat(prompt("Adicione o valor em (METROS)"))
let opt = prompt("Escolha a unidade de medida a ser convertida: \n Milimetro (mm) \n Centrimetro (cm) \n Decímetro (dm) \n Decâmetro (dam) \n Hectômetro (hm) \n Quilômetro (km)")

let calculo = 0

switch (opt) {
    case "mm" || "MM":
        calculo = medida * 1000
        alert("Resultado: " + calculo + "mm")
        break
    case "cm" || "CM":
        calculo = medida * 100
        alert("Resultado: " + calculo + "cm")
        break
    case "dm" || "DM":
        calculo = medida * 10
        alert("Resultado: " + calculo + "dm")
        break
    case "dam" || "DAM":
        calculo = medida / 10
        alert("Resultado: " + calculo + "dam")
        break
    case "hm" || "HM":
        calculo = medida / 100
        alert("Resultado: " + calculo + "hm")
        break
    case "km" || "KM":
        calculo = medida / 1000
        alert("Resultado: " + calculo + "km")
        break
    default:
        alert("Opção inválida!")
}