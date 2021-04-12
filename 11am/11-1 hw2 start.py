# -*- coding: utf-8 -*-
"""
Created on Thu Apr  8 15:36:46 2021

Play with reddit data on ML/AI


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

#%% read in dataframes
for file in file_list:
    print("loading", file)
    # lazy way
    # temp_df = pd.read_csv(input_folder + file)
    
    # fancy way
    temp_df = pd.read_csv(os.path.join(input_folder, file))
    
    # add the dataframe to the list
    df_list.append(temp_df)


#%% join together
# join them together
# https://stackoverflow.com/questions/32444138/concatenate-a-list-of-pandas-dataframes-together

aiml_data = pd.concat(df_list)


# get a random sample of data to see if things work without
# taking forever!

# overwrite the data with a 1000 row subset
# once you are ready for the full data, comment this out. 
aiml_data = aiml_data.sample(1000)


#%% adjust dates
# convert author created date to human readable time
# https://stackoverflow.com/questions/19231871/convert-unix-time-to-readable-date-in-pandas-dataframe
# https://en.wikipedia.org/wiki/Unix_time
aiml_data['author_created_date'] = pd.to_datetime(aiml_data['author_created_utc'], unit='s')
aiml_data['author_created_date'].head()


#%% explore data
aiml_data.info()
summary = aiml_data.describe(include="all")











