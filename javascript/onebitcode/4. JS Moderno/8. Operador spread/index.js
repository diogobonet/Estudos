const towns = ['Prontera', 'Izlude', 'Payon', 'Alberta', 'Geffen', 'Morroc']
console.log(towns)
console.log(...towns)
console.log(...towns[0])

const townsCopy = towns // Referencia

townsCopy.pop()
townsCopy.pop()
townsCopy.push("Diogo")
console.log(townsCopy)

const townsClone = [...towns] // Clonar
townsClone.push("Curitiba")
console.log(townsClone)

const townsObj = { ...towns }
console.log(townsObj)
