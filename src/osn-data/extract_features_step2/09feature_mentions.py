#!/usr/bin/python3

import json

with open('/vagrant/data/osn-data/ids.json', 'r') as file:
  ids = json.load(file)

for user_id in ids:
  r = '/vagrant/data/osn-data/tweets_selected/{}.json'.format(user_id)
  w = '/vagrant/data/osn-data/features_step2/{}mentions.json'.format(user_id)

  with open(r, 'r') as file:
    tweets_hash = json.load(file)

  tweets = []
  for key in sorted(tweets_hash.keys()):
    tweets.append(tweets_hash[key])

  feature = []
  for tweet in tweets:
    mentions = []
    if tweet is not None and 'entities' in tweet:
      for mention in tweet['entities']['user_mentions']:
        mentions.append(mention['id_str'])
    feature.append(mentions)

  with open(w, 'w') as file:
    json.dump(feature, file)
