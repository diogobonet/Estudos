class Product {
    constructor(name, description, price) {
        this.name = name
        this.description = description
        this.price = price
        this.inStock = 0
    }

    addToStock = (quantity) => this.inStock += quantity

    calculateDiscount = function (percentage) {
        let discount = this.price * percentage
        console.log(`O preço era de R$${this.price}, com o desconto aplicado fica R$${discount} `)
    }
}

const prod1 = new Product("Car", "A toy car", 50)
prod1.addToStock(20)
prod1.calculateDiscount(0.5)
console.log(prod1)
