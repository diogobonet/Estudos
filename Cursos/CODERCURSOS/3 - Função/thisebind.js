const pessoa = {
    saudacao: "Boa tarde!",
    falar() {
        console.log(this.saudacao)
    }
}

pessoa.falar()

const falar = pessoa.falar
falar()