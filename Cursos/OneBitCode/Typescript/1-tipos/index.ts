const spaceship = {
    name: 'X-WING',
    speed: 0
}

function accelerate(spaceship: { name: string; speed: number }, speed: number) {
    spaceship.speed = speed
    console.log(spaceship.name, spaceship.speed)
}

accelerate(spaceship, 50)