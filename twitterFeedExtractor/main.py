# The main function to store tweets into database

# Importing the saveTweets function files sub folder 
from files.db_query import saveTweets
#Twitter Handles used to create the Twitter Database
twitter_account = ["@SarahJindra","@wazetrafficchi","@GetRaasta","@dtptraffic","@TrafflineDEL","@TrafflineCHN","@TrafflineIndore",
"@TotalTrafficCHI","@TfL","@HighwaysSEAST","@BillWest5","@John_Kass","@iKartikRao","@shelvieana_prat","@prats_09","@94_294_tollway",
"@DildineMedia","@CrazyRicardo","@TotalTrafficNYC","@WazeTrafficNYC","@Traffic4NY","@NYTrafficAlert","@NYC_DOT","@511NYC","@NYPD_Traffic",
"@NYCityAlerts","@TotalTrafficNYC",]

#A number of tweets that we got whenever the API was hit.
#Note : 200 is the max limit to for free token
numbr_of_tweets = 200

for twitter_id in twitter_account:
    print "\n"
    print "Saving Data for",twitter_id
    saveTweets(twitter_id,numbr_of_tweets)
