class Character {
    constructor(name, hpPoints, damagePoints, defensePoints) {
        this.name = name
        this.hpPoints = hpPoints
        this.damagePoints = damagePoints
        this.defensePoints = defensePoints
    }

    attack(target) {
        let damage = target.hpPoints - (target.defensePoints - this.damagePoints)
        console.log(`${this.name} given ${damage} damage in ${target.name}`)
    }
}

module.exports = Character