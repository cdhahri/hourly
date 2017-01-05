#!/usr/bin/python3

import json
  
def process(r):
  with open(r, 'r') as file:
    tweets = json.load(file)

  zenbu = 0
  geotagged = 0
  for key in sorted(tweets.keys()):
    tweet = tweets[key]
    if tweet is None:
      continue
    if 'coordinates' not in tweet:
      continue
    if tweet['coordinates'] is not None:
      geotagged += 1
    zenbu += 1

  ratio = 0
  try:
    ratio = geotagged/zenbu
  except ZeroDivisionError:
    return

  print(user_id)
  print(len(tweets.keys()))
  print(ratio)
  print('')

with open('/vagrant/data/osn-data/ids.json', 'r') as file:
  ids = json.load(file)

for user_id in ids:
  r = '/vagrant/data/osn-data/tweets_selected/{}.json'.format(user_id)
  process(r)
