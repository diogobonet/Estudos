class Property {
    constructor(area, price) {
        this.area = area
        this.price = price
    }

    getPriceSquareMeter() {
        return this.price / this.area
    }

   
}

class House extends Property {
        
}

class Apartment extends Property {
    constructor(number, area, price) {
        super(area, price) // Chama o construtor do Super (está chamando do Property)
        this.number = number
    }

    getFloor() {
        return this.number.slice(0, -2)
    }
}

const land = new Property(200, 5000)
const house = new House(200, 500)
console.log(house.getPriceSquareMeter())

console.log(house instanceof Property)

const ap = new Apartment('201', 100, 160000)
console.log(ap)
console.log(ap.getFloor())
