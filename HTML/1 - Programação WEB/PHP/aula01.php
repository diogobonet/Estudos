<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Server Novo</title>
    <style>
        body {
            font-family: Verdana;
            background-color: lightgray;
        }
    </style>
</head>

<body>
    <h1>Primeira Aula de PHP!</h1>
    <p>Lorem ipsum dolor sit amet consectetur adipisicing elit. Natus, suscipit fugiat aliquid placeat numquam minima nobis cumque quae non? Quam adipisci saepe similique! Maiores est ut totam ipsum consequuntur fugit.</p>
    <h2>Que pedrada de servidor!</h2>
    <?php
    // BARRA BARRA COMENTARIO EM PHP! TOMA DE COMENTÁRIO!!!
    $diogoOfCities = 10;
    echo "PHP Version: " . PHP_VERSION . "<br>";
    echo "OS System: " . PHP_OS . "<br>";
    echo "Tenho $diogoOfCities casas" . "<br>";
    

    $minhaVariavel = "Olá, mundo!";

    if(isset($minhaVariavel)) {
        echo "A variavel foi inicializada com o valor $minhaVariavel" . "<br>";
    }

    else {
        echo "A variavel não foi inicializada!";
    }
?>
<h1>Tag Script</h1>
</body>
</html>
<?php 
    echo "Diogão tá como? Felizão com o PHP!!!"
?>
<!-- O PHP PODE FICAR FORA E DENTRO DO HTML -->
<!-- O PHP PROCESSA NO SERVIDOR E DEVOLVE O RESULTADO DO SERVIDOR! -->