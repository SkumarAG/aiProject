# Database queries for saving tweets to database, looking for the most recent tweets etc.

from mysql.connector import connect, Error
from configurationFile import Configurations
from twitter_feed import twitterData,tweetData

# Database Configuration
config = Configurations()

# SQL query for inserting data to the tweets table
def saveTweetsQery():
    insert_tweets = ("INSERT INTO tweets "
                   "(tweet_id, tweet_text,user_id,tweet_date,language,location,screen_name,\
                   followers_count,friends_count,time_zone) "
                   "VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)")

    return insert_tweets
# SQL query to find out the most recent tweets corresponding to a specific twitter id   
def mostRecentTweetIdQuery():
    find_max_tweet_id = ("Select max(tweet_id) from tweets" " WHERE user_id = %s ")
    
    return find_max_tweet_id

# Python query to find out the most recent tweets in the database
def mostRecentTweetId(twitter_id):
    # use to find out the mosr recent tweet id
    since_id = 0 
    try:
        # Opening database connection
        cnx = connect(**config.dbApiConfig())
        #cursor is a python object for SQL database
        # For more detail - https://dev.mysql.com/doc/connector-python/en/connector-python-api-mysqlcursor.html
        cursor = cnx.cursor()
        # Executing the query
        cursor.execute(mostRecentTweetIdQuery(),(twitter_id[1:],))
        data=cursor.fetchall()
        '''
        In case tweets is available in the database, assign it to since_id, 
        this id going to pass in the API's to the get the new tweets after that.
        '''
        if(data[0][0]):
            since_id = data[0][0]
        else:
        '''
        If id is not available then initialize it to the initial number.
        '''
            print "No archive tweets available in Database"
            since_id = 700000000000000000 # Initilization number to get started
            #print(since_id) 
    except Error as error:
        print "Error occour"
        print(error)    
    finally:
        cursor.close()
        cnx.close()
    return since_id

# Python query to save the tweets into database    
def saveTweets(twitter_id,numbr_of_tweets):
    
    since_id = mostRecentTweetId(twitter_id)
    consumer_key ,consumer_secret,access_token,access_token_secret= config.twitterApiConfig()
    tweets = twitterData(consumer_key,consumer_secret,access_token,access_token_secret,twitter_id,numbr_of_tweets,since_id)
    # if tweets availabe then only open database connection
    if(tweets):
        for tweet in tweets:
            try:
                # Opening database connection
                cnx = connect(**config.dbApiConfig())
                cursor = cnx.cursor()
               #recent_tweet_id = cursor.execute(("Select max(tweet_id) from tweets" " WHERE user_id = %s "),(twitter_id[1:],))
                tweet_data = tweetData(tweet)
                cursor.execute(saveTweetsQery(), tweet_data)
        	   #To make sure data is committed to DB
                cnx.commit()
            except Error as error:
                a = error
            finally:
                # closing database connection
                cursor.close()
                cnx.close()
        print"Tweets Saved"
    else:
    	print"No relevant tweeter feed"
