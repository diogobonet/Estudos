<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>IRPF - Aula Maicris</title>
    <style>
        body {
            font-family: Arial, Helvetica, sans-serif;
            text-align: center;
        }
        div {
            border: 1px solid black;
        }
    </style>
</head>
<body>
<h2>Imposto de Renda</h2>
<p>Para o calcular o imposto de renda, alterar o valor do sálario e o número de dependentes no arquivo principal.php</p>
<div>
    <?php
        include ("IRPF.php");
        # Salário
            $salario = 1400;
        # Número de dependentes
            $n_dependentes = 4;
        # Pessoa
            $pessoa = new IRPF($salario, $n_dependentes);
            $pessoa->setAlimony(0);
            $pessoa->addDeductions(0);
    
            printf("Salário: R$%.2f", $salario);
            echo "<br>";
            printf("Imposto: R$%.2f", $pessoa->getIRPF());
            echo "<br>";
            printf("Taxa enquadrada: %.2f%%", $pessoa->getTax());
            echo "<br>";
            printf("Taxa efetiva: %.2f%%", $pessoa->getRealTax());
            echo "<br><br>";
    ?>
</div>
</body>
</html>
