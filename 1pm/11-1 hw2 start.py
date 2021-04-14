# -*- coding: utf-8 -*-
"""
Created on Thu Apr  8 15:36:46 2021

Play with reddit data on AI/ML


Primary data source
https://www.kaggle.com/maksymshkliarevskyi/reddit-data-science-posts

@author: Lee Spitzley
"""

#%% imports
import os
import pandas as pd


#%% read data

input_folder = 'data/reddit_aiml'

# list of files
file_list = os.listdir(input_folder)


# empty list to store dataframes
df_list = []

# read in dataframes
for file in file_list:
    print('loading', file)
    
    # easy/lazy way to add directory to file names
    #temp_df = pd.read_csv(input_folder + file)
    
    # better version
    temp_df = pd.read_csv(os.path.join(input_folder, file))
    
    
    # add the dataframes into a list
    df_list.append(temp_df)

#%% join the dataframes together
# https://stackoverflow.com/questions/32444138/concatenate-a-list-of-pandas-dataframes-together
aiml_data = pd.concat(df_list)

# get a random sample of data to see if things work without
# taking forever!
# overwrite the full dataset, re-run code above g
aiml_data = aiml_data.sample(1000)
# ^^comment that line out if you want the full data frame



#%% explore data

aiml_data.info()
summary = aiml_data.describe(include="all")


#%% date formatting

# https://stackoverflow.com/questions/19231871/convert-unix-time-to-readable-date-in-pandas-dataframe

aiml_data['author_created_date'] = pd.to_datetime(aiml_data['author_created_utc'], unit='s')
aiml_data['author_created_date'].head()
