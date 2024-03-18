const Installment = require("./Installment")

module.exports = class Loan {
    constructor(valueLoan, dateCreation, Installment) {
        this.valueLoan = valueLoan
        this.dateCreation = dateCreation
        this.number = Installment.number
    }

    static #interestRate = 1.5

    static get interestRate() {
        return this.#interestRate
    }

    static set interestRate(interestRateValue) {
        return this.#interestRate = interestRateValue
    }
}