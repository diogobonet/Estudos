function chunks(num) {
    if (num == 0) {
        return "nada"
    }

    if (num == 1) {
        return "chunk"
    }

    else {
        return "chunk-" + chunks(num-1)
    }
}

console.log(chunks(0))
console.log(chunks(6))