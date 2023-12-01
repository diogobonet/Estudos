const Character = require("./Character");
const Mage = require("./Mage");
const Thief = require("./Thief");
const Warrior = require("./Warrior");

let diogo = new Character("Diogo", 70, 10, 20)
let user = new Character("User", 80, 20, 50)
diogo.attack(user)

let mago = new Mage("Magoo", 90, 20, 40, 20) 
mago.attack(diogo)
mago.cure(diogo)

let ladrao = new Thief("Ladrão", 50, 30, 40)
ladrao.attack(diogo)

let cavalheiro = new Warrior("Imagine Dragons", 50, 50, 20, 70, "Attack")
cavalheiro.attack(mago)
cavalheiro.switchPosition()
cavalheiro.attack(mago)