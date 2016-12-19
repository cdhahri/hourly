#!/usr/bin/python

import csv
import json
import api_twitter

import config
token = config.load_token('/vagrant/config/twitter.json')

path = '/vagrant/tmp/sample_user2.tsv'

with open(path, newline='', encoding='utf-8') as file:
  csv_reader = csv.reader(file, delimiter='\t')
  tweets = []
  i = 0
  for row in csv_reader:
    i += 1
    print(i)
    tweet = api_twitter.tweet(token, row[0])
    if tweet is None:
      continue
    tweet['X_sentiment'] = row[6]
    tweets.append(tweet)

with open('/vagrant/tmp/sample_user2.json', 'w') as file:
  json.dump(tweets, file, sort_keys=True)

