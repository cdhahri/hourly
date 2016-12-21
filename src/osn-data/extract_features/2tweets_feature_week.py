#!/usr/bin/python3

r = '/vagrant/tmp/tweets.json'
w = '/vagrant/src/rf/data_tmp/pearson/week.json'

import json
with open(r, 'r') as file:
  tweets_hash = json.load(file)

tweets = []
for key in sorted(tweets_hash.keys()):
  tweets.append(tweets_hash[key])

i = -1
days = {
  'Mon': 1,
  'Tue': 1,
  'Wed': 1,
  'Thu': 1,
  'Fri': 1,
  'Sat': 2,
  'Sun': 2
}

feature = []
for tweet in tweets:
  day = tweet['created_at'][:3]
  feature.append(days[day])

with open(w, 'w') as file:
  json.dump(feature, file)
