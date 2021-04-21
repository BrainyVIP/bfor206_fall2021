# -*- coding: utf-8 -*-
"""
Created on Wed Apr 21 11:48:21 2021


This is a short script to play with regular expressions


@author: lee
"""

#%% import
import re


#%% test some regex

re.search(r'bfor', 'BFOR206 Programming for Security Analytics')
re.search(r'BFOR', 'BFOR206 Programming for Security Analytics BFOR')


#%% finding hours and minutes 

hh_mm = 'It is\t13:45'

print(hh_mm)

result = re.search(r'([0-9]{2}):([0-9]{2})', hh_mm)
print(result)

# with groups
print(result.group(1))
print(result.group(2))


# if we wanted to see if the hours were valid, do something like this:
hours = result.group(1)
if (int(hours) > 23):
    print("not a valid time")
    
    
#%% using or statements in regex

bfor = 'BFOR206 Programming for Security Analytics'
# find either BFOR or 206
re.findall(r'BFOR|206', bfor) # returns all matches
