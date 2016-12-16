#!/usr/bin/python3

import json

with open('./data/all_words.json', 'r') as file:
  all_words = json.load(file)

r = './training.1600000.processed.noemoticon.csv'
w = './data_tmp/feature_count_positive_word.json'

with open(r, newline='', encoding='latin-1') as file:
  import csv
  csv_reader = csv.reader(file, delimiter=',')
  out = []
  for row in csv_reader:
    words = row[5].split()
    positive = 0
    for word in words:
      if word in all_words:
        score = int(all_words[word][0]) - abs(int(all_words[word][1]))
        if score > 0:
          positive += 1
    out.append(positive)

with open(w, 'w') as file:
  json.dump(out, file)
