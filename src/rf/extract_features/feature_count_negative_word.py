#!/usr/bin/python3

import json

allwords = ['../data_tmp/train/all_words.json','../data_tmp/test/all_words.json']
r = ['../data_tmp/train.csv','../data_tmp/test.csv']
w = ['../data_tmp/train/count_negative_word.json','../data_tmp/test/count_negative_word.json']

for i in range(2):
  with open(allwords[i], 'r') as file:
    all_words = json.load(file)

  with open(r[i], newline='', encoding='latin-1') as file:
    import csv
    csv_reader = csv.reader(file, delimiter=',')
    out = []
    for row in csv_reader:
      words = row[5].split()
      negative = 0
      for word in words:
        if word in all_words:
          score = int(all_words[word][0]) - abs(int(all_words[word][1]))
          if score < 0:
            negative += 1
      out.append(negative)

  with open(w[i], 'w') as file:
    json.dump(out, file)
