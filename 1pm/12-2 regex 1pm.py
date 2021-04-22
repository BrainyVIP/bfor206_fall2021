# -*- coding: utf-8 -*-
"""
Created on Wed Apr 21 13:18:30 2021

We will use this script to demonstrate some basic regular
expression usage

@author: lee
"""

#%% import 
import re


#%% build some basic expressions

re.search(r'bfor', 'BFOR206 Programming for Security Analytics')
re.findall(r'BFOR', 'BFOR206 Programming for Security Analytics BFOR')


#%% working with times (useful for HW3)

hh_mm = "It is\t13:45\nok"
print(hh_mm)


re.search('[0-9]{2}:[0-9]{2}', hh_mm)


#%% groups

group_result = re.search(r'([0-9]{2}):([0-9]{2})', hh_mm)

print(group_result)
# print the hour group
print(group_result.group(1))
# print the minute group
print(group_result.group(2))
