<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <form method="get" action="dados.php">
        <!-- <input type="number" name="num" id="num">
        <input type="submit" value="Enviar"> -->

        <?php
        $valor = $_GET["num"];
        $rq = sqrt($valor);
        echo("A raiz quadrada de $valor é $rq")
        ?>
    </form>
</body>
</html>