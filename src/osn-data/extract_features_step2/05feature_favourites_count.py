#!/usr/bin/python3

import json

with open('/vagrant/data/osn-data/ids.json', 'r') as file:
  ids = json.load(file)

for user_id in ids:
  r = '/vagrant/data/osn-data/tweets/{}.json'.format(user_id)
  w = '/vagrant/data/osn-data/features_step2/{}favourites_count.json'.format(user_id)

  with open(r, 'r') as file:
    tweets_hash = json.load(file)

  tweets = []
  for key in sorted(tweets_hash.keys()):
    tweets.append(tweets_hash[key])

  feature = []
  for tweet in tweets:
    count = 0
    if tweet is not None and 'favorite_count' in tweet:
      count = tweet['favorite_count']
    feature.append(count)

  with open(w, 'w') as file:
    json.dump(feature, file)
