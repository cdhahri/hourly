#!/usr/bin/python

import db
tweets = db.tweet_sentiment__read()

import json
with open('tweets.json', 'w') as file:
  json.dump(tweets, file, sort_keys=True)
