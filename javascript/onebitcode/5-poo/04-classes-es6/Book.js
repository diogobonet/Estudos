class Book {
    constructor(title, price, author) { // Construtor
        this.title = title // Atributo  
        this.price = price
        this.author = author
        this.published = false
    }

    publishingBook = () => this.published = true
}

const eragon = new Book("Eragon", 17.8, "Diogo Bonet") // Instancia

console.log(eragon)
eragon.publishingBook()
console.log(eragon)

if (eragon instanceof Book) {
    console.log(true)
}

console.log(eragon instanceof Book)