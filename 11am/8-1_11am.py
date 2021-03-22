# -*- coding: utf-8 -*-
"""
Created on Mon Mar 22 11:44:42 2021

This code will demonstrate the use of functions/methods.

@author: lee
"""

#%% define empty function (slide 3)

def new_function():
    pass

#%% call the empty function

print(new_function) # shows details about the function
print(new_function()) # shows None


#%% function with an argument

# this function REQUIRES one argument
def func2(arg1):
    print('the argument is', arg1)
    
#%% call func2

func2() # causes a TypeError
func2('this is a friendly argument')


#%% function with default values

def func3(arg1, arg2=True):
    """ takes one or two arguments and prints stuff """
    if arg2:
        print('arg2 is True')
    
    print('arg1 is ', arg1)


#%% call func3 in several ways

func3() # no arguments, gives TypeError, missing arg1
func3(123)
func3(123, False)
func3(arg2=False, arg1=1234) # can change the order if passing with names

#%% define add numbers

def add_numbers(a, b):
    """
    attempts to convert two values to float type.
    If successful, returns the sum of the numbers.
    
    If the numbers cannot be converted, print a message
    and continue running

    Parameters
    ----------
    a : float or int
        first number to sum.
    b : float or int
        second number to sum.

    Returns
    -------
    result : float
        the sum of the two numbers. Returns None if arguments are not numeric.

    """
    # convert to float first!
    try:
        result = float(a) + float(b) # can convert from string to float
        return result
    except ValueError:
        print("please enter two valid numbers")

#%% call the function

c = add_numbers(11, 22)
print(c)

d = add_numbers('11', '22') # works because these can be converted to floats

e = add_numbers('a', 22) # fail because 'a' cannot be converted


#%% 





