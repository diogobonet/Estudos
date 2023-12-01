const Character = require("./Character");

class Mage extends Character {
    constructor(name, hpPoints, damagePoints, defensePoints, magicPoints) {
        super(name, hpPoints, damagePoints, defensePoints)
        this.magicPoints = magicPoints
    }
    
    attack(target) {
        this.damagePoints += this.magicPoints
        let damage = target.hpPoints - (target.defensePoints - this.damagePoints)
        console.log(`${this.name} given ${damage} damage in ${target.name}`)
        return damage
    }

    cure(target) {
        let cure = target.hpPoints += (2 * this.magicPoints)
        console.log(`The ${this.name} (Mage) cured the ${target.name} (+${cure} HP)`)
        return cure
    }
}
 
module.exports = Mage