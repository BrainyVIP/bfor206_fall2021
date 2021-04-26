# -*- coding: utf-8 -*-
"""
Created on Mon Apr 26 13:00:05 2021

@author: lee
"""

#%% imports

import re

#%% define functions

def is_comment_row(row):
    """
    find rows that start with ---
   
    These rows can tell us when the day has changed 

    Parameters
    ----------
    row : str
        Row from our dataset.

    Returns
    -------
    True/False.

    """
    
    is_comment = re.match('---', row[:5])
    
    return is_comment
    
    
    
def is_time_row(row):
    """
    Check if a row starts with HH:MM format

    Parameters
    ----------
    row : str
        Row from our dataset.

    Returns
    -------
    True/False.

    """
    
    is_time = re.search('[0-9]{2}:[0-9]{2}', row[:5])
    
    return is_time

#%% read in data

# create empty list to store data
raw_log = []

with open('data/hackers.txt', 'r+', errors='ignore') as f:
    raw_log = f.readlines()


#%% use a sample of the data

raw_log = raw_log[:1000]

#%% find rows that start with comments

time_rows = []

for row in raw_log:
    # print(row)
    
    if is_comment_row(row):
        # print('found comment row', row)
        pass
        
    # next, check for rows that start with the time in HH:MM format
    
    elif is_time_row(row):
        # print('found time row')
        
        time_rows.append(row)
    
    
    else:
        print("row did not meet any format", row)
    


#%% little testing example

test = is_comment_row('this is not a comment row --- it is something else')
if test: print("true")


test = is_comment_row('--- this is a comment row --- ')
if test: print("true")

