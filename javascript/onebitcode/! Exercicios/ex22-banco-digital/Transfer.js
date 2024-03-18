module.exports = class Transfer {
    constructor(userTransfer, userReceiver, value, dateCreation) {
        this.userTransfer = userTransfer
        this.userReceiver = userReceiver
        this.value = value
        this.dateCreation = dateCreation
    }
}