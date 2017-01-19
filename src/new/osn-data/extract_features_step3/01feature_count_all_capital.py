#!/usr/bin/python3

import csv, json
        
def process(r, w):
  with open(r, 'r') as file:
    tweets_hash = json.load(file)

  tweets = []
  for key in sorted(tweets_hash.keys()):
    tweets.append(tweets_hash[key])

  feature = []
  for tweet in tweets:
    words = tweet['text'].split()
    all_capital = 0
    for word in words:
      if len(word) > 3 and word.isupper():
        all_capital += 1
    feature.append(all_capital)

  with open(w, 'w') as file:
    json.dump(feature, file)

with open('../ids.json', 'r') as file:
  ids = json.load(file)

for user_id in ids:
  r = '../tweets_selected/10/{}.json'.format(user_id)
  w = '../tweets_selected/features_step2/10/{}count_all_capital.json'.format(user_id)
  process(r, w)
