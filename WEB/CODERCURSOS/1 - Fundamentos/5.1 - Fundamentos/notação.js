function Obj(nome, idade) {
    this.nome = nome
    this.id = idade
    this.exec = function() {
        console.log("Executando...")
    }
}

const obj1 = new Obj("Diogo", ", 18")
console.log(obj1.nome, obj1.id)

obj1.exec()