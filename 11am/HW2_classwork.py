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


#%% adjust dates
# convert author created date to human readable time
# https://stackoverflow.com/questions/19231871/convert-unix-time-to-readable-date-in-pandas-dataframe
# https://en.wikipedia.org/wiki/Unix_time
aiml_data['author_created_date'] = pd.to_datetime(aiml_data['author_created_utc'], unit='s')
aiml_data['author_created_date'].head()


aiml_data['created_date'] = pd.to_datetime(aiml_data['created_date'])


#%% create small sample
# get a random sample of data to see if things work without
# taking forever!

# overwrite the data with a 1000 row subset
# once you are ready for the full data, comment this out. 
aiml_data = aiml_data.sample(1000)





#%% explore data
aiml_data.info()
summary = aiml_data.describe(include="all")



#%% work with dates/times

# https://stackoverflow.com/questions/30222533/create-a-day-of-week-column-in-a-pandas-dataframe-using-python

aiml_data['dow'] = aiml_data['created_date'].dt.day_name()

temp = aiml_data.groupby('dow').count()

"""
before we plot this, let us sort the days of the week
Otherwise they will display in alphabetical order

https://stackoverflow.com/questions/35193808/re-order-pandas-series-on-weekday

"""

aiml_data['dow'] = pd.Categorical(aiml_data['dow'], categories=
    ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday', 'Sunday'],
    ordered=True)

# this first plot is ugly and not what we want
# it tries to plot values in a line chart

aiml_data.groupby('dow').count().plot()

# only plot the count for one column

aiml_data.groupby('dow')[['created_date']].count().plot(kind='bar')

# store the plot in a variable and add plot elements
dow_plot = aiml_data.groupby('dow')[['created_date']].count().plot(kind='bar', legend=None)

dow_plot.set(xlabel="Day of Week", ylabel="Number of Posts", title="Posts by day of week")


dow_plot.get_figure() # submit this for today's lab!


#%% hours of the day similar to above


#%% total posts over time

# get for each day
# https://stackoverflow.com/questions/16176996/keep-only-date-part-when-using-pandas-to-datetime
aiml_data.groupby(aiml_data['created_date'].dt.date)['created_date'].count().plot()





