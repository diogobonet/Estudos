<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="_css/estilo.css"/>
    <title>Document</title>
</head>
<body>
    <div>
        <?php
            $v1 = $_GET['x'];
            $v2 = $_GET['y'];
            echo("<h2>Os valores são de V1 e V2 são: $v1 e $v2</h2>");
            // Valor Absoluto
            echo("O valor absoluto de V2 = $v2 é ". abs($v2));

            // Potenciação
            echo("</br>O valor de $v1<sup>$v2</sup> é " . pow($v1, $v2));

            // Raiz quadrada
            echo("</br>A raiz quadrada de $v1 é " . sqrt($v1));

            //Arredondamento (Valores Reais)
            echo("<br>O valor de $v2 arredondado é " . round($v2)); // ceil floor

            echo("<br>O valor de $v2 a parte inteira é " . intval($v2));

            echo("<br>O valor de $v1 em moéda é R$" . number_format($v1, 2));

        ?>
    </div>
</body>
</html>