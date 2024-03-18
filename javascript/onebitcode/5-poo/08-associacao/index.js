const Address = require("./Address");
const Person = require("./Person");

const addr = new Address("7 de Setembro", 12, "Centro", "Curitiba", "Paraná")
const john = new Person("Diogo", addr)

console.log(john.address.fullAddress())