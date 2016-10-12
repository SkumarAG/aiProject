from files.db_query import saveTweets
twitter_account = ["@SarahJindra",
"@wazetrafficchi",
"@GetRaasta",
"@dtptraffic",
"@TrafflineDEL",
"@TrafflineCHN",
"@TrafflineIndore",
"@TotalTrafficCHI",
"@TfL",
"@HighwaysSEAST",
"@BillWest5",
"@John_Kass",
"@iKartikRao",
"@shelvieana_prat",
"@prats_09",
"@94_294_tollway",
"@DildineMedia",
"@CrazyRicardo",
"@TotalTrafficNYC",
"@WazeTrafficNYC",
"@Traffic4NY",
"@NYTrafficAlert",
"@NYC_DOT",
"@511NYC",
"@NYPD_Traffic",
"@NYCityAlerts",
"@TotalTrafficNYC",
]
numbr_of_tweets = 2000
for twitter_id in twitter_account:
    print "\n"
    print "Saving Data for",twitter_id
    saveTweets(twitter_id,numbr_of_tweets)