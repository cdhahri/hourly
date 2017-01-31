#!/usr/bin/python3

import json
        
out = {}
first_line = True

with open('./data/04.txt', newline='', encoding='latin-1') as file:
  import csv
  csv_reader = csv.reader(file, delimiter='\t')
  for row in csv_reader:
    if first_line:
      first_line = False
      continue
    out[row[2]] = [row[0], row[1]]

with open('./data/05words.json', 'w') as file:
  json.dump(out, file)

out = {}
first_line = True

with open('./data/04_pos.txt', newline='', encoding='latin-1') as file:
  import csv
  csv_reader = csv.reader(file, delimiter='\t')
  for row in csv_reader:
    if first_line:
      first_line = False
      continue
    out[row[2]] = [row[0], row[1]]

with open('./data/05unigrams_pos.json', 'w') as file:
  json.dump(out, file)

out = {}
first_line = True

with open('./data/04_neg.txt', newline='', encoding='latin-1') as file:
  import csv
  csv_reader = csv.reader(file, delimiter='\t')
  for row in csv_reader:
    if first_line:
      first_line = False
      continue
    out[row[2]] = [row[0], row[1]]

with open('./data/05unigrams_neg.json', 'w') as file:
  json.dump(out, file)
