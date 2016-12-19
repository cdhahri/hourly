#!/usr/bin/python3

r = '/vagrant/tmp/tweets.json'
w = '/vagrant/src/rf/data_tmp/pearson/hashtags_or_mentions_exist.json'

import json
with open(r, 'r') as file:
  tweets = json.load(file)

hashtags = []
for tweet in tweets:
  if len(tweet['entities']['hashtags']) > 0 or len(tweet['entities']['user_mentions']) > 0:
    hashtags.append(True)
  else:
    hashtags.append(False)

with open(w, 'w') as file:
  json.dump(hashtags, file)
