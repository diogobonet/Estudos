<?php
$a = 3;
$b = &$a;
$b += 5;
echo("$a <br>");
echo("$b");
?>