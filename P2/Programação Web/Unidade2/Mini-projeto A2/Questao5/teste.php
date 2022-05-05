<?php
    define("ano_atual", 2021);
    $ano_nascimento = $_REQUEST['ano_nascimento'];
    $idade_atual = ano_atual - $ano_nascimento;
    $dias = $idade_atual * 365;
    $ano_seguinte = $idade_atual + 1;


    echo "A sua idade atual é: ".$idade_atual.".<br/>";
    echo "Você viveu ".$dias." dias. <br/>";
    echo "Você vai ter ".$ano_seguinte." anos em 2022.";

    /*
    Lucas Araujo Costa
    Ciência da Computação P2 Noite
    21/11/2021
    16:54
    Questão 5
    */
?>