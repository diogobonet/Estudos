class Account {
    #password
    #balance = 0

    constructor(user) {
        this.email = user.email
        this.#password = user.password
        this.#balance
    }

    getBalance(email, password) {
        if(this.#authenticate(email, password)) {
            return this.#balance
        } else {
            return undefined
        }
    }

    #authenticate(email, password) {
        return this.email == email && this.#password == password
    }
}


const user = {
    email: "diogosobezak@gmail.com",
    password: "123456"
}

const myAccount = new Account(user)
console.log(myAccount.getBalance('diogosobezak@gmail.com', "123456"))

console.log(myAccount)