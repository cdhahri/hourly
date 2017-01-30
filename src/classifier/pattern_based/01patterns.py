#!/usr/bin/python3

import json, re

with open('../data/02.json', 'r') as file:
  tweets = json.load(file)

with open('../data/05words.json', 'r') as file:
  words = json.load(file)

import classifier
patterns = classifier.extract_patterns(tweets, words)

with open('./01patterns.json', 'w') as file:
  json.dump(patterns, file, sort_keys=True)