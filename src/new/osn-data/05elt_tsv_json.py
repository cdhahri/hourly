#!/usr/bin/python3

import json
        
def process(r, w):
  with open(r, newline='', encoding='latin-1') as file:
    import csv
    csv_reader = csv.reader(file, delimiter='\t')
    out = {}
    first_line = True
    for row in csv_reader:
      if first_line:
        first_line = False
        continue
      out[row[2]] = [row[0], row[1]]

  import json
  with open(w, 'w') as file:
    json.dump(out, file)

with open('./ids.json', 'r') as file:
  ids = json.load(file)

for user_id in ids:
  r = './tweets_raw/words/{}0_out.txt'.format(user_id)
  w = './tweets_raw/words/json/{}.json'.format(user_id)
  process(r, w)
