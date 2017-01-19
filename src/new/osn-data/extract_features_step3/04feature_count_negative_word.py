#!/usr/bin/python3

import csv, json
        
def process(r, w, words_path):
  with open(words_path, 'r') as file:
    all_words = json.load(file)
  
  with open(r, 'r') as file:
    tweets_hash = json.load(file)

  tweets = []
  for key in sorted(tweets_hash.keys()):
    tweets.append(tweets_hash[key])

  feature = []
  for tweet in tweets:
    words = tweet['text'].split()
    negative = 0
    for word in words:
      if word in all_words:
        score = int(all_words[word][0]) + int(all_words[word][1])
        if score < 0:
          negative += 1
    feature.append(negative)

  with open(w, 'w') as file:
    json.dump(feature, file)

with open('../ids.json', 'r') as file:
  ids = json.load(file)

for user_id in ids:
  r = '../tweets_selected/10/{}.json'.format(user_id)
  w = '../tweets_selected/features_step2/10/{}count_negative_word.json'.format(user_id)
  words_path = '../tweets_raw/words/json/{}.json'.format(user_id)
  process(r, w, words_path)
