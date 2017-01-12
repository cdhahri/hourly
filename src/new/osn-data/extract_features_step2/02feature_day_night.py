#!/usr/bin/python3

percentages = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

import json

with open('../ids.json', 'r') as file:
  ids = json.load(file)

for user_id in ids:
  print(user_id)
  for percentage in percentages:
    print(percentage / 10)

    r = '../tweets_selected/{}/{}.json'.format(percentage, user_id)
    w = '../tweets_selected/features_step2/{}/{}day_night.json'.format(percentage, user_id)

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
