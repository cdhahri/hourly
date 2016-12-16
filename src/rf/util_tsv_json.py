#!/usr/bin/python3

r = './data/all_words0_out.txt'
w = './data/all_words.json'

with open(r, newline='', encoding='latin-1') as file:
  import csv
  csv_reader = csv.reader(file, delimiter='\t')
  out = {}
  for row in csv_reader:
    out[row[2]] = [row[0], row[1]]

import json
with open(w, 'w') as file:
  json.dump(out, file)
