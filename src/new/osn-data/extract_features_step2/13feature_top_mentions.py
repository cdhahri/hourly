#!/usr/bin/python3

percentages = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
percentages = [10]

import json

with open('../ids.json', 'r') as file:
  ids = json.load(file)

for user_id in ids:
  print(user_id)
  for percentage in percentages:
    print(percentage / 10)

    r = '../tweets_selected/{}/{}.json'.format(percentage, user_id)
    w = '../tweets_selected/features_step2/{}/{}top_mentions.json'.format(percentage, user_id)

    with open(r, 'r') as file:
      tweets_hash = json.load(file)

    tweets = []
    for key in sorted(tweets_hash.keys()):
      tweets.append(tweets_hash[key])

    mentions = {}
    for tweet in tweets:
      for mention in tweet['entities']['user_mentions']:
        n = 1
        if mention['id_str'] in mentions:
          n = n + mentions[mention['id_str']]
        mentions[mention['id_str']] = n

    with open(w, 'w') as file:
      json.dump(sorted(mentions, key=mentions.get, reverse=True)[:3], file)
