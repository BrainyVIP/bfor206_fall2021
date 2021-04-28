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
import pandas as pd


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
    True/False. - It is actually an re.Match object

    """
    
    is_time = re.search(r'([0-9]{2}):([0-9]{2})', row[0:5])
    
    return is_time


def is_message_row(row):
    """
    Check if row is a user message

    Parameters
    ----------
    row : TYPE
        DESCRIPTION.

    Returns
    -------
    True/False.

    """
    
    # we are explicitly returning True/False
    
    is_message = re.search(r'<', row[6:7])
    if is_message:
        return True
    else:
        return False


def convert_time():
    """
    Function to convert time from string to hours and minutes

    """
    pass



def extract_username(row):
    """
    Take a known chat row (assumes we already checked it is a chat row)
    find the username and return just that.

    Parameters
    ----------
    row : TYPE
        DESCRIPTION.

    Returns
    -------
    None.

    """
    # print(row)
    username = re.search(r'<.([\w]+)>', row)
    # print(username)

    return username.group(1)

#%% test the functions

# some sample data to make sure the function works properly
# we can add to this as find new cases
message_row = '01:17 <+nemecy> hi'
message_row2 = '00:25 < ice231> anyone good with exploiting cisco asa with extrabacon?'
login_row = '01:22 -!- lulzdrone [lulz@drone.incoming.pew.pews] has joined #hackers'

is_message_row(message_row) # should find a match
is_message_row(login_row) # should not find a match

test = extract_username(message_row2)


#%% find comment rows (rows that start with ---)

time_row_list = []
bad_row_list = []
message_row_list = []

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
    
    elif is_message_row(row):
        message_row_list.append(row)
    
    # check if the row starts with HH:MM format
    elif is_time_row(row):
        #print("Found row with times ", row)
        time_row_list.append(row)
        

    # show us any rows that do meet these criteria
    # there are 7-8 rows that do not match
    else:
        print("row has no matches", row)
        bad_row_list.append()


#%% we can also do this with pandas apply function

# put the data into a dataframe

hacker_log = pd.DataFrame(raw_log, columns=['raw_log'])
hacker_log['is_message'] = hacker_log['raw_log'].apply(is_message_row)
print(hacker_log)


# subset the data to just those that are messages
# 
chat_rows = hacker_log.loc[hacker_log['is_message'] == True].copy()

#%%% get usesrnames
# apply the extract username function
chat_rows['username'] = chat_rows['raw_log'].apply(extract_username)
