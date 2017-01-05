#!/usr/bin/python

from datetime import datetime, timedelta
import json

with open('/vagrant/data/osn-data/ids.json', 'r') as file:
  ids = json.load(file)

for id_user in ids:
  with open('./data/{}next_days.json'.format(id_user), 'r') as file:
    next_days = json.load(file)

  with open('/vagrant/data/osn-data/tweets_selected/{}.json'.format(id_user), 'r') as file:
    tweets = json.load(file)

  tweets_next_days = {}

  for key, tweet in tweets.items():
    if tweet is None:
      continue
    if 'created_at' not in tweet:
      continue
    current_day = tweet['created_at']
    current_day_object = datetime.strptime(current_day, '%a %b %d %H:%M:%S %z %Y')
    if '{0:%Y-%b-%d}'.format(current_day_object) in next_days:
      tweets_next_days[key] = tweet

  with open('/vagrant/data/osn-data/tweets_next/{}.json'.format(id_user), 'w') as file:
    json.dump(tweets_next_days, file, sort_keys=True)

