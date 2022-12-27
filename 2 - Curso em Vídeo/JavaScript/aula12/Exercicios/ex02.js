function verificar() {
    var data = new Date()
    var ano = data.getFullYear() // Full year pegar o ano com os 4 digitos
    var fAno = document.getElementById('txtano')
    var res = document.querySelector('div#res')
    var fsex = document.getElementsByName("radsex")

    if (fAno.value.length == 0 || Number(fAno.value) > ano) {
        window.alert('[ERRO] Verifique os dados, insira os novamente')
    }

    else { 
        var idade = ano - Number(fAno.value)
        // 
        var genero = ``
        var img = document.createElement("img")
        img.setAttribute("id", "foto")
        if (fsex[0].checked) {
            genero = "Homem"
            
            if (idade >= 0 && )

        } 
        
        
        else {
            genero = "Mulher"
        }
        res.style.textAlign = "center"
        res.innerHTML = `Detectamos ${genero} com ${idade} anos`
}
}