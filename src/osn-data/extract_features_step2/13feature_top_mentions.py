#!/usr/bin/python3

import json

with open('/vagrant/data/osn-data/ids.json', 'r') as file:
  ids = json.load(file)

for user_id in ids:
  r = '/vagrant/data/osn-data/tweets_selected/{}.json'.format(user_id)
  w = '/vagrant/data/osn-data/features_step2/{}top_mentions.json'.format(user_id)

  with open(r, 'r') as file:
    tweets_hash = json.load(file)

  tweets = []
  for key in sorted(tweets_hash.keys()):
    tweets.append(tweets_hash[key])

  mentions = {}
  for tweet in tweets:
    if tweet is not None and 'entities' in tweet:
      for mention in tweet['entities']['user_mentions']:
        n = 1
        if mention['id_str'] in mentions:
          n = n + mentions[mention['id_str']]
        mentions[mention['id_str']] = n

  with open(w, 'w') as file:
    json.dump(sorted(mentions, key=mentions.get, reverse=True)[:3], file)
