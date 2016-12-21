#!/usr/bin/python

import json
with open('/vagrant/tmp/osn-data/tweets_before.json', 'r') as file:
  tweets = json.load(file)

with open('/vagrant/src/rf/data_tmp/pearson/target.json', 'r') as file:
  targets = json.load(file)

if len(tweets) != len(targets):
  print('Check length')
  import sys
  sys.exit(1)

mapping = {}
for i in range(len(tweets)):
  mapping[tweets[i]['id_str']] = {}
  mapping[tweets[i]['id_str']]['target'] = targets[i]

with open('/vagrant/tmp/osn-data/tweet_before_target.json', 'w') as file:
  json.dump(mapping, file, sort_keys=True)

