#! /bin/bash

a=0
LIMIT=15

while [ $a -lt $LIMIT ]
do
	if [ $a -eq 3 ] || [ $a -eq 11 ]
	then
		echo 
		echo "\$a is either 3 or 11: $a"
		echo
		break
	fi
	echo -n "$a "
	let "a+=1"  # increment by 1
done


echo
