#!/usr/bin/python3

percentages = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
percentages = [10]

import json

with open('../ids.json', 'r') as file:
  ids = json.load(file)

for user_id in ids:
  for percentage in percentages:
    r = '../tweets_selected/{}/{}.json'.format(percentage, user_id)
    w = '../tweets_selected/features_step2/{}/{}mentions_count.json'.format(percentage, user_id)

    with open(r, 'r') as file:
      tweets_hash = json.load(file)

    tweets = []
    for key in sorted(tweets_hash.keys()):
      tweets.append(tweets_hash[key])

    feature = []
    for tweet in tweets:
      count = len(tweet['entities']['user_mentions'])
      feature.append(count)

    with open(w, 'w') as file:
      json.dump(feature, file)
