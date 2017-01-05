#!/usr/bin/python3

import json

with open('../ids.json', 'r') as file:
  ids = json.load(file)

for user_id in ids:
  r = '../tweets_selected/{}.json'.format(user_id)
  w = '../tweets_selected/features_step2/{}active_passive.json'.format(user_id)

  with open(r, 'r') as file:
    tweets_hash = json.load(file)

  tweets = []
  for key in sorted(tweets_hash.keys()):
    tweets.append(tweets_hash[key])

  feature = []
  for tweet in tweets:
    if 'retweeted_status' not in tweet or tweet['retweeted_status'] is None:
      feature.append(1)
    else:
      feature.append(-1)

  with open(w, 'w') as file:
    json.dump(feature, file)
