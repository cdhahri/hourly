#!/usr/bin/python3

import json, re

with open('../data/02.json', 'r') as file:
  tweets = json.load(file)

with open('../data/05words.json', 'r') as file:
  all_words = json.load(file)

text_list = []
for tweet in tweets:
  text_list.append(tweet['text'])
import classifier
patterns = classifier.patterns(text_list, all_words)

with open('./01patterns.json', 'w') as file:
  json.dump(patterns, file, sort_keys=True)