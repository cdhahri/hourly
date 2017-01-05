#!/usr/bin/python3

import csv, json
        
def process(r, w):
  with open(r, newline='', encoding='latin-1') as file:
    csv_reader = csv.reader(file, delimiter=',')
    out = []
    for row in csv_reader:
      words = row[5].split()
      all_capital = 0
      for word in words:
        if len(word) > 3 and word.isupper():
          all_capital += 1
      out.append(all_capital)

  with open(w, 'w') as file:
    json.dump(out, file)

with open('../ids.json', 'r') as file:
  ids = json.load(file)

for user_id in ids:
  r = '../tweets_raw/csv/{}.csv'.format(user_id)
  w = '../tweets_raw/features_step1/{}count_all_capital.json'.format(user_id)
  process(r, w)
