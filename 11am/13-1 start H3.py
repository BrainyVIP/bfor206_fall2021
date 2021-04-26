# -*- coding: utf-8 -*-
"""
Created on Mon Apr 26 11:41:55 2021

Start homework 3

- load the IRC logs

- use regular expressions to check the start of each line


@author: lee
"""

#%% imports 

import re


#%% read data file

# create empty list for the logs
raw_log = []

# open the file and then read the lines

with open('data/hackers.txt', 'r+', errors='ignore') as f:
    raw_log = f.readlines()

#%% view the first 100 rows

print(raw_log[0:100])


#%% create a subset of 1000 rows

# comment this out later when doing the final run!
raw_log = raw_log[:1000]


#%% start creating functions to break the code down


def is_comment_row(row):
    """
    check if row begins with ---

    Parameters
    ----------
    row : string
        row from a chat log.

    Returns
    -------
    True/False.

    """
    is_comment = re.match(r'---', row[0:5])
    
    return is_comment


def is_time_row(row):
    """
    check if the row starts with HH:MM format

    Parameters
    ----------
    row : string
        row from a chat log.

    Returns
    -------
    True/False.

    """
    
    is_time = re.search(r'([0-9]{2}):([0-9]{2})', row[0:5])
    
    return is_time
    

#%% find comment rows (rows that start with ---)

time_row_list = []
bad_row_list = []

for row in raw_log:
    # print(row)
    
    """
    The first row is:
    --- Log opened Tue Sep 20 00:01:49 2016
    
    We want to find rows that match this pattern at the beginning
    
    To look at just the beginning of the string, just view
    the first 5 characters (a string is like a list of characters)
    
    """
    # print("the first 5 chars are", row[0:5])
    if is_comment_row(row):
        print("Found comment row", row)
        # pass
    
    # check if the row starts with HH:MM format
    elif is_time_row(row):
        #print("Found row with times ", row)
        time_row_list.append(row)

    # show us any rows that do meet these criteria
    # there are 7-8 rows that do not match
    else:
        print("row has no matches", row)
        bad_row_list.append()
