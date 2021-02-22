#! /bin/bash

a=0
LIMIT=15


while [ $a -le $LIMIT ]
do
#	echo "we are at the start of the loop, \$a is $a"
#	let "a += 1"
	if [ $a -eq 3 ] || [ $a -eq 11 ]
	then
		echo
		echo "The value of \$a is either 3 or 11: $a"
		let "a=a+3"
		continue
	fi

	echo -n "$a "
	let "a=a+1"
done

echo 
echo "Done."
