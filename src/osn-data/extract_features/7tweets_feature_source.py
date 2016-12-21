#!/usr/bin/python3

r = '/vagrant/tmp/tweets.json'
w = '/vagrant/src/rf/data_tmp/pearson/source.json'

import json
with open(r, 'r') as file:
  tweets_hash = json.load(file)

tweets = []
for key in sorted(tweets_hash.keys()):
  tweets.append(tweets_hash[key])

i = 0
sources = {}
feature = []
for tweet in tweets:
  if tweet['source'] not in sources:
    i += 1
    sources[tweet['source']] = i
  feature.append(sources[tweet['source']])

with open(w, 'w') as file:
  json.dump(feature, file)
