#!/usr/bin/python

import csv
import json
import api_twitter

with open('/vagrant/tmp/tweets.json', 'r') as file:
  tweets = json.load(file)

targets = []
for tweet in tweets:
  targets.append(int(tweet['X_sentiment']))

with open('/vagrant/src/rf/data_tmp/pearson/target.json', 'w') as file:
  json.dump(targets, file, sort_keys=True)
