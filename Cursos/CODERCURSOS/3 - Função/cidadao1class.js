// Higher order function
// Cidadão de primeria linha = trata função como dado tmb

// Criar de forma literal
function fun1() {
}

// Variavel
const fun2 = function () {
}

// Array
const array = [function (a, b) {return a + b}, fun1, fun2]

// Atributo de um objeto
const obj = {}
obj.falar = function () {return "Opa"}
console.log(obj.falar())

// Passar função em parametro de função
function run(fun) {
    fun()
}

run(function () {console.log("Sim")})
