#!/usr/bin/python3

import json, re
import classifier

with open('./data/02.json', 'r') as file:
  tweets = json.load(file)
with open('./data/05words.json', 'r') as file:
  all_words = json.load(file)
with open('./data/05unigrams_pos.json', 'r') as file:
  unigrams_pos = json.load(file)
with open('./data/05unigrams_neg.json', 'r') as file:
  unigrams_neg = json.load(file)

with open('./pattern_based/02features.json', 'r') as file:
  features_pattern_based_all = json.load(file)

features = []
targets = []

for tweet in tweets:
  text = tweet['text']
  words = text.split()

  entry = []

  # SENTIMENT BASED FEATURES
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

  # hashtag + - neutral
  hashtag_pos = 0
  hashtag_neg = 0
  hashtag_neu = 0
  for word in words:
    m = re.match('^#(.+)$', word)
    if m is not None:
      hashtag_stripped = m.group(1)
      hashtag_stripped_pos =     int(all_words[hashtag_stripped][0])
      hashtag_stripped_neg = abs(int(all_words[hashtag_stripped][1]))
      if hashtag_stripped_pos > hashtag_stripped_neg:
        hashtag_pos += 1
      elif hashtag_stripped_pos > hashtag_stripped_neg:
        hashtag_neg += 1
      else:
        hashtag_neu += 1
  entry.append(hashtag_pos)
  entry.append(hashtag_neg)
  entry.append(hashtag_neu)

  # emoticons
  icons_pos_set = [":‑)", ":-)", ":)", ":‑]", ":-]", ":]", ":-3", ":3", ":->", ":>", "8-)", "8)", ":-}", ":}", ":o)", ":c)", ":^)", "=]", "=)", ":‑D", ":D", "8‑D", "8D", "x‑D", "xD", "X‑D", "XD", "=D", "=3", "B^D", ":-))", ";‑)", ";-)", ";)", "*-)", "*)", ";‑]", ";]", ";^)", ":‑,", ";D", ":‑P", ":P", "X‑P", "XP", "x‑p", "xp", ":‑p", ":p", ":‑Þ", ":Þ", ":‑þ", ":þ", ":‑b", ":b", "d:", "=p", ">:P"]
  icons_neg_set = [":‑(", ":-(", ":(", ":‑c", ":c", ":‑<", ":<", ":‑[", ":[", ":-||", ">:[", ":{", ":@", ">:(", ":'‑(", ":'(", "D‑':", "D:<", "D:", "D8", "D;", "D=", "DX", ":‑/", ":/", ":‑.", ">:\\", ">:/", ":\\", "=/", "=\\", ":L", "=L", ":S"]
  icons_pos = 0
  icons_neg = 0
  for icon in icons_pos_set:
    if icon in text:
      icons_pos += 1
  for icon in icons_neg_set:
    if icon in text:
      icons_neg += 1
  entry.append(icons_pos)
  entry.append(icons_neg)



  # PUNCTUATION AND SYNTAX BASED FEATURES
  # count all capitals
  all_capital = 0
  for word in words:
    if len(word) >= 3 and word.isupper():
      all_capital += 1
  entry.append(all_capital)

  # exclamation mark
  entry.append(text.count('!'))

  # question mark
  entry.append(text.count('?'))

  # more than three dots
  m = re.search('^.*(\.){3,}.*$', text)
  entry.append(bool(m))

  # more than three vowels
  m = re.search('^.*(a{3,}|i{3,}|u{3,}|e{3,}|o{3,}).*$', text)
  entry.append(bool(m))



  # PATTERN BASED FEATURES
  features_pattern_based = features_pattern_based_all[text]
  for i in range(3, 11):
    length = str(i)
    entry.append(features_pattern_based['-1'][length])
    entry.append(features_pattern_based['1'][length])

  # UNIGRAM BASED FEATURES
  # total score +
  total_pos = 0
  for word in words:
    if word in unigrams_pos:
      total_pos += int(unigrams_pos[word][0])
  entry.append(total_pos)

  # total score -
  total_neg = 0
  for word in words:
    if word in unigrams_neg:
      total_neg += abs(int(unigrams_neg[word][1]))
  entry.append(total_neg)

  features.append(entry)
  targets.append(tweet['mood'])

with open('./data/06features.json', 'w') as file:
  json.dump(features, file)

with open('./data/07targets.json', 'w') as file:
  json.dump(targets, file)
