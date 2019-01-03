import tweepy
from tweepy import OAuthHandler
import json

def process_or_store(tweet):
    print(json.dumps(tweet))

consumer_key = 'YoF6fIoKyNK7xVzSdPvHLIDyf'
consumer_secret = '8eT0mwgasUhruN7Rxrb5fTPgAYixT5dxf5HSFJXYAHJVo7lpjQ'
access_token = '27921499-BxFHm42hWK5AEErzjAQCThZS8o2EGp3SlUJVdyJzd'
access_secret = 'iaF11XorVbcv9sxpCP0Y8ay0txKxGJ2YcxtRlQm0Xl4Ex'

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
 
api = tweepy.API(auth)

for status in tweepy.Cursor(api.home_timeline).items(10):
    # Process a single status
    process_or_store(status._json)

for friend in tweepy.Cursor(api.friends).items():
    process_or_store(friend._json)
