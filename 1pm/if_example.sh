#! /bin/bash

echo "The script is running."

input=$1
echo "The input is $input"

# how to check number of args:
# https://stackoverflow.com/questions/18568706/check-number-of-arguments-passed-to-a-bash-script

if [ $input -gt 0 ]
	then echo "The input of $input is greater than 0"

elif [ $input -lt 0 ] 
	then echo "The input of $input is less than 0."
else
	echo "The input must be 0."
fi


echo "Done."
