#!/usr/bin/python3

import json
        
with open('/vagrant/data/osn-data/ids.json', 'r') as file:
  ids = json.load(file)

def process(r, w):
  with open(r, newline='', encoding='latin-1') as file:
    import csv
    csv_reader = csv.reader(file, delimiter=',')
    out = []
    for row in csv_reader:
      out.append(row[5].count('?'))

  import json
  with open(w, 'w') as file:
    json.dump(out, file)

for user_id in ids:
  r = '/vagrant/data/osn-data/tweets/csv/{}.csv'.format(user_id)
  w = '/vagrant/data/osn-data/features_step1/{}count_question_mark.json'.format(user_id)
  process(r, w)

'''
path = '/vagrant/data/osn-data/tweets/mentions/past_tweets/csv'
from os import listdir
from os.path import isfile, join
files = [f for f in listdir(path) if isfile(join(path, f)) and f.endswith('.csv')]

for f in files:
  import re
  user_id = re.search('^(.*)\.csv$', f).group(1)
  r = '/vagrant/data/osn-data/tweets/mentions/past_tweets/csv/{}.csv'.format(user_id)
  w = '/vagrant/data/osn-data/features_step1/mentions/past_tweets/{}count_question_mark.json'.format(user_id)
  process(r, w)
'''
