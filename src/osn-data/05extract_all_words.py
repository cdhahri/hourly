#!/usr/bin/python3

import json
        
with open('/vagrant/data/osn-data/ids.json', 'r') as file:
  ids = json.load(file)
  
def process(r, w):
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
    # remove hashtag from words
    m = re.match('^#(.+)$', key)
    if m is not None:
      hashset[m.group(1)] = None
      keys_to_delete.append(key)

  for key in keys_to_delete:
    del hashset[key]

  out = '\n'.join(sorted(hashset.keys()))

  with open(w, 'w', encoding='latin-1') as file:
    file.write(out)
  
for user_id in ids:
  r = '/vagrant/data/osn-data/tweets/csv/{}.csv'.format(user_id)
  w = '/vagrant/data/osn-data/tweets/words/{}.txt'.format(user_id)
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
  w = '/vagrant/data/osn-data/tweets/mentions/past_tweets/words/{}.txt'.format(user_id)
  process(r, w)
'''
