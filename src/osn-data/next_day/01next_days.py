#!/usr/bin/python

from datetime import datetime, timedelta
import json
import re

with open('/vagrant/data/osn-data/ids.json', 'r') as file:
  ids = json.load(file)

for id_user in ids:
  with open('/vagrant/data/osn-data/tweets_selected/{}.json'.format(id_user), 'r') as file:
    tweets = json.load(file)

  next_days = {}
  for key in sorted(tweets.keys()):
    tweet = tweets[key]
    if tweet is None:
      continue
    if 'created_at' not in tweet:
      continue
    current_day = tweet['created_at']
    # Tue Sep 27 01:58:41 +0000 2016
    current_day_object = datetime.strptime(current_day, '%a %b %d %H:%M:%S %z %Y')
    next_day_object = current_day_object + timedelta(days=1)
    next_day = '{0:%Y-%b-%d}'.format(next_day_object)
    next_days[next_day] = None

  with open('./data/{}next_days.json'.format(id_user), 'w') as file:
    json.dump(next_days, file, sort_keys=True)
