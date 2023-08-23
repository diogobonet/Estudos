document.getElementById('sessionBtn').addEventListener('click', function () {
    const input = document.getElementById('session')
    sessionStorage.setItem('info', input.value)
    input.value = ''
})

document.getElementById('readSession').addEventListener('click', function () {
    const info = sessionStorage.getItem('info')
    alert(info)
})

document.getElementById('localBtn').addEventListener('click', function () {
    const input = document.getElementById('local')
    localStorage.setItem('text', input.value)
    input.value = ''
})

document.getElementById('readLocal').addEventListener('click', function () {
    const info = localStorage.getItem('text')
    alert("LocalStorage mensagem: " + info)
})

document.getElementById('cookieBtn').addEventListener('click', function () {
    const input = document.getElementById('cookie')
    // cookieName = value; expires=UTCStringDate; path=/ ;
    const cookie = 'info=' + input.value + ';'
    const expiration = 'expires=' + new Date(2023, 8, 25) + ';'
    const path = 'path=/;' 
    document.cookie = cookie + expiration + path
    input.value = ''
})