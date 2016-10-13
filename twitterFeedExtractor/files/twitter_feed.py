import tweepy
from checkConnection import is_connected
import re

# Below function will hit the twitter api and return all the tweet
def twitterData(consumer_key,consumer_secret,access_token,access_token_secret,twitter_id,numbr_of_tweets,since_id):
	auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
	auth.set_access_token(access_token, access_token_secret)
	api = tweepy.API(auth)
	print "Finding out your internet connection"
	internet_working = is_connected()
	# handel error in case of authentication failure or connection error
	if internet_working:
		print "Internet is fine"
		try:
			print 'Parsing twitter API data... Wait for a while'
			#for reference http://docs.tweepy.org/en/v3.5.0/api.html#API.user_timeline
			all_tweet = api.user_timeline(id= twitter_id ,count = numbr_of_tweets, since_id = since_id)# here tweepy checkt the above user keys
			print "User Authenticated Successfully"
			return all_tweet
		except tweepy.TweepError as error:
		   print error.message
	else:
		print "Check yout internet connection"

def tweetData(tweet):
	#This function is for extracting the tweet data like tweet text, id from a object
	#This will return a tuple a according to the query

	#In future release I will update the database to save  emoji also

	######################## for Emoticon removal from tweet.text##################
	#To remove unicode emoji, so 1366: Incorrect
	# string value: '\xF0\x9F\x9A\x97' for column 'tweet_text' at row 1 error can be avoided

    try:
        # Wide UCS-4 build
        myre = re.compile(u'['
            u'\U0001F300-\U0001F64F'
            u'\U0001F680-\U0001F6FF'
            u'\u2600-\u26FF\u2700-\u27BF]+',
            re.UNICODE)
    except re.error:
        # Narrow UCS-2 build
        myre = re.compile(u'('
            u'\ud83c[\udf00-\udfff]|'
            u'\ud83d[\udc00-\ude4f\ude80-\udeff]|'
            u'[\u2600-\u26FF\u2700-\u27BF])+',
            re.UNICODE)
######################## End of Emoticon removal###############################
    # myre.sub remove emoticon
    # .encode used to convert unicode in to text
    tweet_text = (myre.sub('', tweet.text)).encode('utf-8')
    tweet_id = tweet.id
    tweet_date =  tweet.author.created_at.strftime('%Y-%m-%d %H:%M:%S')
    user_id = tweet.author.screen_name
    screen_name = tweet.author.name
    language = tweet.author.lang
    location = tweet.author.location.encode('utf-8-sig')
    followers_count = tweet.author.followers_count
    friends_count = tweet.author.friends_count
    time_zone = tweet.author.time_zone

    return (tweet_id,tweet_text,user_id,tweet_date,\
                     language,location,screen_name,followers_count,friends_count,time_zone)

if __name__ == "__main__":
	consumer_key = "HXXXXXXXXXXXXXXXXXXXXXn"
	consumer_secret = "wXXXXXXXXXXXXXXXXXXXXXXXXk"
	access_token = "2XXXXXXXXXXXXXXXXXXXXXO"
	access_token_secret = "qXXXXXXXXXXXXXXXXXXXl"
	twitter_id = "@TrafflineDEL"
	numbr_of_tweets = 200
	twitter_data(consumer_key,consumer_secret,access_token,access_token_secret,twitter_id,numbr_of_tweets)
