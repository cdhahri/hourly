#!/usr/bin/python3

r = '/vagrant/tmp/tweets.json'
w = '/vagrant/src/rf/data_tmp/pearson/media_exist.json'

import json
with open(r, 'r') as file:
  tweets_hash = json.load(file)

tweets = []
for key in sorted(tweets_hash.keys()):
  tweets.append(tweets_hash[key])

media = []
for tweet in tweets:
  if 'media' in tweet['entities'] and len(tweet['entities']['media']) > 0:
    media.append(True)
  else:
    media.append(False)

with open(w, 'w') as file:
  json.dump(media, file)
