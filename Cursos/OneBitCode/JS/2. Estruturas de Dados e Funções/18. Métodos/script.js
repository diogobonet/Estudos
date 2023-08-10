// Metodos são funções atrelados a objetos
// Console = Objeto
// Log = Função - logo é um metodo
let pessoa = {
    nome: "Diogo",
    idade: 18,

    dizerOla() {
        console.log("Olá, mundo! Meu nome é " + this.nome) // Referenciando
    }
}


console.log(pessoa)
pessoa.dizerOla()
