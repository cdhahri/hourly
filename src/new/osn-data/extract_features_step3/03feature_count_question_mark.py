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
    feature.append(tweet['text'].count('?'))

  with open(w, 'w') as file:
    json.dump(feature, file)

with open('../ids.json', 'r') as file:
  ids = json.load(file)

for user_id in ids:
  r = '../tweets_selected/10/{}.json'.format(user_id)
  w = '../tweets_selected/features_step2/10/{}count_question_mark.json'.format(user_id)
  process(r, w)
