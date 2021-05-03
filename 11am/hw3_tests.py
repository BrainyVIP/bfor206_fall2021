# -*- coding: utf-8 -*-
"""
Created on Mon May  3 11:50:09 2021


This script will contain unit tests for H3.

@author: lee
"""

#%% imports

import pytest


# may need to add the current directory to your system path
# so that python can find it.
import sys
sys.path.append('.')
print(sys.path)

# import the main script file
# make sure you have an empty file called __init__.py in your directory
import testing_lecture as irc


#%% test data


# some sample data to make sure the function works properly
# we can add to this as find new cases
message_row = '01:17 <+nemecy> hi'
message_row2 = '00:25 < ice231> anyone good with exploiting cisco asa with extrabacon?'
login_row = '01:22 -!- lulzdrone [lulz@drone.incoming.pew.pews] has joined #hackers'

date_row = '--- Log opened Tue Sep 20 00:01:49 2016'


#%% write tests



#%% test is_message_row

# first define the test and the expected result
@pytest.mark.parametrize('row, expected', [(message_row, True),
                                           (message_row2, True),
                                           (login_row, False),
                                           (date_row, False)])


def test_is_message_row(row, expected):
    assert irc.is_message_row(row) == expected

#%% test finding the hours of the day
# first define the test and the expected result
@pytest.mark.parametrize('row, expected', [(message_row, '01:17'),
                                           (message_row2, '00:25'),
                                           (login_row, '01:22'),
                                           (date_row, None)])

def test_get_time(row, expected):
    assert irc.get_time(row) == expected



#%% try to find the date
import datetime

@pytest.mark.parametrize('row, expected', [(date_row, datetime.datetime(2016, 9, 20, 0, 0))])

def test_get_date(row, expected):
    assert irc.get_date(row) == expected