#!/usr/bin/python

import json

import db

time_id_from = '2016-01-01-00'
time_id_to = '2016-12-31-23'

bag = {}

days = db.history_twitter__read('10449052', time_id_from, time_id_to)

for day in days:
  data = json.loads(day['data'])
  tweet_ids = data['tweets']
  for tweet_id in tweet_ids:
    print(tweet_id)
    tweet = db.tweet__read(tweet_id)
    if tweet is None:
      continue
    text = tweet['text']
    words = text.split(' ')
    for word in words:
      if word not in bag:
        bag[word] = 1
      else:
        bag[word] = bag[word] + 1

with open('/tmp/twitter_bag_of_words.json', 'w') as file:
  json.dump(bag, file, sort_keys=True)
