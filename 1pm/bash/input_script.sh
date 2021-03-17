#!/bin/bash

# read input from file
# reads into variable called $input
read input < input.txt

# make sure the file read properly
# by showing the contents of the 
# input variable.

echo "\$input is $input"

printf "\n#############################\n\n" >> output.log

# put the date and time into the log
echo "The script is running at " `date` >> output.log


#### ping google and store the results

ping -c3 $input >> output.log

echo "Done." >> output.log


