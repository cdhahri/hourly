#!/usr/bin/python

import config
token = config.load_token('/vagrant/config/twitter.json')

r = '/vagrant/tmp/larryconlin'
import json
with open(r, 'r') as file:
  tweet_ids = json.load(file)

tweets = []
import api_twitter, db
for tweet_id in tweet_ids:
  tweet = db.tweet__read(tweet_id)
  if tweet is None:
    tweet = api_twitter.tweet(token, tweet_id)
    if tweet is None:
      continue
    db.tweet__create(tweet)
  tweets.append(tweet)

w = '/vagrant/tmp/tweets.json'
with open(w, 'w') as file:
  json.dump(tweets, file, sort_keys=True)
