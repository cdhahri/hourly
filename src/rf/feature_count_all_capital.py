#!/usr/bin/python3

r = './training.1600000.processed.noemoticon.csv'
w = './data_tmp/count_all_capital.json'

with open(r, newline='', encoding='latin-1') as file:
  import csv
  csv_reader = csv.reader(file, delimiter=',')
  out = []
  for row in csv_reader:
    words = row[5].split()
    all_capital = 0
    for word in words:
      if len(word) > 3 and word.isupper():
        all_capital += 1
    out.append(all_capital)

import json
with open(w, 'w') as file:
  json.dump(out, file)
