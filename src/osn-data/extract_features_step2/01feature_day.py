#!/usr/bin/python3

days = {
  'Mon': 1,
  'Tue': 2,
  'Wed': 3,
  'Thu': 4,
  'Fri': 5,
  'Sat': 6,
  'Sun': 7,
  'NOVAL': -1,
}

import json

with open('/vagrant/data/osn-data/ids.json', 'r') as file:
  ids = json.load(file)

for user_id in ids:
  r = '/vagrant/data/osn-data/tweets/{}.json'.format(user_id)
  w = '/vagrant/data/osn-data/features_step2/{}day.json'.format(user_id)

  with open(r, 'r') as file:
    tweets_hash = json.load(file)

  tweets = []
  for key in sorted(tweets_hash.keys()):
    tweets.append(tweets_hash[key])

  feature = []
  for tweet in tweets:
    day = 'NOVAL'
    if tweet is not None and 'created_at' in tweet:
      day = tweet['created_at'][:3]
    feature.append(days[day])

  with open(w, 'w') as file:
    json.dump(feature, file)
