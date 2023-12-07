module.exports = class Account {
    #balance
    constructor(balance, deposits, loans, transfers) {
        this.#balance = balance
        this.deposits = deposits
        this.loans = loans
        this.transfers = transfers
    }

    get balance() {
        return this.#balance
    }

    set balance(money) {
        return this.#balance + money
    }

    newDeposit(money) {
        Deposit.
    }
}