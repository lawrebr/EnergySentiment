import tweepy

consumer_key = "XXX"
consumer_secret = "XXX"

access_token = "XXX"
access_token_secret = "XXX"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

public_tweets = api.home_timeline()
for tweet in public_tweets:
    print tweet.text
