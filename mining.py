import tweepy
import csv
import toml
import pandas as pd
import snscrape.modules.twitter as sntwitter

#Env's
with open('config.toml') as config:
  config = toml.loads(config.read())
  APP_NAME = config['APP_NAME']
  API_KEY = config['API_KEY']
  API_KEY_SECRET = config['API_KEY_SECRET']
  ACCESS_TOKEN = config['ACCESS_TOKEN']
  ACCESS_TOKEN_SECRET = config['ACCESS_TOKEN_SECRET']

#Auth Twitter API
auth = tweepy.OAuthHandler(API_KEY, API_KEY_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth,wait_on_rate_limit=True)

#Mining
csvFile = open('base.csv', 'a')
csvWriter = csv.writer(csvFile)
maxTweets = 50
for i,tweet in enumerate(sntwitter.TwitterSearchScraper(' BBB ' + 'lang:pt').get_items()) :
        if i > maxTweets :
            break
        print(tweet.content)
        print(tweet.date)
        csvWriter.writerow([tweet.date, tweet.content.encode('utf-8')]) #If you need more information, just provide the attributes

#Teste