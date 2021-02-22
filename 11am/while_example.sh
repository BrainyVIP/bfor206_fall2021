#! /bin/bash

counter=0

LIMIT=10

while [ $counter -lt $LIMIT ]
do
	echo -n "$counter "
	let "counter += 1"
done
echo
