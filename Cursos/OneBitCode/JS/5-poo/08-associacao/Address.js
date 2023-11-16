class Address {
    constructor(street, number, neighborhood, city, state) {
        this.street = street
        this.city = city
        this.number = number
        this.neighborhood = neighborhood 
        this.state = state
    }

    fullAddress() {
        return `Rua ${this.street} | Número ${this.number} | Bairro ${this.neighborhood} | Cidade ${this.city} | Estado ${this.state}`
    }
}

module.exports = Address