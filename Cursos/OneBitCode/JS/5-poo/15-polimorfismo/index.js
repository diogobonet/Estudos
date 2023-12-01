class Vehicle {
    move() {
        console.log("O veiculo está se movendo")
    }
}

class Car extends Vehicle {
    move() {
        console.log("O carro está se movendo no asfalto.")
    }
}

class Ship extends Vehicle {
    move() {
        console.log("O navio está navegando no mar.")
    }
}

class Aircraft extends Vehicle {
    move(speed) {
        console.log(`A aeronave está voando no céu a ${speed}km/h`)
    }
}

const delorean = new Car()
const blackPearl = new Ship()
const boeing = new Aircraft()

delorean.move()
blackPearl.move()
boeing.move(1200)

function start(vehicle) {
    console.log("Iniciando um veiculo...")
    vehicle.move()
}

start(delorean)

