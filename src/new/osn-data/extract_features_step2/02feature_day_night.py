#!/usr/bin/python3

days = {
  'Mon': 1,
  'Tue': 1,
  'Wed': 1,
  'Thu': 1,
  'Fri': 1,
  'Sat': 2,
  'Sun': 2,
  'NOVAL': -1
}

import json

with open('../ids.json', 'r') as file:
  ids = json.load(file)

for user_id in ids:
  r = '../tweets_selected/{}.json'.format(user_id)
  w = '../tweets_selected/features_step2/{}day_night.json'.format(user_id)

  with open(r, 'r') as file:
    tweets_hash = json.load(file)

  tweets = []
  for key in sorted(tweets_hash.keys()):
    tweets.append(tweets_hash[key])

  feature = []
  for tweet in tweets:
    # Fri Feb 28 18:30:34 +0000 2014
    import re
    m = re.search('^.*(\d\d):\d\d:\d\d.*$', tweet['created_at'])
    day = m.group(1)
    feature.append(day)

  with open(w, 'w') as file:
    json.dump(feature, file)
