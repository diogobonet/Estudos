<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <?php
    $nome = isset($_GET['nome'])?$_GET['nome']:"Nome não informado!";
    $ano = isset($_GET['ano'])?$_GET['ano']:0;
    $sexo = isset($_GET['sexo'])?$_GET['sexo']:["Sem sexo"];

    $idade = 2022 - $ano;
    
    echo("Seu nome é $nome <br>");
    echo("$nome, você nasceu no ano de $ano e possui $idade anos de vida! Seu sexo é $sexo!<br>");
    ?>
</body>
</html>
