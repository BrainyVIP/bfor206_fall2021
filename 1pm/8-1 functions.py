# -*- coding: utf-8 -*-
"""
Created on Mon Mar 22 13:15:35 2021

This script covers the basics of functions/methods

@author: lee
"""

#%% create empty function

def new_function():
    pass

#%% run the empty function

new_function() # looks like nothing happens



#%% function with an argument

def func2(arg1):
    print('the value of arg1 is', arg1)
    
#%% call func2
    
func2(11)


#%% create func3 with a required arg and a default arg

def func3(arg1, arg2=True):
    if arg2:
        print('arg2 is True')
    
    print('arg1 is ', arg1)
    
#%% run func3

func3(1) # this will work and arg2 is true
func3(2, False)
func3(arg2=False, arg1=5)


#%% create a function to add two numbers

def add_numbers(a, b):
    """
    Takes two numbers and adds thtem together. It also checks to verify
    that both parameters/arguments are numbers (float or int)

    Parameters
    ----------
    a : float or int
        The first number to add.
    b : float or int
        The second number to add.

    Returns
    -------
    result : float
        The second number to add.

    """
    try:
        result = float(a) + float(b)
        return result
    
    except:
        print('You must input two numbers')

#%% call the function
c = add_numbers(11, 22)
print(c)
d = add_numbers('11', '22')

# try it with invalid data
e = add_numbers('a', 'b')

f = add_numbers()








