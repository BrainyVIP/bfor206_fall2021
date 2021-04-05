#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Basic analysis of COVID-19 data

Setup for Homework 2

@author: leespitzley
"""

import pandas as pd


#%% read in data

county = pd.read_csv('https://raw.githubusercontent.com/nytimes/covid-19-data/master/us-counties.csv')
state = pd.read_csv('https://raw.githubusercontent.com/nytimes/covid-19-data/master/us-states.csv')

# get column information


#%% data cleaning

# convert dates

# get column information

#%% basic data exploration

# see number of rows



#%% summary statistics


#%% aggregate

# get total daily cases in the US

# important note for aggregation: How do you need your data to look?
# check out https://pandas.pydata.org/pandas-docs/stable/user_guide/groupby.html




#%% plot chart

# see https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.plot.html

#linear


# log scale (good for visualizing exponentail growth)


#%% today's lab

# plot in a single chart (with log scale) total cases and total deaths.
