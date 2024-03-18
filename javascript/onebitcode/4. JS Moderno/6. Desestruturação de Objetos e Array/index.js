const person = {
    name: "Diogo",
    job: "Estagiário",
    parents: ['Sandro', 'Marielle']
}
console.log(person)

const name = person.name // Normal

const {job, parents} = person

console.log(`Job: ${job}`)
console.log(`Parents: ${parents}`)

const [father, mother] = parents
console.log(`Father: ${father}`)
console.log(`Mother: ${mother}`)

function createUser({name, job, parents}) {
    const id = Math.floor(Math.random() * 9999)
    return {
        id,
        name: name,
        job: job,
        parents: parents
    }
}

const diogo = createUser(person)
console.log(diogo)