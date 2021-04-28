# -*- coding: utf-8 -*-
"""
Created on Mon Apr 26 13:00:05 2021

@author: lee
"""

#%% imports

import re
import pandas as pd

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



def is_message_row(row):
    """
    Check to see if a row is a regular chat message.

    Parameters
    ----------
    row : TYPE
        DESCRIPTION.

    Returns
    -------
    True/False.

    """
    
    is_message = re.search('<', row[6:7])
    if is_message:
        return True
    else:
        return False



def extract_username(row):
    """
    Assume values passed to this function have already
    been checked if it is a chat message.
    
    Extract the name of the user who posted the chat message
    and return that name.

    Parameters
    ----------
    row : TYPE
        DESCRIPTION.

    Returns
    -------
    a username.

    """
    
    #print(row)
    
    username = re.search(r'<.(\w+)>', row)
    
    #print(username, username)
    
    return username.group(1)

#%% testing

# these are test cases to make sure functions work as expected
message_row = '00:25 < ice231> anyone good with exploiting cisco asa with extrabacon?'
message_row2 = '01:17 <+nemecy> hi'
join_row = '00:01 -!- Guest40341 [AndChat2541@AN-pl0gl1.8e2d.64f9.r226rd.IP] has quit [Quit: Bye]'

# this should return True
is_message_row(message_row)

# should return false
is_message_row(join_row)

# check username parsing
test = extract_username(message_row)
# check to see if it returns the correct value
extract_username(message_row2) == 'nemecy'

#%% read in data

# create empty list to store data
raw_log = []

with open('data/hackers.txt', 'r+', errors='ignore') as f:
    raw_log = f.readlines()


#%% use a sample of the data

raw_log = raw_log[:1000]

#%% find rows that start with comments

time_rows = []
message_rows = []

for row in raw_log:
    # print(row)
    
    if is_comment_row(row):
        # print('found comment row', row)
        pass
    
    elif is_message_row(row):
        message_rows.append(row)
        
        # could add an if statement and then call extract_ussernames
        
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



#%% use a dataframe instead of a for loop

# create the dataframe

hacker_log = pd.DataFrame(raw_log, columns=['raw_log'])

hacker_log['is_message'] = hacker_log['raw_log'].apply(is_message_row)
print(hacker_log)


# create a separate dataframe for chat rows
chat_rows = hacker_log.loc[hacker_log['is_message'] == True].copy()

chat_rows['username'] = chat_rows['raw_log'].apply(extract_username)


