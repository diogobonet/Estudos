const Character = require("./Character");

class Thief extends Character{
    constructor(name, hpPoints, damagePoints, defensePoints) {
        super(name, hpPoints, damagePoints, defensePoints)  
    }

    attack(target) {
        let damage = (this.damagePoints - target.defensePoints) * 2
        console.log(`${this.name} (Thief) given ${damage} damage in ${target.name}`)
        return damage
    }
}

module.exports = Thief

