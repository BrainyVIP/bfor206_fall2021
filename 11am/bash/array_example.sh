#! /bin/bash


test_array=( "A" "B" "C" )

echo ${test_array[0]} # prints out "A"


echo "What is your name?"
read name_var
echo "Your name is ${name_var[0]}"

echo "###############"

read -p "What is your name? " -a name_var
echo "You reported your first name as ${name_var[0]}" 

