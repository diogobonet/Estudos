const Account = require("./Account");

const user = new Account(0)
console.log(user.newDeposit(50))
console.log(user.newDeposit(90))
console.log(user.deposits)
console.log(user.balance)
