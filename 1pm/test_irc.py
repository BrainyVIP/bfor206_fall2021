# -*- coding: utf-8 -*-
"""
Created on Mon May  3 13:12:22 2021


This file will contain our unit tests for the 
IRC homework (HW3)


@author: lee
"""


#%% imports

import pytest


import sys

# this tells us where python is looking for imports
print(sys.path)
# this adds the current directory to the path
# this may not be necessary for some, but
# solves the problem of the current directory 
# not showing when running in the terminal
sys.path.append('.')

# import our main script
# make sure you have an __init__.py file in your current directory
import H3_classwork as irc

#%% test data
# these are test cases to make sure functions work as expected
message_row = '00:25 < ice231> anyone good with exploiting cisco asa with extrabacon?'
message_row2 = '01:17 <+nemecy> hi'
join_row = '00:01 -!- Guest40341 [AndChat2541@AN-pl0gl1.8e2d.64f9.r226rd.IP] has quit [Quit: Bye]'
join_row2 = '00:01 -!- Guest40341 [AndChat2541@AN-pl0gl1.8e2d.64f9.r226rd.IP] has quit [Quit: < ice231>]'



date_row = '--- Log opened Tue Sep 20 00:01:49 2016'


#% check is_message_row
@pytest.mark.parametrize('row, expected', [(message_row, True),
                                           (message_row2, True),
                                           (join_row, False)])

def test_is_message_row(row, expected):
    assert irc.is_message_row(row) == expected

#%% test extract username

@pytest.mark.parametrize('row, expected', [(message_row, 'ice231'),
                                           (message_row2, 'nemecy')])

def test_extract_username(row, expected):
    assert irc.extract_username(row) == expected
    
"""
# also try it with errors if you want it to raise one 
# for example, this function should only receive message rows 
# to process. Otherwise, raise an error
https://docs.pytest.org/en/stable/assert.html#assertions-about-expected-exceptions
"""

@pytest.mark.parametrize('row', [(join_row),
                                 (join_row2)])

def test_extract_username_errors(row):
    """ the second case of this join_row2 actually finds a match
        because of what the user could put in their message
    """
    with pytest.raises(AttributeError):
        irc.extract_username(row)
    
#%% test finding the time from a row


@pytest.mark.parametrize('row, expected', [(message_row, '00:25'),
                                           (message_row2, '01:17'),
                                           (join_row, '00:01')])

def test_get_time(row, expected):
    assert irc.get_time(row) == expected
    
    
#%% test finding the date from a date row
import datetime
@pytest.mark.parametrize('row, expected', [(date_row, datetime.datetime(2016, 9, 20, 0, 0))])

def test_get_date(row, expected):
    assert irc.get_date(row) == expected
    
    
#%% test finding non-English words
# this test is better, because Wednesday is different than wednesday
# word_counts = {'the': 100, 'asdfasdf': 4, 'wednesday': 20, 'aaaaaaaaa': 1}
word_counts = {'the': 100, 'asdfasdf': 4, 'python': 20, 'aaaaaaaaa': 1}
non_english_expected = {'asdfasdf': 4, 'aaaaaaaaa': 1}

@pytest.mark.parametrize('word_counts, expected', [(word_counts, non_english_expected)])

def test_find_non_english_words(word_counts, expected):
    assert irc.find_non_english_words(word_counts) == expected