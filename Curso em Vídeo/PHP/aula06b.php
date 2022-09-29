<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="_css/estilo.css">
    <title>Document</title>
</head>
<body>
    <div>
        <?php
            $atual = $_GET['aa']; # Essa linha vai pegar o dado da URL
            echo("O ano atual é $atual e o ano anterior é ". --$atual);

        ?>
    </div>
</body>
</html>