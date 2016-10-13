# Queries for data insertion in classifiedTweet, processedTweet, tweets
# heavy traffic at newyork street

# Query for inserting data to the tweets table
from mysql.connector import connect, Error
from configurationFile import Configurations
from twitter_feed import twitterData,tweetData
# Database Configuration
config = Configurations()
#Twitter Config

def saveTweetsQery():
    insert_tweets = ("INSERT INTO tweets "
                   "(tweet_id, tweet_text,user_id,tweet_date,language,location,screen_name,\
                   followers_count,friends_count,time_zone) "
                   "VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)")

    return insert_tweets
    
def mostRecentTweetIdQuery():
    find_max_tweet_id = ("Select max(tweet_id) from tweets" " WHERE user_id = %s ")
    
    return find_max_tweet_id

def mostRecentTweetId(twitter_id):
    # use to find out the mosr recent tweet id
    since_id = 0 
    try:
        cnx = connect(**config.dbApiConfig())
        cursor = cnx.cursor()
        cursor.execute(mostRecentTweetIdQuery(),(twitter_id[1:],))
        data=cursor.fetchall()
        if(data[0][0]):
            since_id = data[0][0]
        else:
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
    
def saveTweets(twitter_id,numbr_of_tweets):
    since_id = mostRecentTweetId(twitter_id)
    #print "Last Tweet ID is %s",since_id
    consumer_key ,consumer_secret,access_token,access_token_secret= config.twitterApiConfig()
    tweets = twitterData(consumer_key,consumer_secret,access_token,access_token_secret,twitter_id,numbr_of_tweets,since_id)
    if(tweets):
        for tweet in tweets:
            try:
                cnx = connect(**config.dbApiConfig())
                cursor = cnx.cursor()
               #recent_tweet_id = cursor.execute(("Select max(tweet_id) from tweets" " WHERE user_id = %s "),(twitter_id[1:],))
                tweet_data = tweetData(tweet)
                cursor.execute(saveTweetsQery(), tweet_data)
        	   #to make sure data is committed to DB
                cnx.commit()
                print ".",
            except Error as error:
                a = error
            finally:
                cursor.close()
                cnx.close()
        print"Tweets Saved"
    else:
    	print"No relevant tweeter feed"
