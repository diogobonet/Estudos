class Wallet {
    #amount 
    #username
    constructor() {
        this.#amount = 100.99 * 100 // 100099
    }
    get amount() {
        return this.#amount / 100
    }

    set username(newUsername) {
        if (typeof newUsername === 'string') {
            this.#username =  newUsername
        } else {
            console.log("This must be a string!")
        }
        
    }

    get username() {
        return this.#username
    }
}

let mywallet = new Wallet()
console.log(mywallet.amount)
mywallet.username = "Diogo"
console.log(mywallet.username)

