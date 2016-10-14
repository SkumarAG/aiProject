# Main program to run different part of algorithm

#Importing textToVector from bagofwords folder
from bagofwords.textToVector import bagofWords

#Importing process_tweets function from preProcessing folder
from preProcessing.tweet_cleanser import process_tweets

from file_read.data_read import dataRead
#read tweet data from csv file.
tweets = dataRead()

#test_sentence = ["John likes to watch movies. Mary likes movies too.","John also likes to watch football games."]
filter_data = []
for tweet in tweets:
    filter_data.append(process_tweets(text))

vector = bagofWords(filter_data,1)
