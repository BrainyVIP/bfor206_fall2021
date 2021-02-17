#! /bin/bash

# this code runs a loop a predetermined number of times

for i in {0..5}
do
	echo "The value of \$i is $i"
done

# This code will run the loop over an array
name="Lee A Spitzley"
for part in $name
do
	echo "The part of the name is $part"
done


# use index to get array values
for i in {1..2}
do
	echo ${name[$i]}
done



# jump by two each time through
# update a variable in the loop
#  {start..end..increment_by}

read -p "How long should the loop run? " N

for (( n=0; n <= N; n++ ))
do
	let "sum=$sum+$n"
	echo "The value at $n is $sum"
done


