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




""" ######################################## """
#%% 12-1 Text Processing

# https://stackoverflow.com/questions/46786211/counting-the-frequency-of-words-in-a-pandas-data-frame

words = aiml_data['post'].str.split(expand=True).stack().value_counts()
print(words[:10])

# fix case issues
test_string = "ClAsS tImE"
test_string.lower()

# count after lowercase
words = aiml_data['post'].str.lower().str.split(expand=True).stack().value_counts()
print(words[:10])


"""
on some systems, the method above causes 
errors with memory allocation
"""
#https://stackoverflow.com/questions/18936957/count-distinct-words-from-a-pandas-data-frame

# this method gives an error on empty posts
# convert the column so that everything string

aiml_data['post'] = aiml_data['post'].apply(str)


from collections import Counter
results = Counter()
aiml_data['post'].str.lower().str.split().apply(results.update)
# print(results)
results.most_common(10)


#%% nltk setup

# only need to run this once!
"""
import nltk

nltk.download('vader_lexicon')
# comment this out once you are done. 

"""

#%% load nltk sentiment analyzer

from nltk.sentiment.vader import SentimentIntensityAnalyzer
nltk_sentiment = SentimentIntensityAnalyzer()

#%% get sentiment for each row

# using a lambda (aka temporary function)
full_sent = aiml_data['title'].apply(lambda x: nltk_sentiment.polarity_scores(x))

# or just pass the method you want to use to the apply function
full_sent = aiml_data['title'].apply(nltk_sentiment.polarity_scores)


#%% dictionary example 

new_dict = {'key1': 'value1', 'key2': 2}

new_dict['key1']
new_dict.keys()
new_dict.values()


#%% get the compund score and add that to the main dataframe

aiml_data['title_sentiment'] = full_sent.apply(lambda x: x['compound'])

#%% get most positive/negative

most_positive = aiml_data.loc[aiml_data['title_sentiment'].idxmax()]
print("the most positive title is:", most_positive[['title', 'title_sentiment']])

most_negative = aiml_data.loc[aiml_data['title_sentiment'].idxmin()]
print("the most negative title is:", most_negative[['title', 'title_sentiment']])




#%% 12-2 regular expressions

""" 
we want to find the URLs that are contained in a post body.

"""
import re

#%% define a separate function to check for URLs
def find_urls(string):
    """ check a string for the presence of URLs, if found
    return a list of those URLs
    """
    
    # print out each row, the last row printed before an error
    # is our offending row
    print(string)
    
    
    # https://stackoverflow.com/questions/6883049/regex-to-extract-urls-from-href-attribute-in-html-with-python
    
    
    
    # urls = re.findall('https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+', str(string))
    # try this one from urlregex.com
    urls = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', str(string))
    return urls   
    

#%% run the function
urls = aiml_data['post'].apply(lambda x: find_urls(x))

# we have a pandas Series
# we want to convert this to a list of all of the urls

url_list = urls.tolist()

# https://stackoverflow.com/questions/952914/how-to-make-a-flat-list-out-of-a-list-of-lists

flat_list = [item for sublist in url_list for item in sublist]


