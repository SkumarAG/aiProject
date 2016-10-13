# Main program to run different part of algorithm

#Importing text vector form 
from bagofwords.textToVector import bagofWords

from preProcessing.tweet_cleanser import process_tweets

test_sentence = ["John likes to watch movies. Mary likes movies too.","John also likes to watch football games."]
filter_data = []
for text in test_sentence:
    filter_data.append(process_tweets(text))

vector = bagofWords(filter_data,1)
