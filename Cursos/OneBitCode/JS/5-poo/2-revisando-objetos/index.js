const book = {
    title: 'Eragon',
    pages: 468,
    published: true,
    inStock: 20,
    tags: ["Fantasy", "Adventure", "Medieval"],
    author: {
        name: "Diogo Bonet",
        age: 19
    },
    addOnStock(quantity) {
        this.inStock += quantity
    },
    save: function () {
        // salva no banco de dados
        console.log('Olá')
    }
    // Funções contrutoras = fabricas de objetos
}

// PascalCase -> A primeira letra é maiuscula
function Books(title, pages, tags, author) {
    this.title = title
    this.pages = pages
    this.tags = tags
    this.author = author
    this.published = false
    this.inStock = 0
    this.addOnStock = (quantity) => this.inStock += quantity
}

book.addOnStock(60)
book.save()
console.log(book)

const eragon = new Books("Eragon", 60, "Aventura", "Christian Macedo")
eragon.addOnStock(70)
console.log(eragon)

