#!/usr/bin/python3

user_id = '10045092'

r = '/vagrant/data/osn-data/tweets/{}.json'.format(user_id)
w = '/vagrant/data/osn-data/tweets/{}.csv'.format(user_id)

import json
with open(r, 'r') as file:
  tweets_hash = json.load(file)

tweets = []
for key in sorted(tweets_hash.keys()):
  tweets.append(tweets_hash[key])

import csv
with open(w, 'w', newline='', encoding='utf-8') as file:
  csv_writer = csv.writer(file, delimiter=',')
  for tweet in tweets:
    csv_writer.writerow(['','','','','',tweet['text'].replace('\n','')])
