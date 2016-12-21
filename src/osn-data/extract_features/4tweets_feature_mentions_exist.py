#!/usr/bin/python3

r = '/vagrant/tmp/tweets.json'
w = '/vagrant/src/rf/data_tmp/pearson/mentions_exist.json'

import json
with open(r, 'r') as file:
  tweets_hash = json.load(file)

tweets = []
for key in sorted(tweets_hash.keys()):
  tweets.append(tweets_hash[key])

hashtags = []
for tweet in tweets:
  if len(tweet['entities']['user_mentions']) > 0:
    hashtags.append(True)
  else:
    hashtags.append(False)

with open(w, 'w') as file:
  json.dump(hashtags, file)
