#!/usr/bin/python3

import json, random, re

with open('../data/02.json', 'r') as file:
    tweets = json.load(file)

with open('../data/05words.json', 'r') as file:
    words = json.load(file)

with open('./01patterns.json', 'r') as file:
    patterns = json.load(file)

import classifier

print(len(tweets))

features = {}
i = 0
for tweet in tweets:
    i += 1
    text = tweet['text']
    f = classifier.extract_features(text, patterns, words)
    if text in features:
        print('WARN text previously added to hash')
    features[text] = f
    if random.random() > 0.9:
        print('{}/{}'.format(i, f))

with open('./02features.json', 'w') as file:
  json.dump(features, file, sort_keys=True)