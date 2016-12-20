#!/usr/bin/python

user_id = '10045092'

import json
with open('/vagrant/tmp/osn-data/tweet_ids_before.json', 'r') as file:
  tweets = json.load(file)

tweets = tweets[user_id]

with open('/vagrant/tmp/osn-data/tweet_before_target.json', 'r') as file:
  targets = json.load(file)

mapping = {}
for checkin_tweet_id, tweet_before_ids in tweets.items():
  sentiment = 0
  for tweet_before_id in tweet_before_ids:
    if targets[tweet_before_id]['target'] == '0':
      sentiment -= 1
    elif targets[tweet_before_id]['target'] == '4':
      sentiment += 1
  if sentiment > 0:
    sentiment = 1
  elif sentiment < 0:
    sentiment = -1
  mapping[checkin_tweet_id] = sentiment

with open('/vagrant/tmp/osn-data/checkin_tweet_target.json', 'w') as file:
  json.dump(mapping, file, sort_keys=True)

