#!/usr/bin/python3

r = '/vagrant/tmp/tweets.json'
w = '/vagrant/src/rf/data_tmp/pearson/favorite_count.json'

import json
with open(r, 'r') as file:
  tweets = json.load(file)

feature = []
for tweet in tweets:
  feature.append(tweet['favorite_count'])

with open(w, 'w') as file:
  json.dump(feature, file)
