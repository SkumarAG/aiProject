
#simple DB Connection
from mysql.connector import connect, Error
import re
import tweepy
tweet_id = 0
# DB Configuration
config = {
  'user': 'root',
  'password': 'rmtdl0680036',
  'host': '127.0.0.1',
  'database': 'twitterdata',
  'raise_on_warnings': True,
}

consumer_key = "Hol90i780joDoqDzWS32tR2cn"
consumer_secret = "wIPsoeGyHbqfmHNcCdATs8GOlPOx9HeU5OlekcGm6D2TtHyUPk"
access_token = "249152008-zYoxFHAVeDzlWNasuaqxOXBOZpihHCYxi0frmChO"
access_token_secret = "qBTozbbXA10mdI57sEhOoiYrIE18E2GHg8qCwKnkjNZYl"
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)


add_data_tweets = ("INSERT INTO tweets "
               "(tweet_id, tweet_text,user_id,tweet_date,language,screen_name,\
               followers_count,friends_count,time_zone) "
               "VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)")

try:
	cnx = connect(**config)
	cursor = cnx.cursor()
	tweet_data = (12454,"this is for test",4569,"1970-01-12 00:12:12",\
                 "eng","unknown",12,122,"eu")
	cursor.execute(add_data_tweets, tweet_data)

        #Make sure data is committed to the database
	cnx.commit()
    print(".")
except Error as error:
    print "Error occour"
    print(error)
finally:
	cursor.close()
	cnx.close()
