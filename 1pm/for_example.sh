#!/bin/bash

# basic for loop from 0 to 5

for i in {0..5} 
do
	echo "The value of \$i is $i"
done

echo "#### Example using arrays ####"

name="Lee A Spitzley"

for part in $name
do
	echo $part
done

echo "#### example where increment is 2 ####"

for n in {0..10..2}
do
	let "sum=$sum + $n"
	echo "The sum at $n is $sum"
done


echo "#### example using C-style syntax ####"

N=10
for (( i=0; i<N; i++ ))
do
	echo "The index \$i is $i"
done
