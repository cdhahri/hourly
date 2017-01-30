#!/usr/bin/python3

import json, re

with open('./data/02.json', 'r') as file:
  tweets = json.load(file)

hashset = {}

for tweet in tweets:
  words = tweet['text'].split()
  for word in words:
    hashset[word] = None

out = '\n'.join(sorted(hashset.keys()))

with open('./data/03.txt', 'w', encoding='latin-1') as file:
  file.write(out)