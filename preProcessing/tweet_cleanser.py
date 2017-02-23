# -*- coding: utf-8 -*-
"""
Created on Fri Mar 13 07:54:30 2015

@author: Ramanuja
"""

##   Tweet Reprocessing - To remove wide space and repetation,special character

##   This function is used for location extraction purpose, but not for 
##   clasification

import re

def process_tweets(tweet):
    #
    #Convert www.* or https?://* to space
    tweet = re.sub('((www\.[^\s]+)|(https?://[^\s]+))','',tweet)
    #Convert @username to space
    tweet = re.sub('@[^\s]+',' ',tweet)
    #Remove additional white spaces
    tweet = re.sub('[\s]+', ' ', tweet)
    #Replace #word with word
    tweet = re.sub('#([^\s]+)', r'\1', tweet)
    #look for 2 or more repetitions of character and replace with the character itself
    pattern = re.compile(r"(.)\1{1,}", re.DOTALL)
    tweet = pattern.sub(r"\1\1", tweet)
    #Remove ... , -, special character
    tweet = re.sub('[^A-Za-z]+', ' ', tweet)
    #trim
    tweet = tweet.strip('\'"')
    
    return tweet
#end Tweet_cleanser
if __name__ == "__main__":
     data = ["this is for test","John likes to watch movies. Mary likes movies too.","John also likes to watch football games."]
     print ""
