#!/usr/bin/python3

r = '/vagrant/tmp/tweets_larryconlin.json'
w = '/vagrant/src/rf/data_tmp/pearson/day.json'

import json
with open(r, 'r') as file:
  tweets = json.load(file)

i = -1
days = {
  'Mon': 1,
  'Tue': 2,
  'Wed': 3,
  'Thu': 4,
  'Fri': 5,
  'Sat': 6,
  'Sun': 7
}

feature = []
for tweet in tweets:
  day = tweet['created_at'][:3]
  feature.append(days[day])

with open(w, 'w') as file:
  json.dump(feature, file)
