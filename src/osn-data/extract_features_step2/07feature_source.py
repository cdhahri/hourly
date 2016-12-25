#!/usr/bin/python3

import json

with open('/vagrant/data/osn-data/ids.json', 'r') as file:
  ids = json.load(file)

for user_id in ids:
  r = '/vagrant/data/osn-data/tweets/{}.json'.format(user_id)
  w = '/vagrant/data/osn-data/features_step2/{}source.json'.format(user_id)

  with open(r, 'r') as file:
    tweets_hash = json.load(file)

  tweets = []
  for key in sorted(tweets_hash.keys()):
    tweets.append(tweets_hash[key])

  i = 0
  sources = {}
  feature = []
  for tweet in tweets:
    if tweet is None or 'source' not in tweet:
      feature.append(-100)
      continue
    if tweet['source'] not in sources:
      i += 1
      sources[tweet['source']] = i
    feature.append(sources[tweet['source']])

  with open(w, 'w') as file:
    json.dump(feature, file)
