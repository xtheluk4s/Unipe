<?php
    $nome = $_POST['nome'];
    $nota1 = $_POST['nota1'];
    $nota2 = $_POST['nota2'];

    echo "O aluno " .$nome. " ficou com " . ($nota1 + $nota2) / 2 . " de média.";

    /*
    Lucas Araujo Costa
    Ciência da Computação P2 Noite
    21/11/2021
    17:08
    Questão 1
    */
?>