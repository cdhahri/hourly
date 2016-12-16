#!/usr/bin/python3

import json

with open('./data/positive.json', 'r') as file:
  positive = json.load(file)

r = './training.1600000.processed.noemoticon.csv'
w = './data_tmp/exist_positive_word.json'

with open(r, newline='', encoding='latin-1') as file:
  import csv
  csv_reader = csv.reader(file, delimiter=',')
  out = []
  for row in csv_reader:
    exist = False
    for word in positive:
      if word in row[5]:
        exist = True
        break
    out.append(exist)

with open(w, 'w') as file:
  json.dump(out, file)
