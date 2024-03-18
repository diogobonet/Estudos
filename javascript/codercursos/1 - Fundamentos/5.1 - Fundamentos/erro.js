function tratarErroELancar(erro) {
    // throw new Error('Deu ruim!')
    // throw 10
    throw ("Deu ruim!")
}

function imprimirNome(obj) {
    try{
        console.log(obj.name.toUpperCase() + '!!!')
    }
    catch (e) {
        tratarErroELancar(e)
    }
    finally {
        console.log("Pedrada")
    }
}

const obj = { name: "Diogo" }
imprimirNome(obj)