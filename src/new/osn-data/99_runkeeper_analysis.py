#!/usr/bin/python

import json

with open('./ids2.json', 'r') as file:
  ids = json.load(file)

for user_id in ids:
  with open('./tweets_raw/{}.json'.format(user_id), 'r') as file:
    tweets = json.load(file)

  for tweet in tweets.values():
    if tweet['source'] == '<a href="http://runkeeper.com" rel="nofollow">Runkeeper</a>':
      print(tweet['text'])
