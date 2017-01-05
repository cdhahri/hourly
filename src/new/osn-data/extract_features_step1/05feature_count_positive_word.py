#!/usr/bin/python3

import csv, json

def process(r, w, words_path):
  with open(words_path, 'r') as file:
    all_words = json.load(file)
  
  with open(r, newline='', encoding='latin-1') as file:
    csv_reader = csv.reader(file, delimiter=',')
    out = []
    for row in csv_reader:
      words = row[5].split()
      positive = 0
      for word in words:
        if word in all_words:
          score = int(all_words[word][0]) + int(all_words[word][1])
          if score > 0:
            positive += 1
      out.append(positive)

  with open(w, 'w') as file:
    json.dump(out, file)

with open('../ids.json', 'r') as file:
  ids = json.load(file)

for user_id in ids:
  r = '../tweets_raw/csv/{}.csv'.format(user_id)
  w = '../tweets_raw/features_step1/{}count_positive_word.json'.format(user_id)
  words_path = '../tweets_raw/words/json/{}.json'.format(user_id)
  process(r, w, words_path)
