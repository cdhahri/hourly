#!/usr/bin/python3

r = '/vagrant/tmp/tweets_larryconlin.json'
w = '/vagrant/src/rf/data_tmp/pearson/source.json'

import json
with open(r, 'r') as file:
  tweets = json.load(file)

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
