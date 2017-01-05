#!/usr/bin/python3

import csv, json
        
def process(r, w):
  with open(r, newline='', encoding='latin-1') as file:
    csv_reader = csv.reader(file, delimiter=',')
    out = []
    for row in csv_reader:
      out.append(row[5].count('?'))

  with open(w, 'w') as file:
    json.dump(out, file)

with open('../ids.json', 'r') as file:
  ids = json.load(file)

for user_id in ids:
  r = '../tweets_raw/csv/{}.csv'.format(user_id)
  w = '../tweets_raw/features_step1/{}count_question_mark.json'.format(user_id)
  process(r, w)
