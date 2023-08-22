const input = document.getElementById('input')

document.getElementById('value').addEventListener('click', function () {
    // input.value = input.value === '' ? 'Olá, mundo!' : ''
    input.value = 'Olá, mundo!'
    console.log(input.value)
    console.log(input.getAttribute('value')) // GetAtribute pega o valor pré-definido
})

document.getElementById('type').addEventListener('click', function () {
    // input.type = input.type !== 'radio' ? 'radio' : 'text'
    input.setAttribute('type', 'radio')
})

document.getElementById('placeholder').addEventListener('click', function () {
    input.setAttribute('placeholder', "Digite algo")
})

document.getElementById('disable').addEventListener('click', function () {
    input.setAttribute('disabled', !input.disable)
})

document.getElementById('data').addEventListener('click', function () {
    const data = input.dataset
    console.log('Dataset é um objeto! ', data)
    input.dataset = 'Isso é um objeto'
    console.log('Dataset é um objeto! ', data)
})