#!/usr/bin/python3

r = '/vagrant/tmp/tweets.json'
w = '/vagrant/src/rf/data_tmp/pearson/week.json'

import json
with open(r, 'r') as file:
  tweets = json.load(file)

i = -1
days = {
  'Mon': 1,
  'Tue': 1,
  'Wed': 1,
  'Thu': 1,
  'Fri': 1,
  'Sat': 1,
  'Sun': 1
}

feature = []
for tweet in tweets:
  day = tweet['created_at'][:3]
  feature.append(days[day])

with open(w, 'w') as file:
  json.dump(feature, file)
