const Character = require("./Character");

class Warrior extends Character {
    constructor(name, hpPoints, damagePoints, defensePoints, shieldPoints, position) {
        super(name, hpPoints, damagePoints, defensePoints)
        this.shieldPoints = shieldPoints
        this.position = position
    }

    attack(target) {
        if (this.position == "Attack") {
            super.attack(target)
        } else {
            console.log("You can't attack, because you're setted position is Defense! Use the function switchPosition() to change your position to Attack!")
        }
    }

    switchPosition() {
        if (this.position == "Attack") {
            console.log("Now you're setted to the position Defense!")
            return this.position = "Defense"
        } else if (this.position == "Defense") {
            console.log("Now you're setted to the position Attack!")
            return this.position = "Attack"
        }
    }
}

module.exports = Warrior