#!/usr/bin/python3

r = '/vagrant/tmp/tweets.json'
w = '/vagrant/src/rf/data_tmp/pearson/hashtags_exist.json'

import json
with open(r, 'r') as file:
  tweets = json.load(file)

hashtags = []
for tweet in tweets:
  print(1)
  if len(tweet['entities']['hashtags']) > 0:
    hashtags.append(0)
  else:
    hashtags.append(1)

with open(w, 'w') as file:
  json.dump(hashtags, file)
