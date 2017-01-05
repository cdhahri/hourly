#!/usr/bin/python3

import json
  
def process(r, w):
  with open(r, 'r') as file:
    tweets_hash = json.load(file)

  tweets = []
  for key in sorted(tweets_hash.keys()):
    tweets.append(tweets_hash[key])

  import csv
  with open(w, 'w', newline='', encoding='utf-8') as file:
    csv_writer = csv.writer(file, delimiter=',')
    for tweet in tweets:
      text = ''
      if tweet is not None and 'text' in tweet:
        text = tweet['text'].replace('\n','')
      else:
        print(tweet)
      csv_writer.writerow(['','','','','',text])

with open('/vagrant/data/osn-data/ids.json', 'r') as file:
  ids = json.load(file)

for user_id in ids:
  #r = '/vagrant/data/osn-data/tweets/{}.json'.format(user_id)
  #r = '/vagrant/data/osn-data/tweets_selected/{}.json'.format(user_id)
  r = '/vagrant/data/osn-data/tweets_next/{}.json'.format(user_id)
  w = '/vagrant/data/osn-data/tweets/csv/{}.csv'.format(user_id)
  process(r, w)
