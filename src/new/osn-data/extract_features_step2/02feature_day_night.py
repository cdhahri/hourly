#!/usr/bin/python3

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
    feature.append(m.group(1))

  with open(w, 'w') as file:
    json.dump(feature, file)
