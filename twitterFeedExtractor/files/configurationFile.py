# This file will contain all database configuration, also the key for Twitter API

class Configurations:
	#db configuration
	userName = 'root'#user name for database
	password = 'rmtdl0680036'
	hostIP ='127.0.0.1'
	databaseName = 'twitterdata'
	raise_on_warnings = True

	dbconfig = {
		'user': userName,
		'password': password,
		'host': hostIP,
		'database': databaseName,
		'raise_on_warnings': True,
	}
	def dbApiConfig(self):
		# return db configuration
		return self.dbconfig


	#twitter api configuration
	consumer_key = "HXXXXXXXXXXXn"
	consumer_secret = "wXXXXXXXXXXXXXXXXXXXXXXk"
	access_token = "2XXXXXXXXXXXXXXXXXXO"
	access_token_secret = "qXXXXXXXXXXXXXXXXXXXXXXXXXl"
	twitter_config = consumer_key,consumer_secret,access_token,access_token_secret

	def twitterApiConfig(self):
		# return twitter api configuration
		return self.twitter_config

if __name__ == "__main__":
	config = Configuration()
	print config.twitterApiConfig()
