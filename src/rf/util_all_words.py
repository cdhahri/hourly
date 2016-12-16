#!/usr/bin/python3

r = './training.1600000.processed.noemoticon.csv'
w = './data/all_words.txt'

with open(r, newline='', encoding='latin-1') as file:
  import csv
  csv_reader = csv.reader(file, delimiter=',')
  hashset = {}
  for row in csv_reader:
    words = row[5].split()
    for word in words:
     hashset[word] = None

# clean
import re
keys_to_delete = []
for key in sorted(hashset.keys()):
  if bool(re.search('^!.*', key)):
    keys_to_delete.append(key)
  if bool(re.search('^#.*', key)):
    keys_to_delete.append(key)
  if bool(re.search('^@.*', key)):
    keys_to_delete.append(key)

for key in keys_to_delete:
  del hashset[key]

out = '\n'.join(sorted(hashset.keys()))

import json
with open(w, 'w', encoding='latin-1') as file:
  file.write(out)
