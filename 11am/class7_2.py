# -*- coding: utf-8 -*-
"""
Created on Wed Mar 17 11:57:41 2021

This is a block comment.
I can type whatever I want here.

This area is good to describe what the program does 
in general terms.

This script will demonstrate basic variables,
if statements, and for loops with Python.

@author: lee
"""

# this is a normal comment

""" 
The comment below defines a chunk that spyder can 
use to separate parts of code into small blocks.
This make to easy to run just a small part of your code.

The syntax is

#%% 

If you want to name a chunk

#%% chunk name
"""

#%% define vars

# to run a single line, F9
my_str = "this is a string"
print(my_str)

my_num = 123.456789
my_int = 123

print(my_num, my_int)

# to run the entire chunk
# Ctrl + Enter (Cmd + Enter on Mac)

# to run the entire chunk and go to the next chunk
# Shift + Enter


#%% if statements

a = 0
b = 1

print("the value of a is", a)


if a > b:
    # everything indented under the if statement is part of that if statement    
    print("a is greater than b. Wow!")
elif a < b:
    print("a is less than b. Weak!")

else:
    print("a and b are the same, eh?")


print("Done with if statements.")


#%% for loops

for i in range(10):
    print("the number i is ", i)


#%% nested statements

for i in range(5, 10):
    print("i is ", i)
    # indents are very important!
    for j in range(3):
        print("j is ", j)
    
print("done with the nested loops")


#%% lab
"""
Fix this code below to complete the lab
"""


my_list = ['Hello', 'BFOR', 206, None, 'Bye!']

for item in my_list:
    print(item)

    if item is None:
        print("Item is none!")
        continue # may be useful depending on how you structure it







