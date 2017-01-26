#!/usr/bin/python3

import json, re

with open('./data/02.json', 'r') as file:
  tweets = json.load(file)

with open('./data/05words.json', 'r') as file:
  all_words = json.load(file)

features = []
targets = []

# pattern-based features
text_list = []
for tweet in tweets:
  text_list.append(tweet['text'])
import classifier
patterns = classifier.patterns(text_list, all_words)

import sys
sys.exit(1)

for tweet in tweets:
  text = tweet['text']
  words = text.split()

  entry = []

  # total score +
  total_pos = 0
  for word in words:
    if word in all_words:
      total_pos += int(all_words[word][0])
  entry.append(total_pos)

  # total score -
  total_neg = 0
  for word in words:
    if word in all_words:
      total_neg += abs(int(all_words[word][1]))
  entry.append(total_neg)

  # ratio score
  entry.append((total_pos - total_neg)/(total_pos + total_neg))

  # number of highly emotional positive words
  num_pos = 0
  for word in words:
    if word in all_words:
      if int(all_words[word][0]) >= 3:
        num_pos += 1
  entry.append(num_pos)

  # number of highly emotional negtive words
  num_neg = 0
  for word in words:
    if word in all_words:
      if abs(int(all_words[word][1])) >= 3:
        num_neg += 1
  entry.append(num_neg)

  # count all capitals
  all_capital = 0
  for word in words:
    if len(word) > 3 and word.isupper():
      all_capital += 1
  # entry.append(all_capital)

  # exclamation mark
  # entry.append(text.count('!'))

  # question mark
  # entry.append(text.count('?'))

  # -
  negative = 0
  for word in words:
    if word in all_words:
      score = int(all_words[word][0]) + int(all_words[word][1])
      if score < 0:
        negative += 1
  # entry.append(negative)

  # +
  positive = 0
  for word in words:
    if word in all_words:
      score = int(all_words[word][0]) + int(all_words[word][1])
      if score > 0:
        positive += 1
  # entry.append(positive)

  # more than three dots
  m = re.search('^.*(\.){3,}.*$', text)
  # entry.append(bool(m))

  # more than three vowels
  m = re.search('^.*(a{3,}|i{3,}|u{3,}|e{3,}|o{3,}).*$', text)
  # entry.append(bool(m))

  features.append(entry)
  targets.append(tweet['mood'])

with open('./data/06features.json', 'w') as file:
  json.dump(features, file)

with open('./data/07targets.json', 'w') as file:
  json.dump(targets, file)
