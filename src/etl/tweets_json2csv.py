#!/usr/bin/python3

r = '/vagrant/tmp/tweets.json'
w = '/vagrant/tmp/tweets.csv'

import json
with open(r, 'r') as file:
  tweets = json.load(file)

import csv
with open(w, 'w', newline='', encoding='utf-8') as file:
  csv_writer = csv.writer(file, delimiter=',')
  for tweet in tweets:
    target = ''
    if 'X_tag' in tweet:
      taget = '0' # default to 'negative'
      if tweet['X_tag'] == 'positive':
        target = '4'
    csv_writer.writerow([target,'','','','',tweet['text'].replace('\n','')])
