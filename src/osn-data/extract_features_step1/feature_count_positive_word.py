#!/usr/bin/python3

import json

with open('/vagrant/data/osn-data/ids.json', 'r') as file:
  ids = json.load(file)

def process(r, w, words_path):
  with open(words_path, 'r') as file:
    all_words = json.load(file)
  
  with open(r, newline='', encoding='latin-1') as file:
    import csv
    csv_reader = csv.reader(file, delimiter=',')
    out = []
    for row in csv_reader:
      words = row[5].split()
      positive = 0
      for word in words:
        if word in all_words:
          score = int(all_words[word][0]) - abs(int(all_words[word][1]))
          if score > 0:
            positive += 1
      out.append(positive)

  with open(w, 'w') as file:
    json.dump(out, file)

for user_id in ids:
  r = '/vagrant/data/osn-data/tweets/csv/{}.csv'.format(user_id)
  w = '/vagrant/data/osn-data/features_step1/{}count_positive_word.json'.format(user_id)
  words_path = '/vagrant/data/osn-data/tweets/words/json/{}.json'.format(user_id)
  process(r, w, words_path)

'''
path = '/vagrant/data/osn-data/tweets/mentions/past_tweets/csv'
from os import listdir
from os.path import isfile, join
files = [f for f in listdir(path) if isfile(join(path, f)) and f.endswith('.csv')]

for f in files:
  import re
  user_id = re.search('^(.*)\.csv$', f).group(1)
  r = '/vagrant/data/osn-data/tweets/mentions/past_tweets/csv/{}.csv'.format(user_id)
  w = '/vagrant/data/osn-data/features_step1/mentions/past_tweets/{}count_positive_word.json'.format(user_id)
  words_path = '/vagrant/data/osn-data/tweets/mentions/past_tweets/words/json/{}.json'.format(user_id)
  process(r, w, words_path)
'''
