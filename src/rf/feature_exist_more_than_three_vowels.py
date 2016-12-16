#!/usr/bin/python3

r = './training.1600000.processed.noemoticon.csv'
w = 'data_tmp/exist_more_than_three_vowels.json'

with open(r, newline='', encoding='latin-1') as file:
  import csv
  csv_reader = csv.reader(file, delimiter=',')
  out = []
  for row in csv_reader:
    import re
    m = re.search('^.*[a,i,u,e,o]{3,}.*$', row[5])
    out.append(bool(m))

import json
with open(w, 'w') as file:
  json.dump(out, file)
