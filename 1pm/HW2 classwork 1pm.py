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



#%% date formatting

# https://stackoverflow.com/questions/19231871/convert-unix-time-to-readable-date-in-pandas-dataframe

aiml_data['author_created_date'] = pd.to_datetime(aiml_data['author_created_utc'], unit='s')
aiml_data['author_created_date'].head()


aiml_data['created_date'] = pd.to_datetime(aiml_data['created_date'])


#%% subset if needed
# get a random sample of data to see if things work without
# taking forever!
# overwrite the full dataset, re-run code above g
aiml_data = aiml_data.sample(1000)
# ^^comment that line out if you want the full data frame



#%% explore data

aiml_data.info()
summary = aiml_data.describe(include="all")




#%% Q2.3 posts by day of week

# which day of the week was something posted?
# https://stackoverflow.com/questions/30222533/create-a-day-of-week-column-in-a-pandas-dataframe-using-python

aiml_data['dow'] = aiml_data['created_date'].dt.day_name()


"""
We need to sort the days of the week in their natural
instead of alphabetical order.

https://stackoverflow.com/questions/35193808/re-order-pandas-series-on-weekday
"""

aiml_data['dow'] = pd.Categorical(aiml_data['dow'], categories=
    ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday', 'Sunday'],
    ordered=True)

# this prints the plot directly, minimal formatting:
aiml_data.groupby('dow')['created_date'].count().plot(kind='bar')

# to format the plot, store it and add elements.
dow_plot = aiml_data.groupby('dow')['created_date'].count().plot(kind='bar')

dow_plot.set(xlabel="Day Of The Week", ylabel="Total Number of Posts",
             title="AI/ML Posts Per day of the week")

dow_plot.get_figure()

# if you want to save the figure to a file:
dow_plot.get_figure().savefig('lab11-2.jpeg')


#%% Q2.1 daily posts over time

# get justs the date, not the hours:minutes:seconds
# https://stackoverflow.com/questions/16176996/keep-only-date-part-when-using-pandas-to-datetime

aiml_data['created_date'].dt.date

aiml_data.groupby(aiml_data['created_date'].dt.date)['created_date'].count().plot()
