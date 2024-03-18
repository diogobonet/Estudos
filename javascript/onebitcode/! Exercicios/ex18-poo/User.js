class User {
    constructor(fullname, email, password) {
        this.fullname = fullname
        this.email = email
        this.password = password
    }
    
    login(email, password) {
        if (email == this.email && password == this.password) {
            console.log(`Login realizado com sucesso ${this.fullname}`)
        } else {
            console.log("Erro no login!")
        }
    }
}

const user1 = new User("Diogo Bonet Sobezak", "diogosobezak@gmail.com", 123456)
user1.login("diogosobezak@gmail.com", 123456)
user1.login("diogosobezak@gmail.com", 12345)