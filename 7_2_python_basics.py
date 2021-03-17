# -*- coding: utf-8 -*-
"""
Created on Wed Mar 17 13:19:59 2021

This is a block comment. The comment at the start of the 
script can be used to describe the overall purpose of 
what you are trying.

This script will demonstrate basic python functionality.
We'll cover variables, if statements, and for loops.


@author: lee
"""

# this is a regular comment


"""
### Notes on using Spyder

#%% <----- this is a special type of comment in Spyder.

#%% cell name

To run a single line or selection, F9

To run an entire cell, Ctrl + Enter
"""

#%% define variables
my_str = "This is a string"
my_float = 123.45678
my_int = 123
my_bool = True
# boolean is True/False only!

print(my_str)

#%% if statements

a = 1
b = 1

if a > b:
    print("a is greater than b. Wow!")

elif a < b:
    print("a is less than b. Weak!")

else:
    print('a and b are the same, eh?')


#%% for loops

for i in range(5, 10, 2):
    print("i is ", i)

#%% nested statements

for i in range(5, 10):
	print("the outer num is", i) # separate values by commas in print statement
	# indents are very important
	for j in range(2):
		print("the inner num is", j)
print("Done")
 
#%% lab

# create a list using [] 
# separate items using commas
# lists can have multiple types of values

my_list = ["Hello", "BFOR", 206, None, "Bye!"]

for item in my_list:
    print("the item is ", item)










