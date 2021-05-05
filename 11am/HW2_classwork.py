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



#%% 12-1 Text analysis

# this example is from:
# https://stackoverflow.com/questions/46786211/counting-the-frequency-of-words-in-a-pandas-data-frame

# count words
words = aiml_data['post'].str.split(expand=True).stack().value_counts()
print(words[:10])

# fix the lowercase/uppercase issue
# example on a single string
test_string = "HeLlO pEoPlE"
test_string.split()

# add the lowercase conversion
words = aiml_data['post'].str.lower().str.split(expand=True).stack().value_counts()
print(words[:10])


#%% better way
"""
some machines have problems with memory allocation if 
using the above method, this method should solve that.
It is more difficult and not as pretty, but the results
are the same. 

The for loop below does not sort the output.
"""
# https://stackoverflow.com/questions/18936957/count-distinct-words-from-a-pandas-data-frame


from collections import Counter
results = Counter()

# convert all data to str
aiml_data['post'] = aiml_data['post'].apply(str)
aiml_data['post'].str.lower().str.split().apply(results.update)
print(results)
i = 0 
for key, value in results.items():
    print(key, value, sep='\t')
    i += 1
    if i > 10:
        break

#%% start nltk and download

import nltk
# install sentiment analysis tool if not already installed:
# only need to run this once
# nltk.download('vader_lexicon')


#%% import the sentiment analyzer

from nltk.sentiment.vader import SentimentIntensityAnalyzer

# create a new sentiment analyzer instance
nltk_sentiment = SentimentIntensityAnalyzer()


#%% get sentiment on post titles

# lambdas are small functions
# we can apply these to each row of the data
full_sent = aiml_data['title'].apply(lambda x: nltk_sentiment.polarity_scores(x))

""" intro to dictionaries"""

new_dict = {'key1': 'value1', 'key2': 2}

# get the value stored for a key
new_dict['key1']
new_dict.keys()
new_dict.values()

aiml_data['title_sentiment'] = full_sent.apply(lambda x: x['compound'])

print(aiml_data[['title', 'title_sentiment']].head(10))


#%% most pos & negative posts

most_positive = aiml_data.loc[aiml_data['title_sentiment'].idxmax()]
most_negative = aiml_data.loc[aiml_data['title_sentiment'].idxmin()]

print("The most positive title is ", most_positive[['title', 'title_sentiment']])

print("The most positive title is ", most_negative[['title', 'title_sentiment']])





#%% 12-2 regex

import re

""" 
we want to find URLs from the body of a post

"""

def find_urls(string):
    """ look for urls in a string and return them """
    
    print(string)
    
    """
    # more complicated partial solution:
    if pd.isna(string):
        print('found nan')
    
    """
    
    
    # search the string for URLs
    # force it to a string type with str()
    # URL string is from
    # https://stackoverflow.com/questions/6883049/
    urls = re.findall(r'https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+', str(string))
    
    
    """
    NOTE:
        There is a better URL regex from http://urlregex.com/
        Thanks to Anthony B.!
        urls = re.findall(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', str(string))
    """
    
    
    # return something to the line that called the function
    return urls


#%% run the function
urls = aiml_data['post'].apply(lambda x: find_urls(x))

#%% convert to a list


url_list = urls.tolist() # not quite!

# convert list of lists to a flat list
# https://stackoverflow.com/questions/952914/how-to-make-a-flat-list-out-of-a-list-of-lists

# exchange `t` in the original to `url_list`

flat_list = [item for sublist in url_list for item in sublist]
