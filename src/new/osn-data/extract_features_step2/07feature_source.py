#!/usr/bin/python3

import json

with open('../ids.json', 'r') as file:
  ids = json.load(file)

for user_id in ids:
  r = '../tweets_selected/{}.json'.format(user_id)
  w = '../tweets_selected/features_step2/{}source.json'.format(user_id)

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
