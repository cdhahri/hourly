#!/usr/bin/python3

r = './training.1600000.processed.noemoticon.csv'
w = './data_tmp/count_exclamation_mark.json'

with open(r, newline='', encoding='latin-1') as file:
  import csv
  csv_reader = csv.reader(file, delimiter=',')
  out = []
  for row in csv_reader:
    out.append(row[5].count('!'))

import json
with open(w, 'w') as file:
  json.dump(out, file)
