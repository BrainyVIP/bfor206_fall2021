# -*- coding: utf-8 -*-
"""
Created on Mon Apr 26 13:00:05 2021

@author: lee
"""

#%% imports

import re
import pandas as pd
from datetime import datetime

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


def get_time(row):
    """
    This function looks at the start of the row
    and finds the time. It returns the time in HH:MM format.

    Parameters
    ----------
    row : str
        DESCRIPTION.

    Returns
    -------
    The time in the format of HH:MM.

    """
    
    
    time = re.search('[0-9]{2}:[0-9]{2}', row)
    
    return time.group(0)


def get_date(row):
    """
    

    Parameters
    ----------
    row : TYPE
        DESCRIPTION.

    Returns
    -------
    The date in 'YYYY-MM-DD' format.

    """
    
    #  remove this line when done
    # row = '--- Log opened Tue Sep 20 00:01:49 2016'
    
    # split on spaces and inspect the parts
    date_parts = row.split()
    
    # join this into a single string
    formatted_date = "-".join([date_parts[7], date_parts[4], date_parts[5]])
    
    # convert from string to datetime format
    dt_date = datetime.strptime(formatted_date, '%Y-%b-%d')
    
    return dt_date
    

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


