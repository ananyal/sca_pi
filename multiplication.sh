#!/bin/bash

read -p "What is the first number?: " number1
read -p "What is the second number?: " number2

let "a=$number1"
let "b=$number2"
let "c=$number1 *  $number2"

echo "The product is" $c
