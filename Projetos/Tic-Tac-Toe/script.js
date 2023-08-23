document.getElementById('play').addEventListener('click', function (ev) {
    ev.preventDefault()
    var nome1 = document.getElementById('nome1').value
    var nome2 = document.getElementById('nome2').value
    console.log(nome1, nome2)
})
