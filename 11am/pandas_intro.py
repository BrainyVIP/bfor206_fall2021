#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 29 11:50:23 2021

Basics of pandas.

@author: leespitzley
"""

#%% imports

import numpy as np # this is an alias 
import pandas as pd # another alias
from matplotlib.pyplot import hist

#%% create random matrix

matrix = np.random.randint(0, 100, size=(100, 4)) # 100 rows, 4 columns
print(matrix)

"""
print the matrix, but only certain rows and columns
The syntax is matrix_name[rows, columns]
In this case, print rows 90 to 100 from column 0
"""

print(matrix[90:100, 0:2]) # prints cols 0 & 1

#%% convert matrix to dataframe

random_df = pd.DataFrame(matrix, columns=list('ABCD'))

# view column by name instead by number
print(random_df['B'])

# plot a column in a histogram
random_df['C'].plot.hist()

#%% add a new column

# generate 100 observations from random normal distribution 
# with mean of 5 and SD of 2

new_col = np.random.normal(loc=5, scale=5, size=100)

# add this column to our existing dataframe into a new column E

random_df['E'] = new_col

random_df['E'].plot.hist()

#%% create labels column

labels = np.random.choice(['A_1', 'A_2', 'B_1', 'B_2'], size=100)

# create a new dataframe column called 'labels'
random_df['labels'] = labels 

# show column names
print(list(random_df))


#%% modify the string to get groups

# split the label column using the '_' character
label_group = random_df['labels'].str.split('_')
print(label_group)

# get the first value (aka 0) from the list in each row
# and store it in our random_df

random_df['group'] = label_group.str[0]
random_df.head()


#%% summarize the dataframe with basic stats

# include='all' shows stats for the text columns (otherwise just numbers show)
random_df.describe(include='all')

# get the average value for columns C and D broken out by group 
# general syntax
#        (grouping column)[datacols].function()
random_df.groupby('group')['C', 'D'].mean()


# run it for all columns and store result in a new variable
df_summary = random_df.groupby('group').mean()

# write the data to an external file
random_df.to_csv('data/random_df.csv')

#%% start on the lab

# read in the data using pandas built-in read_csv()
# file location is relative to your current working directory
# os.getcwd()

mtcars = pd.read_csv('data/mtcars.csv')

#  view statistics
mtcars.describe()

# fix the name of the first column
mtcars.rename(columns={"Unnamed: 0": 'make_model'}, inplace=True)











