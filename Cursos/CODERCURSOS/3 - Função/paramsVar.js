function soma() {
    var nums = 0
    for (i in arguments) {
        nums += arguments[i]
    }
}


console.log(soma(2, 3))