#! /bin/bash

echo "We are starting the script"

input=$1

echo "The input is $input"

if [ "$input" -gt 0 ]
	then echo "The input is greater than 0"

elif [ "$input" -lt 0 ]
	then echo "The input is less than 0"

else 
	echo "No statements were true, therefore the number must be 0"

fi



echo "Done."
