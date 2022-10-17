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
    $nome = $_POST['nome'];
    $ano = $_POST['ano'];
    $sexo = $_POST['sexo'];

    $idade = 2022 - $ano;
    
    echo("Seu nome é $nome <br>");
    echo("$nome, você nasceu no ano de $ano e possui $idade anos de vida!<br>");
    echo("E você pertence ao sexo $sexo!")
    ?>
</body>
</html>
