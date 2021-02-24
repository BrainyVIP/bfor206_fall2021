#!/bin/bash

# read from a file into variable $input

read input < input.txt

echo "\$input is $input"

# ping google 3 times and save the results to the output file

# this line makes the log look a little cleaner
printf "\n############################\n" >> output.log

echo "Script started at " `date` >> output.log

ping -c3 $input >> output.log

echo "Done." >> output.log
