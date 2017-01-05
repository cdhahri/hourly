#!/usr/bin/python3

import csv, json
        
def process(r, w):
  with open(r, newline='', encoding='latin-1') as file:
    csv_reader = csv.reader(file, delimiter=',')
    out = []
    for row in csv_reader:
      import re
      m = re.search('^.*(\.){3,}.*$', row[5])
      out.append(bool(m))

  with open(w, 'w') as file:
    json.dump(out, file)

with open('../ids.json', 'r') as file:
  ids = json.load(file)
    
for user_id in ids:
  r = '../tweets_raw/csv/{}.csv'.format(user_id)
  w = '../tweets_raw/features_step1/{}exist_more_than_three_dots.json'.format(user_id)
  process(r, w)
