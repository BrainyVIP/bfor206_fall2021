#! /bin/bash

# create the array
test_array=( "one" "two" "three" )

# with bash, array index starts at 0
echo ${test_array[1]}


##################################

echo "enter your name:"
read name_var
echo "You entered $name_var"

# fancy version
read -p "Enter you name: " -a name_var
echo "You entered your first name as ${name_var[0]}"
