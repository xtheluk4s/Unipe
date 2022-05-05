<?php
    $salario = $_GET['salario'];
    $vendas = $_GET['vendas'];
    $comissao = $vendas * 4/100;
    $salario_final = $salario + $comissao;

    echo "Comissão do funcionário é: R$ ".$comissao."<br/>";
    echo "Salário final do funcionário é: R$ ".$salario_final;

    /*
    Lucas Araujo Costa
    Ciência da Computação P2 Noite
    21/11/2021
    17:08
    Questão 2
    */
?>