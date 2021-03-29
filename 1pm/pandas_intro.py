#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 29 13:18:50 2021

@author: leespitzley
"""

#%% imports 

import numpy as np # this is an alias
import pandas as pd # also an alias
from matplotlib.pyplot import hist

#%% create a random matrix

matrix = np.random.randint(0, 100, size=(100, 4))

print(matrix)

# [rows, columns]
print(matrix[90:100, 0:2])


#%% create a dataframe with pandas

random_df = pd.DataFrame(matrix, columns=list('ABCD'))
random_df['A']

random_df['B'].plot.hist()


#%% add a new colun of random numbers

new_col = np.random.normal(loc=5, scale=2, size=100)

# add this column to our dataframe
random_df['E'] = new_col

# this plot will look like a normal curve (bell curve)
random_df['E'].plot.hist()

#%% add text column

labels = np.random.choice(['A_1', 'A_2', 'B_1', 'B_2'], size=100)
# add this column to our dataframe
random_df['labels'] = labels

# view the column names programatically
list(random_df)


#%% split the label column into two parts
label_group = random_df['labels'].str.split('_')
print(label_group)

# add the 0 column from that operation to our main dataframe
random_df['group'] = label_group.str[0]

# view first five rows
print(random_df.head())

#%% summarize and describe the data

# the include all param also includes text columns
random_df.describe(include='all')

# getting information by group

random_df.groupby('group')[['C', 'D']].mean()

# get means of all columns by group 
df_summary = random_df.groupby('group').mean()

#%% lab start
mtcars = pd.read_csv('data/mtcars.csv')

# check column names
list(mtcars)


# change the name of the first column
mtcars.rename(columns={"Unnamed: 0": "make_model"}, inplace=True)

list(mtcars)




