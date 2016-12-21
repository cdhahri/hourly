#!/usr/bin/python3

r = '/vagrant/tmp/tweets.json'
w = '/vagrant/src/rf/data_tmp/pearson/hashtags_exist.json'

import json
with open(r, 'r') as file:
  tweets_hash = json.load(file)

tweets = []
for key in sorted(tweets_hash.keys()):
  tweets.append(tweets_hash[key])

hashtags = []
for tweet in tweets:
  if len(tweet['entities']['hashtags']) > 0:
    hashtags.append(0)
  else:
    hashtags.append(1)

with open(w, 'w') as file:
  json.dump(hashtags, file)
