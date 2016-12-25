#!/usr/bin/python3

import json

with open('/vagrant/data/osn-data/ids.json', 'r') as file:
  ids = json.load(file)

ids = [106104712, 109223169, 11437162, 117093537, 11922222, 119436439, 13385712, 14098915, 14216821, 14229632, 14262523, 14701396, 14900774, 14901281, 15370082, 15412985, 15413409, 15479048, 15482020, 15507115, 15526160, 15844952]

for user_id in ids:
  r = '/vagrant/data/osn-data/tweets/{}.json'.format(user_id)
  w = '/vagrant/data/osn-data/tweets/mentions/{}.json'.format(user_id)

  with open(r, 'r') as file:
    tweets_hash = json.load(file)

  tweets = []
  for key in sorted(tweets_hash.keys()):
    tweets.append(tweets_hash[key])

  mentions_hash = {}
  for tweet in tweets:
    if tweet is not None and 'entities' in tweet:
      for mention in tweet['entities']['user_mentions']:
        mentions_hash[mention['id_str']] = None

  mentions = []
  for key in sorted(mentions_hash.keys()):
    mentions.append(key)

  with open(w, 'w') as file:
    json.dump(mentions, file)
