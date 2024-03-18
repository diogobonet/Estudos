const Deposit = require("./Deposit");
const Loan = require("./Loan");
const date = new Date()
const formattedDate = date.toLocaleDateString("pt-BR");

module.exports = class Account {
    #balance
    deposits = []
    loans = []
    transfers = []
    constructor(balance) {
        this.#balance = balance
    }

    get balance() {
        return this.#balance + ` balance`
    }

    set balance(money) {
        return this.#balance + money
    }

    newDeposit(value) {
        this.#balance += value
        const deposit = new Deposit(value, formattedDate)
        this.deposits.unshift(deposit)
        return this.deposits[0]
    }

    newLoan(value) {
        this.#balance += value
        const loan = new Loan(value, formattedDate, "Aprovado")
    }
}