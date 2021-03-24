#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 24 13:16:06 2021

@author: leespitzley
"""

#%% imports

import time

#%% print the current time

print(time.asctime())


#%% os
import os

print(os.getcwd())


print(os.listdir())

print(os.listdir('1pm'))


#%% lab

file_list = os.listdir('1pm')

# iterate throught the items in file_list

for file in file_list:
    if file.endswith('.py'):
        print(file)
        
        
#%% requests
import requests

r = requests.get('https://www.albany.edu/business/faculty/lee-spitzley')

print(r) # should print 200 

print(r.text)

#%% run a bash script
import subprocess

subprocess.call(['bash', '1pm/bash/echo_lab.sh'])
