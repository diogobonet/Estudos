const p = new Promise((resolve) => {
    console.log("a promise está sendo executada")
    resolve("finished")
})

// pending = pendente
// resolved = resolvida
// rejected = rejeitada

console.log(p)
