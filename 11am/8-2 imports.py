# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

#%% imports

import time


#%% print time

print(time.asctime())


#%% os

import os
os.getcwd()

# list current directory
os.listdir()

# list a specific directory
os.listdir('11am/')

os.listdir('..')

# store output into a directory


#%% list python files only
file_list = os.listdir('11am/')

for file in file_list:
    if file.endswith('.py'):
        print(file)


#%% requests

import requests
r = requests.get('https://www.albany.edu/business/faculty/lee-spitzley')

print(r)
print(r.text)

#%% 
import subprocess

subprocess.call(['bash', '11am/bash/echo_lab.sh'])
