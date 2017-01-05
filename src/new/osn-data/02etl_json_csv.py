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
      text = tweet['text'].replace('\n','')
      csv_writer.writerow(['','','','','',text])

with open('./ids.json', 'r') as file:
  ids = json.load(file)

for user_id in ids:
  r = './tweets_raw/{}.json'.format(user_id)
  w = './tweets_raw/csv/{}.csv'.format(user_id)
  process(r, w)
