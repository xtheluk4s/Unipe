<?php
    $bmaior = $_REQUEST['bmaior'];
    $bmenor = $_REQUEST['bmenor'];
    $altura = $_REQUEST['altura'];
    $area = ($bmaior + $bmenor) * $altura / 2;

    echo "A = (B + b) * h / 2 <br/>";
    echo "A = ($bmaior + $bmenor) * $altura / 2 <br/>";
    echo "Área: ".$area.".";

    /*
    Lucas Araujo Costa
    Ciência da Computação P2 Noite
    21/11/2021
    17/10
    Questão 3
    */
?>